# LinguaSync: Multilingual Translator with Docker

A powerful multilingual translation application that uses Hugging Face Transformers models to provide high-quality translations between multiple languages. This version is specifically configured for Docker deployment.

## Features

- Translate between multiple languages (English, Hindi, French, Spanish, German)
- Modern, responsive user interface
- Memory-optimized for deployment environments
- Health check endpoint for monitoring
- Docker-ready configuration

## Quick Start with Docker

The easiest way to deploy this application is using Docker:

```bash
# Clone the repository (if you haven't already)
git clone https://github.com/yashdubeyy/multilingual-translator.git
cd multilingual-translator

# Build and run with Docker Compose
docker-compose up -d
```

The application will be available at http://localhost:5000

## Manual Setup (without Docker)

If you prefer to run the application directly:

1. Install Python 3.10+
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```

## Environment Variables

- `PORT`: The port to run the application on (default: 5000)
- `DOCKER_DEPLOYMENT`: Set to "true" when running in a Docker environment
- `TRANSFORMERS_OFFLINE`: Control model download behavior (0/1)

## Docker Configuration

The included Docker setup provides:

- Python 3.10 environment
- Optimized memory usage for translation models
- Persistent model cache using Docker volumes
- Resource limits to prevent container issues

See [DOCKER_DEPLOY_GUIDE.md](DOCKER_DEPLOY_GUIDE.md) for detailed Docker deployment instructions.

## Project Structure

```
.
├── Dockerfile                  # Docker build configuration
├── docker-compose.yml          # Docker deployment configuration
├── DOCKER_DEPLOY_GUIDE.md      # Detailed Docker deployment guide
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python version specification
└── translator/                 # Main application package
    ├── __init__.py
    ├── app.py                  # Flask application
    ├── translator.py           # Translation logic
    ├── static/                 # Static assets
    │   └── style.css
    └── templates/              # HTML templates
        ├── base.html
        └── index.html
```

## API Endpoints

- `GET /`: Main translation interface
- `POST /translate`: Translate text between languages
- `GET /translation_status`: Check status of translation task
- `GET /health`: Health check endpoint

## Memory Optimization

The application is optimized for memory usage:

- Models are loaded on demand
- Only one model is kept in memory at a time
- Garbage collection is performed after translations
- Half-precision (FP16) is used for models

## Troubleshooting

If you encounter issues, check the Docker logs:

```bash
docker logs multilingual_translator
```

Common issues:
- **Container crashes**: Check memory limits in docker-compose.yml
- **Slow first translation**: Models are downloaded on first use
- **Translation errors**: Check source/target language compatibility

## License

[MIT License](LICENSE)

## Credits

- Translation models: [Helsinki-NLP/Opus-MT](https://huggingface.co/Helsinki-NLP)
- Framework: Flask
- Model handling: Hugging Face Transformers