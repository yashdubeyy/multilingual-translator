import gradio as gr
import threading
import time
from translator.app import app

def start_flask():
    app.run(host="0.0.0.0", port=5000, debug=False)

# Start Flask in background
flask_thread = threading.Thread(target=start_flask, daemon=True)
flask_thread.start()
time.sleep(3)  # Wait for Flask to start

# Create Gradio interface that embeds Flask app
with gr.Blocks(title="LinguaSync Translator") as demo:
    gr.HTML('<iframe src="http://localhost:5000" width="100%" height="800px" frameborder="0"></iframe>')

if __name__ == "__main__":
    demo.launch()