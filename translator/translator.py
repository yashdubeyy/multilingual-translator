from transformers import MarianMTModel, MarianTokenizer
import torch
import threading
import queue
import time
import uuid

class Translator:
    def __init__(self):
        # Dictionary mapping language pairs to model names
        self.models = {
            'en-fr': 'Helsinki-NLP/opus-mt-en-fr',
            'en-es': 'Helsinki-NLP/opus-mt-en-es',
            'en-de': 'Helsinki-NLP/opus-mt-en-de',
            'en-hi': 'Helsinki-NLP/opus-mt-en-hi',
            'fr-en': 'Helsinki-NLP/opus-mt-fr-en',
            'es-en': 'Helsinki-NLP/opus-mt-es-en',
            'de-en': 'Helsinki-NLP/opus-mt-de-en',
            'hi-en': 'Helsinki-NLP/opus-mt-hi-en',
            # Add more language pairs as needed
        }
        # Cache for loaded models to avoid reloading - limited to 1 model for memory constraints
        self.loaded_models = {}
        self.loaded_tokenizers = {}
        self.max_models_in_memory = 1  # Only keep one model in memory at a time
        
        # Available languages
        self.languages = {
            'en': 'English',
            'fr': 'French',
            'es': 'Spanish',
            'de': 'German',
            'hi': 'Hindi',
            # Add more languages as needed
        }
        
        # For optimized translation
        self.translation_queue = queue.Queue()
        self.translation_results = {}
        self.worker_thread = threading.Thread(target=self._translation_worker, daemon=True)
        self.worker_thread.start()
    
    def get_available_languages(self):
        """Return available languages"""
        return self.languages
    
    def get_model_name(self, source_lang, target_lang):
        """Get the appropriate model name for the language pair"""
        lang_pair = f"{source_lang}-{target_lang}"
        return self.models.get(lang_pair)
    
    def load_model(self, model_name):
        """Load model and tokenizer if not already loaded, with memory management"""
        # If the model is already loaded, return it
        if model_name in self.loaded_models:
            return self.loaded_models[model_name], self.loaded_tokenizers[model_name]
        
        # If we've reached our model limit, clear the oldest model first
        if len(self.loaded_models) >= self.max_models_in_memory:
            # Clear all models to conserve memory
            print(f"Memory limit reached. Clearing models...")
            self.loaded_models = {}
            self.loaded_tokenizers = {}
            # Force garbage collection to free memory
            import gc
            gc.collect()
            torch.cuda.empty_cache() if torch.cuda.is_available() else None
        
        # Now load the new model
        print(f"Loading model: {model_name}")
        try:
            # Use more memory-efficient loading options
            self.loaded_tokenizers[model_name] = MarianTokenizer.from_pretrained(model_name)
            self.loaded_models[model_name] = MarianMTModel.from_pretrained(
                model_name, 
                low_cpu_mem_usage=True,
                torch_dtype=torch.float16,  # Use half-precision to save memory
                local_files_only=False,     # Allow downloading if needed
                force_download=False        # Don't force download if already cached
            )
            
            # Force garbage collection after loading to minimize memory impact
            import gc
            gc.collect()
            
            return self.loaded_models[model_name], self.loaded_tokenizers[model_name]
        except Exception as e:
            print(f"Error loading model {model_name}: {e}")
            # Make error message more descriptive for debugging
            import traceback
            print(f"Detailed error: {traceback.format_exc()}")
            raise
    
    def _translation_worker(self):
        """Background worker that processes translation requests"""
        while True:
            try:
                # Get a translation task from the queue
                task_id, text, source_lang, target_lang = self.translation_queue.get()
                
                # Process the translation
                model_name = self.get_model_name(source_lang, target_lang)
                
                if not model_name:
                    self.translation_results[task_id] = f"Translation not available for {source_lang} to {target_lang}"
                else:
                    try:
                        model, tokenizer = self.load_model(model_name)
                        
                        # Handle large inputs by chunking if needed
                        max_length = 512  # Maximum sequence length most models can handle
                        if len(text) > max_length * 2:  # Rough character to token ratio
                            # Simple chunking for long texts
                            chunks = [text[i:i + max_length * 2] for i in range(0, len(text), max_length * 2)]
                            translated_chunks = []
                            
                            for chunk in chunks:
                                # Process each chunk
                                inputs = tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
                                
                                # Use memory-efficient settings
                                with torch.no_grad():
                                    translated = model.generate(
                                        **inputs,
                                        num_beams=2,  # Reduce beam size to save memory
                                        early_stopping=True,
                                        max_length=max_length
                                    )
                                
                                chunk_text = tokenizer.batch_decode(translated, skip_special_tokens=True)[0]
                                translated_chunks.append(chunk_text)
                            
                            # Join the translated chunks
                            self.translation_results[task_id] = " ".join(translated_chunks)
                        else:
                            # Process as usual for smaller texts
                            inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
                            
                            # Generate translation with memory-efficient settings
                            with torch.no_grad():
                                translated = model.generate(
                                    **inputs,
                                    num_beams=2,  # Reduce beam size to save memory
                                    early_stopping=True,
                                    max_length=max_length * 2
                                )
                            
                            # Decode the generated tokens back to text
                            translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
                            self.translation_results[task_id] = translated_text[0]
                        
                        # Clear some memory after translation
                        import gc
                        gc.collect()
                        torch.cuda.empty_cache() if torch.cuda.is_available() else None
                        
                    except Exception as e:
                        print(f"Translation error: {e}")
                        self.translation_results[task_id] = f"Error translating text: {str(e)[:100]}"
                
                # Mark the task as done
                self.translation_queue.task_done()
            except Exception as e:
                print(f"Error in translation worker: {e}")
                self.translation_results[task_id] = "Server error occurred during translation"
                self.translation_queue.task_done()
                # Continue processing other items even if one fails
                continue
    
    def translate(self, text, source_lang, target_lang):
        """Translate text from source language to target language"""
        # Generate a unique ID for this translation request
        task_id = str(uuid.uuid4())
        
        # Submit the task to the background worker
        self.translation_queue.put((task_id, text, source_lang, target_lang))
        
        # Return the task ID immediately
        return {"task_id": task_id, "status": "processing"}
    
    def get_translation_result(self, task_id):
        """Get the result of a translation task by its ID"""
        if task_id in self.translation_results:
            result = self.translation_results[task_id]
            # Clean up after returning the result
            del self.translation_results[task_id]
            return {"status": "completed", "translation": result}
        else:
            return {"status": "processing"}
