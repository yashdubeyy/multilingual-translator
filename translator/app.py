from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import platform
import sys
from .translator import Translator

# Create Flask application
app = Flask(__name__, static_folder='static', static_url_path='/static')
translator = None  # Initialize lazily to improve startup time

# Configure for production environments
is_production = any([
    os.environ.get('RENDER', False),
    os.environ.get('DOCKER_DEPLOYMENT', False),
    os.environ.get('RAILWAY_DEPLOY', False),
    os.environ.get('HEROKU_APP_NAME', False),
    os.environ.get('DYNO', False),  # Heroku
])

app.config['PRODUCTION'] = is_production

# Print diagnostic information on startup
print(f"Starting LinguaSync Translator in {'production' if is_production else 'development'} mode")
print(f"Python version: {platform.python_version()}")
print(f"Platform: {platform.system()} {platform.release()}")
print(f"System memory: {os.environ.get('MEMORY_AVAILABLE', 'unknown')}")

# Lazy initialization of translator
def get_translator():
    global translator
    if translator is None:
        print("Initializing translator...")
        translator = Translator()
    return translator

@app.route('/')
def index():
    translator_instance = get_translator()
    languages = translator_instance.get_available_languages()
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate_text():
    translator_instance = get_translator()
    text = request.form.get('text', '')
    source_lang = request.form.get('source_lang', 'hi')
    target_lang = request.form.get('target_lang', 'en')
    
    if not text:
        return jsonify({'status': 'completed', 'translation': ''})
    
    # Start the translation process asynchronously
    result = translator_instance.translate(text, source_lang, target_lang)
    return jsonify(result)

@app.route('/translation_status', methods=['GET'])
def translation_status():
    translator_instance = get_translator()
    task_id = request.args.get('task_id', '')
    
    if not task_id:
        return jsonify({'status': 'error', 'message': 'No task ID provided'})
    
    # Check the status of the translation
    result = translator_instance.get_translation_result(task_id)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    translator_instance = get_translator()
    health_data = {
        'status': 'ok',
        'languages_available': list(translator_instance.languages.keys())
    }
    
    try:
        import psutil
        memory_info = psutil.virtual_memory()
        health_data['memory'] = {
            'total': memory_info.total / (1024 * 1024),  # Convert to MB
            'available': memory_info.available / (1024 * 1024),  # Convert to MB
            'percent_used': memory_info.percent
        }
    except ImportError:
        health_data['memory'] = 'psutil not installed'
    except Exception as e:
        health_data['memory_error'] = str(e)
    
    return jsonify(health_data)

if __name__ == '__main__':
    app.run(debug=True)
