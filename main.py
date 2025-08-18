import os
import sys
import gc
import time
import traceback
from translator.app import app

def print_memory_info():
    """Print memory usage information"""
    try:
        import psutil
        process = psutil.Process(os.getpid())
        memory_info = process.memory_info()
        print(f"Memory usage: {memory_info.rss / 1024 / 1024:.2f} MB")
        
        virtual_mem = psutil.virtual_memory()
        print(f"System memory: {virtual_mem.available / 1024 / 1024:.2f} MB available out of {virtual_mem.total / 1024 / 1024:.2f} MB")
    except ImportError:
        print("psutil not installed, skipping memory info")
    except Exception as e:
        print(f"Error getting memory info: {e}")

def wait_for_models_ready():
    """Pre-download the model with retry to ensure it's ready for use"""
    from transformers import MarianMTModel, MarianTokenizer
    
    # Only do this for the most commonly used model to save memory
    model_name = 'Helsinki-NLP/opus-mt-en-hi'
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            print(f"Pre-downloading tokenizer for {model_name} (attempt {attempt+1}/{max_retries})...")
            tokenizer = MarianTokenizer.from_pretrained(model_name)
            
            # Let's avoid loading the model in advance - it's too memory intensive
            # We'll let it load on first request
            print(f"Tokenizer for {model_name} loaded successfully.")
            return True
        except Exception as e:
            print(f"Error pre-downloading model (attempt {attempt+1}): {e}")
            print(traceback.format_exc())
            time.sleep(5)  # Wait before retry
    
    print("Failed to pre-download models after multiple attempts")
    return False

if __name__ == '__main__':
    print("Starting LinguaSync Translator...")
    print("Running with memory-optimized settings for cloud deployment")
    print("Loading translation models in background. First translations may take longer.")
    
    # Force garbage collection
    gc.collect()
    
    # Print initial memory info
    print_memory_info()
    
    # Set environment variables
    if os.environ.get("RENDER_SERVICE_ID"):
        os.environ["RENDER"] = "true"
        print("Running in Render environment")
    elif os.environ.get("RAILWAY_DEPLOY"):
        print("Running in Railway environment")
    
    # Try to pre-download models, but continue even if it fails
    try:
        wait_for_models_ready()
    except Exception as e:
        print(f"Error in model initialization: {e}")
        print("Continuing startup despite model initialization error")
    
    print("Access the translator at the provided URL")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
