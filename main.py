import os
from translator.app import app

if __name__ == '__main__':
    print("Starting Multilingual Text Translator...")
    print("Loading translation models in background. First translations may take longer.")
    print("Access the translator at http://127.0.0.1:5000")
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
