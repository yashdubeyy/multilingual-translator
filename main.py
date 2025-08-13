import os
import sys
import gc
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

if __name__ == '__main__':
    print("Starting Multilingual Text Translator...")
    print("Running with memory-optimized settings for cloud deployment")
    print("Loading translation models in background. First translations may take longer.")
    
    # Force garbage collection
    gc.collect()
    
    # Print initial memory info
    print_memory_info()
    
    # Set environment variable to identify Render environment
    if os.environ.get("RENDER_SERVICE_ID"):
        os.environ["RENDER"] = "true"
        print("Running in Render environment")
    
    print("Access the translator at http://127.0.0.1:5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
