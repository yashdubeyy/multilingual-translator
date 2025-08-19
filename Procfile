web: gunicorn --bind 0.0.0.0:$PORT --workers 1 --timeout 120 --worker-class uvicorn.workers.UvicornWorker translator.app:app
