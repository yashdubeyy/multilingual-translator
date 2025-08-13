from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from .translator import Translator

app = Flask(__name__, static_folder='static', static_url_path='/static')
translator = Translator()

# Configure for production
app.config['PRODUCTION'] = os.environ.get('RENDER', False)

@app.route('/')
def index():
    languages = translator.get_available_languages()
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.form.get('text', '')
    source_lang = request.form.get('source_lang', 'hi')
    target_lang = request.form.get('target_lang', 'en')
    
    if not text:
        return jsonify({'status': 'completed', 'translation': ''})
    
    # Start the translation process asynchronously
    result = translator.translate(text, source_lang, target_lang)
    return jsonify(result)

@app.route('/translation_status', methods=['GET'])
def translation_status():
    task_id = request.args.get('task_id', '')
    
    if not task_id:
        return jsonify({'status': 'error', 'message': 'No task ID provided'})
    
    # Check the status of the translation
    result = translator.get_translation_result(task_id)
    return jsonify(result)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for monitoring"""
    import psutil
    memory_info = psutil.virtual_memory()
    health_data = {
        'status': 'ok',
        'memory': {
            'total': memory_info.total / (1024 * 1024),  # Convert to MB
            'available': memory_info.available / (1024 * 1024),  # Convert to MB
            'percent_used': memory_info.percent
        },
        'languages_available': list(translator.languages.keys())
    }
    return jsonify(health_data)

if __name__ == '__main__':
    app.run(debug=True)
