# Docker Deployment Guide for Multilingual Translator

This guide provides instructions for deploying the Multilingual Translator application using Docker.

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop/) installed on your system
- [Docker Compose](https://docs.docker.com/compose/install/) (usually included with Docker Desktop)

## Quick Start

For Windows users, run:
```
docker-deploy.bat
```

For manual deployment, follow these steps:

## Step 1: Build the Docker Image

```bash
docker build -t multilingual-translator .
```

## Step 2: Run with Docker Compose

```bash
docker-compose up -d
```

Your application will now be available at http://localhost:5000

## Managing Your Docker Container

### View Logs

```bash
docker logs multilingual_translator
```

### Stop the Container

```bash
docker-compose down
```

### Restart the Container

```bash
docker-compose restart
```

## Understanding the Docker Configuration

- **Dockerfile**: Defines how the application image is built
- **docker-compose.yml**: Configures the runtime environment
- **.dockerignore**: Lists files excluded from the image

## Memory Considerations

The application is configured to use a maximum of 2GB memory. If you need to adjust this:

1. Open `docker-compose.yml`
2. Modify the `memory` value under `deploy > resources > limits`

## Persistent Model Cache

The Hugging Face models are cached in a Docker volume (`huggingface_cache`) to:
- Speed up container restarts
- Reduce bandwidth usage
- Improve startup time

## Deploying to Cloud Platforms

### Deploy to DigitalOcean App Platform

1. Create a DigitalOcean account
2. Install the [doctl](https://docs.digitalocean.com/reference/doctl/how-to/install/) CLI
3. Authenticate with `doctl auth init`
4. Build and push your container:
   ```
   docker build -t registry.digitalocean.com/your-registry/multilingual-translator:latest .
   docker push registry.digitalocean.com/your-registry/multilingual-translator:latest
   ```
5. Deploy through the DigitalOcean App Platform UI

### Deploy to AWS Elastic Container Service (ECS)

1. Create an ECR repository
2. Build and push your image:
   ```
   aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin your-aws-account-id.dkr.ecr.your-region.amazonaws.com
   docker build -t your-aws-account-id.dkr.ecr.your-region.amazonaws.com/multilingual-translator:latest .
   docker push your-aws-account-id.dkr.ecr.your-region.amazonaws.com/multilingual-translator:latest
   ```
3. Create an ECS task definition, service, and cluster

## Troubleshooting

### Container Exits Immediately

Check the logs for errors:
```bash
docker logs multilingual_translator
```

### Memory Issues

The application requires significant memory for the translation models. If you see memory-related errors:

1. Increase the memory limit in `docker-compose.yml`
2. If on a cloud platform, choose an instance with more memory

### Model Download Issues

If models fail to download:

1. Check your internet connection
2. Try running in offline mode by adding this to docker-compose.yml environment section:
   ```
   - TRANSFORMERS_OFFLINE=0
   ```

### Container Won't Start

Ensure ports are not already in use:
```bash
netstat -ano | findstr :5000
```

## License

This Docker configuration is provided under the same license as the Multilingual Translator application.