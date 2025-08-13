# TranslateNow

A modern, feature-rich web application that enables real-time translation between multiple languages using state-of-the-art machine learning models.

![TranslateNow]


<img width="1919" height="1079" alt="Screenshot 2025-08-13 234612" src="https://github.com/user-attachments/assets/82791513-1a6e-4eb0-b881-da9eb911a320" />


## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Translation Process](#translation-process)
- [Responsive Design](#responsive-design)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)

## Overview

TranslateNow is a web-based application that leverages Hugging Face's MarianMT neural machine translation models to provide high-quality translations between English, French, Spanish, German, Hindi, and potentially other languages. The application features a modern, responsive user interface with real-time translation, history tracking, and various interactive elements that enhance the user experience.

## Features

### Core Functionality
- **Multi-language Support**: Translate between English, French, Spanish, German, and Hindi
- **Real-time Translation**: Text is automatically translated after typing stops
- **Language Swapping**: Easily switch source and target languages
- **Translation History**: Keep track of previous translations in a sidebar
- **Local Storage**: Translation history persists across browser sessions

### User Interface
- **Modern Design**: Clean, intuitive interface with responsive layout
- **Interactive Elements**: Animations, toast notifications, and visual feedback
- **Responsive Layout**: Works on desktop, tablet, and mobile devices
- **Text-to-Speech**: Listen to both source and translated text
- **Copy to Clipboard**: One-click copying of source or translated text
- **Character Counter**: Track the length of your text in real-time
- **Progress Indicators**: Visual feedback during translation process

### Technical Highlights
- **Asynchronous Processing**: Translations run in the background to keep UI responsive
- **Task Management**: Unique identifiers for tracking translation tasks
- **Error Handling**: Graceful handling of translation errors
- **Mobile Optimizations**: Touch gestures, viewport adaptations, and mobile-specific UI adjustments

## Technology Stack

### Frontend
- **HTML5/CSS3**: Modern markup and styling
- **JavaScript**: Client-side interaction and AJAX requests
- **Bootstrap 5**: Responsive design framework
- **Animate.css**: CSS animation library
- **Bootstrap Icons**: Icon library

### Backend
- **Python 3.13**: Core programming language
- **Flask 2.3.2**: Web framework for handling routes and serving the application
- **Hugging Face Transformers 4.30.2**: Machine learning library for translation models
- **PyTorch 2.6.0**: Deep learning framework supporting the translation models
- **Gunicorn/Uvicorn**: WSGI/ASGI server for production deployment

## Project Structure

```
NLP_Project/
├── build.sh                # Build script for Render deployment
├── main.py                 # Entry point for the application
├── Procfile               # Process file for Render/Heroku
├── render.yaml            # Configuration for Render deployment
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # Custom CSS styles
└── translator/
    ├── __init__.py        # Package initialization
    ├── app.py             # Flask application and routes
    ├── translator.py      # Core translation functionality
    └── templates/
        ├── base.html      # Base template with layout and common elements
        └── index.html     # Main translator interface
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

### Local Setup

1. Clone the repository (or download and extract the ZIP file):
```bash
git clone https://github.com/yashdubeyy/multilingual-translator.git
cd multilingual-translator
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

5. Access the application in your browser:
```
http://127.0.0.1:5000
```

Note: The first time you use the application, it will download the translation models, which may take some time depending on your internet connection.

## Usage

### Basic Translation
1. Select your source language from the dropdown
2. Enter or paste text in the input field
3. Select your target language
4. The translation will appear automatically after you stop typing, or you can click the "Translate" button

### Additional Features
- **Swap Languages**: Click the swap button (↔️) to exchange source and target languages
- **Listen to Text**: Click the speaker button to hear the text spoken aloud
- **Copy Text**: Click the clipboard button to copy text to your clipboard
- **Clear Text**: Use the clear button (✕) to remove all text
- **View History**: Click the history button in the header to see your previous translations
- **Restore Translation**: In the history sidebar, click "Use" to restore a previous translation
- **Remove from History**: Delete individual history items with the trash button
- **Clear All History**: Remove all history items with the "Clear All History" button

## Translation Process

The translation process works as follows:

1. **Model Loading**: When the application starts, it initializes the `Translator` class, which prepares to load translation models on demand.

2. **Language Pair Management**: The application manages translation by creating model pairs (e.g., English to French, French to English) and loads them as needed.

3. **Translation Request**:
   - When text is entered, the client sends an AJAX request to the `/translate` endpoint
   - The server creates a unique task ID and begins processing the translation asynchronously
   - The client periodically polls the `/translation_status` endpoint to check progress

4. **Background Processing**:
   - The appropriate translation model is loaded if not already in memory
   - The text is processed through the model to generate the translation
   - Results are stored in a task dictionary with the task ID as the key

5. **Response Handling**:
   - Once translation is complete, the result is returned to the client
   - The UI is updated with the translated text and animations
   - The translation is added to the history in localStorage

This approach ensures the UI remains responsive even during computationally intensive translations, especially when working with larger text blocks.

## Responsive Design

The application is designed to work seamlessly across various screen sizes:

### Desktop (>992px)
- Full-width layout with side-by-side source and target text areas
- Spacious controls and larger text areas
- Full feature set visible

### Tablet (768px - 992px)
- Adapted layout with optimized spacing
- Slightly reduced padding and margins
- All features remain accessible

### Mobile (< 768px)
- Stacked layout with source text area above target
- Compact controls with icon-only buttons where appropriate
- Swipe gestures for opening/closing the sidebar
- Touch-optimized button sizes and spacing

### Technical Implementation Details
- CSS media queries for responsive breakpoints
- Bootstrap grid system for layout changes
- JavaScript viewport adjustments for mobile browsers
- Touch event handling for swipe gestures
- Mobile-specific optimizations for animations and interactions

## Deployment

The application is configured for deployment on Render, a cloud platform that makes it easy to deploy web services.

### Deployment Files
- `render.yaml`: Defines the service configuration for Render
- `build.sh`: Installation script that runs during deployment
- `Procfile`: Defines the command to start the application
- `requirements.txt`: Lists all Python dependencies

### Deployment Steps
1. Push your code to a GitHub repository
2. Sign up for a Render account at [render.com](https://render.com)
3. Connect your GitHub account to Render
4. Create a new Web Service and select your repository
5. Render will automatically detect your `render.yaml` configuration
6. Click "Create Web Service" to start the deployment process

See the full [Deployment Guide](deployment-guide.md) for detailed instructions.

### Important Considerations
- The free tier of Render has memory limitations that may affect performance with multiple translation models
- Services on the free tier sleep after 15 minutes of inactivity
- Initial load time may be longer due to model loading
- Consider implementing model caching strategies for production deployments

## Future Enhancements

Potential improvements for future versions:

- **Additional Languages**: Expand the language offerings
- **Offline Mode**: Progressive Web App features for offline translation
- **Document Translation**: Support for uploading and translating documents
- **Custom Dictionaries**: Allow users to create custom translations for specific terms
- **Translation Memory**: Improved caching of common translations
- **Speech-to-Text**: Direct voice input for translation
- **User Accounts**: Save translations across devices with user accounts
- **API Access**: Public API for integrating translation capabilities into other applications
- **Mobile Apps**: Native mobile applications for iOS and Android

## Contributing

Contributions are welcome! If you'd like to improve the Multilingual Text Translator:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please ensure your code follows the existing style and include appropriate tests.

---

Created by Yash Dubey | https://github.com/yashdubeyy/multilingual-translator
