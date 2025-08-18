@echo off
echo Building and deploying multilingual translator Docker container...

echo Step 1: Building Docker image...
docker build -t multilingual-translator .

echo Step 2: Starting Docker container...
docker-compose up -d

echo Done! Your multilingual translator is now running at http://localhost:5000
echo To view logs: docker logs multilingual_translator
echo To stop the container: docker-compose down