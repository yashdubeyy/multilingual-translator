import os
import gc
from translator.app import app

# For Hugging Face Spaces deployment
os.environ['MALLOC_TRIM_THRESHOLD_'] = '65536'

if __name__ == '__main__':
    print("Starting LinguaSync Translator for Hugging Face Spaces...")
    
    # Force garbage collection
    gc.collect()
    
    # Set environment for Hugging Face Spaces
    if os.environ.get("SPACE_ID"):
        print("Running in Hugging Face Spaces environment")
    
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
