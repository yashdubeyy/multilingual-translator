# Multilingual Text Translator

A powerful web-based translator application using Flask and Hugging Face Transformers.

## Features

- Translate text between multiple languages including English, French, Spanish, German, Hindi and more
- User-friendly interface with responsive design
- Translation history management
- Text-to-speech functionality
- Memory-optimized for cloud deployment

## Deployment Instructions for Render

This application is configured for deployment on Render's free tier. Follow these steps to deploy updates:

1. Commit your changes to GitHub:

```bash
git add .
git commit -m "Fix input field responsiveness and improve UI"
git push origin main
```

2. Render will automatically detect changes and rebuild your application.

3. Monitor the build process in your Render dashboard.

4. If you encounter any issues with memory constraints, the application includes optimization features:
   - Memory-efficient model loading
   - Garbage collection between translations
   - Health check endpoint to monitor memory usage

## Local Development

To run the application locally:

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

3. Open your browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- `main.py`: Entry point for the application
- `translator/app.py`: Flask application setup and routes
- `translator/translator.py`: Core translation functionality
- `translator/templates/`: HTML templates
  - `base.html`: Base template with common layout
  - `index.html`: Main translator interface
- `static/style.css`: Custom CSS styles
- `requirements.txt`: Required Python packages
- `render.yaml`: Render deployment configuration

## UI Troubleshooting

If you encounter UI issues like text overflow in input fields, try:

1. Clearing your browser cache
2. Refreshing the page with Ctrl+F5
3. Testing in a different browser

The application is designed to be responsive across desktop and mobile devices.

## Memory Management

When running on Render's free tier, the application uses memory optimization techniques:
- Models are loaded only when needed
- Unused models are unloaded from memory
- Garbage collection is performed regularly

You can monitor memory usage by accessing the `/health` endpoint.
