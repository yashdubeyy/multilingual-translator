# LinguaSync: Multilingual Translator

A modern web application for real-time translation between multiple languages using Hugging Face MarianMT models.

<img width="1919" height="1079" alt="Screenshot 2025-08-13 234612" src="https://github.com/user-attachments/assets/82791513-1a6e-4eb0-b881-da9eb911a320" />

## 🌟 Features

- **5 Languages**: English, French, Spanish, German, Hindi
- **Real-time Translation**: Auto-translates as you type
- **Language Swapping**: One-click language exchange
- **Translation History**: Persistent local storage
- **Text-to-Speech**: Listen to translations
- **Copy to Clipboard**: Easy text copying
- **Responsive Design**: Works on all devices

## 🚀 Quick Deploy to Hugging Face Spaces (FREE)

### Step 1: Create Account
1. Go to [huggingface.co](https://huggingface.co)
2. Sign up for free account

### Step 2: Create Space
1. Click "Create new" → "Space"
2. **Space name**: `linguasync-translator` (or your choice)
3. **SDK**: Select "Static" 
4. **Visibility**: Public (free)
5. Click "Create Space"

### Step 3: Upload Files
Upload these files to your Space:
```
app.py
main.py
requirements.txt
runtime.txt
README.md
translator/
├── __init__.py
├── app.py
├── translator.py
└── templates/
    ├── base.html
    └── index.html
static/
└── style.css
```

### Step 4: Configure Space
Create/edit these files in your Space:

**`README.md`** (Space header):
```yaml
---
title: LinguaSync Translator
emoji: 🌐
colorFrom: blue
colorTo: purple
sdk: static
app_file: app.py
pinned: false
---

# LinguaSync Translator
Real-time multilingual translation powered by Hugging Face MarianMT models.
```

Your Space will auto-deploy at: `https://huggingface.co/spaces/YOUR_USERNAME/linguasync-translator`

## 📁 Project Structure

```
LinguaSync/
├── app.py              # Main entry point
├── main.py             # Alternative entry
├── requirements.txt    # Dependencies
├── runtime.txt         # Python version
├── translator/
│   ├── app.py         # Flask routes
│   ├── translator.py  # Translation engine
│   └── templates/     # HTML templates
└── static/            # CSS styles
```

## 🛠️ Local Development

```bash
# Clone and setup
git clone <your-repo>
cd linguasync

# Virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
# Visit: http://localhost:7860
```

## 🔧 Technology Stack

- **Backend**: Flask, PyTorch, Transformers
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Models**: Helsinki-NLP MarianMT models
- **Deployment**: Hugging Face Spaces

## 📱 Usage

1. **Select Languages**: Choose source and target languages
2. **Type Text**: Enter text to translate
3. **Auto-Translate**: Translation appears automatically
4. **Use Features**: Swap languages, listen, copy, view history

## 🎯 Supported Language Pairs

- English ↔ French
- English ↔ Spanish  
- English ↔ German
- English ↔ Hindi

## 💡 Tips for Hugging Face Spaces

- **Free Tier**: 2 CPU cores, 16GB RAM
- **Auto-Sleep**: Spaces sleep after inactivity
- **Cold Start**: First load may take 30-60 seconds
- **Persistent**: Your Space URL stays active
- **Custom Domain**: Available with Pro subscription

## 🔗 Links

- [Hugging Face Spaces](https://huggingface.co/spaces)
- [MarianMT Models](https://huggingface.co/Helsinki-NLP)
- [Flask Documentation](https://flask.palletsprojects.com/)

---
**Ready to deploy?** Follow the steps above to get your free translation app live in minutes! 🚀