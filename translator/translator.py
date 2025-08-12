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
        # Cache for loaded models to avoid reloading
        self.loaded_models = {}
        self.loaded_tokenizers = {}
        
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
        """Load model and tokenizer if not already loaded"""
        if model_name not in self.loaded_models:
            print(f"Loading model: {model_name}")
            self.loaded_models[model_name] = MarianMTModel.from_pretrained(model_name)
            self.loaded_tokenizers[model_name] = MarianTokenizer.from_pretrained(model_name)
        
        return self.loaded_models[model_name], self.loaded_tokenizers[model_name]
    
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
                    model, tokenizer = self.load_model(model_name)
                    
                    # Tokenize and translate
                    inputs = tokenizer(text, return_tensors="pt", padding=True)
                    
                    # Generate translation with no grad to save memory
                    with torch.no_grad():
                        translated = model.generate(
                            **inputs,
                            num_beams=4,  # Beam search for better quality
                            early_stopping=True
                        )
                    
                    # Decode the generated tokens back to text
                    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
                    self.translation_results[task_id] = translated_text[0]
                
                # Mark the task as done
                self.translation_queue.task_done()
            except Exception as e:
                print(f"Error in translation worker: {e}")
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
