# LinguaSync: Multilingual Translator

A modern, professional web application for real-time translation between multiple languages using state-of-the-art Hugging Face MarianMT models.

<img width="1919" height="1079" alt="Screenshot 2025-08-13 234612" src="https://github.com/user-attachments/assets/82791513-1a6e-4eb0-b881-da9eb911a320" />

## 🌟 Features

- **5 Languages**: English, French, Spanish, German, Hindi
- **Real-time Translation**: Auto-translates as you type (800ms delay)
- **Language Swapping**: One-click language exchange with animations
- **Translation History**: Persistent local storage (up to 15 translations)
- **Text-to-Speech**: Listen to both source and translated text
- **Copy to Clipboard**: Easy text copying with visual feedback
- **Language Detection**: Auto-detect source language
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Progress Indicators**: Visual feedback during translation process
- **Memory Optimized**: Efficient model loading for cloud deployment

## 🚀 Live Demo

**Deployed on Hugging Face Spaces**: [Try TranslateNow](https://huggingface.co/spaces/yashdubey/multilingual-translator)

## 🏗️ Architecture Overview

### Backend Components

#### 1. **Flask Application** (`translator/app.py`)
- **Routes**: Main web routes for serving UI and handling API requests
- **Lazy Loading**: Translator instance initialized on first request
- **Health Check**: Monitoring endpoint for deployment status
- **Environment Detection**: Automatically detects Hugging Face Spaces environment

#### 2. **Translation Engine** (`translator/translator.py`)
- **Asynchronous Processing**: Background worker thread for non-blocking translations
- **Memory Management**: Loads only 1 model at a time to conserve memory
- **Model Caching**: Intelligent caching with automatic cleanup
- **Error Handling**: Robust error handling with detailed logging
- **Text Chunking**: Handles long texts by splitting into manageable chunks

#### 3. **Model Management**
- **MarianMT Models**: Uses Helsinki-NLP pre-trained models
- **Half-Precision**: Uses float16 to reduce memory usage
- **Dynamic Loading**: Models loaded on-demand based on language pairs
- **Garbage Collection**: Automatic memory cleanup after translations

### Frontend Components

#### 1. **Base Template** (`translator/templates/base.html`)
- **Responsive Layout**: Bootstrap 5 with custom CSS
- **Modern UI**: Gradient backgrounds, animations, and smooth transitions
- **Sidebar History**: Collapsible translation history panel
- **Mobile Optimized**: Touch gestures and mobile-specific optimizations

#### 2. **Main Interface** (`translator/templates/index.html`)
- **Real-time Translation**: Auto-translation with typing delay
- **Interactive Elements**: Language selectors, swap button, action buttons
- **Progress Tracking**: Visual progress bars and loading indicators
- **Toast Notifications**: User feedback for all actions

#### 3. **Styling** (`static/style.css`)
- **Custom Variables**: CSS custom properties for consistent theming
- **Animations**: Smooth transitions and hover effects
- **Responsive Breakpoints**: Mobile-first responsive design

## 📁 Project Structure

```
LinguaSync/
├── app.py                      # Gradio wrapper for HF Spaces
├── main.py                     # Alternative Flask entry point
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version (3.10.11)
├── translator/                 # Main application package
│   ├── __init__.py            # Package initialization
│   ├── app.py                 # Flask application and routes
│   ├── translator.py          # Core translation engine
│   ├── templates/             # Jinja2 HTML templates
│   │   ├── base.html         # Base layout template
│   │   └── index.html        # Main translator interface
│   └── static/               # Static assets
│       └── style.css         # Custom CSS styles
└── static/                    # Additional static files
    └── style.css             # Backup CSS file
```

## 🔧 Technology Stack

### Backend
- **Python 3.10**: Core programming language
- **Flask 2.3.2**: Lightweight web framework
- **PyTorch 2.0.1**: Deep learning framework
- **Transformers 4.30.2**: Hugging Face transformers library
- **SentencePiece**: Tokenization library for MarianMT models

### Frontend
- **HTML5/CSS3**: Modern web standards
- **JavaScript ES6+**: Client-side interactivity
- **Bootstrap 5**: Responsive CSS framework
- **Animate.css**: CSS animation library
- **Bootstrap Icons**: Icon library

### AI Models
- **Helsinki-NLP MarianMT**: Neural machine translation models
- **Supported Pairs**: 8 translation directions between 5 languages

## 🚀 Deployment Guide for Hugging Face Spaces

### Prerequisites
- Hugging Face account (free)
- Git repository with your code

### Step 1: Prepare Your Repository
Ensure your repository has these files:
```
✅ app.py (Gradio wrapper)
✅ requirements.txt (with gradio>=4.0.0)
✅ runtime.txt (python-3.10.11)
✅ translator/ folder (complete)
✅ static/ folder (complete)
```

### Step 2: Create Hugging Face Space
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
3. Configure:
   - **Name**: `linguasync-translator`
   - **SDK**: **Gradio** ⚠️ (Important!)
   - **Visibility**: Public
   - **Hardware**: CPU Basic (free)

### Step 3: Upload Files
**Option A: Direct Upload**
- Drag and drop all files/folders to your Space

**Option B: Git Integration**
- Connect your GitHub repository in Space settings
- Auto-deploys on every push

### Step 4: Configure Space
Create `README.md` in your Space with this header:

```yaml
---
title: LinguaSync Translator
emoji: 🌐
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
---

# LinguaSync Translator
Professional multilingual translation powered by Hugging Face MarianMT models.

## Features
- Real-time translation between 5 languages
- Modern, responsive web interface
- Translation history and text-to-speech
- Optimized for cloud deployment
```

### Step 5: Monitor Deployment
- Check **"Logs"** tab for build progress
- First build takes 3-5 minutes
- App will be available at: `https://huggingface.co/spaces/yashdubey/multilingual-translator`

## 🛠️ Local Development

### Setup
```bash
# Clone repository
git clone https://github.com/yashdubeyy/multilingual-translator.git
cd multilingual-translator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

### Access
- **Local URL**: http://localhost:7860
- **Health Check**: http://localhost:7860/health

## 📱 Usage Guide

### Basic Translation
1. **Select Languages**: Choose source and target from dropdowns
2. **Enter Text**: Type or paste text in the input area
3. **Auto-Translate**: Translation appears after you stop typing (800ms delay)

### Advanced Features
- **Language Swap**: Click ↔️ button to exchange languages
- **Auto-Detect**: Click "Auto-detect" to identify source language
- **Listen**: Click 🔊 to hear text-to-speech
- **Copy**: Click 📋 to copy text to clipboard
- **History**: Click 🕒 to view translation history
- **Clear**: Use clear buttons to remove text

### Keyboard Shortcuts
- **Enter**: Trigger manual translation
- **Ctrl+A**: Select all text
- **Ctrl+C**: Copy selected text

## 🎯 Supported Language Pairs

| Source | Target | Model |
|--------|--------|-------|
| English | French | Helsinki-NLP/opus-mt-en-fr |
| English | Spanish | Helsinki-NLP/opus-mt-en-es |
| English | German | Helsinki-NLP/opus-mt-en-de |
| English | Hindi | Helsinki-NLP/opus-mt-en-hi |
| French | English | Helsinki-NLP/opus-mt-fr-en |
| Spanish | English | Helsinki-NLP/opus-mt-es-en |
| German | English | Helsinki-NLP/opus-mt-de-en |
| Hindi | English | Helsinki-NLP/opus-mt-hi-en |

## 🔍 API Endpoints

### Translation
```http
POST /translate
Content-Type: application/x-www-form-urlencoded

text=Hello world&source_lang=en&target_lang=fr
```

### Status Check
```http
GET /translation_status?task_id=<uuid>
```

### Health Check
```http
GET /health
```

## 💡 Performance Optimization

### Memory Management
- **Single Model Loading**: Only 1 model in memory at a time
- **Automatic Cleanup**: Garbage collection after each translation
- **Half-Precision**: Uses float16 to reduce memory usage
- **Lazy Loading**: Models loaded on first request

### Translation Optimization
- **Asynchronous Processing**: Non-blocking translation requests
- **Text Chunking**: Handles long texts efficiently
- **Caching**: Intelligent model caching with cleanup
- **Error Recovery**: Graceful handling of translation failures

## 🐛 Troubleshooting

### Common Issues

**Build Fails on Hugging Face Spaces**
- Check `requirements.txt` format
- Ensure `gradio>=4.0.0` is included
- Verify all files are uploaded

**Translation Not Working**
- Check browser console for errors
- Verify model loading in Space logs
- Test with shorter text first

**Memory Issues**
- Models are loaded on-demand
- Only 1 model kept in memory
- Automatic cleanup after translations

**UI Not Loading**
- Ensure `sdk: gradio` in Space README
- Check that `app.py` is the entry point
- Verify Flask app starts correctly

### Debug Mode
For local development, set `debug=True` in `translator/app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📄 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## 🔗 Links

- **Live Demo**: [Hugging Face Spaces](https://huggingface.co/spaces/yashdubey/multilingual-translator)
- **GitHub Repository**: [multilingual-translator](https://github.com/yashdubeyy/multilingual-translator)
- **Hugging Face Models**: [Helsinki-NLP](https://huggingface.co/Helsinki-NLP)
- **Documentation**: [Flask](https://flask.palletsprojects.com/) | [Transformers](https://huggingface.co/docs/transformers)

---

**Ready to deploy your own translation service?** Follow the deployment guide above and get your app live in minutes! 🚀
