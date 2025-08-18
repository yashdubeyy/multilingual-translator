# How to Deploy Your Translator Application with Docker

## Prerequisites
Before you begin, make sure you have:

1. Docker Desktop installed and running (you have Docker version 28.3.2 installed)
2. Sufficient memory on your machine (at least 4GB free RAM recommended)

## Step 1: Start Docker Desktop

1. Find Docker Desktop in your Start menu and launch it
2. Wait for Docker to fully initialize (the Docker icon in your system tray should stop animating)
3. Verify Docker is running with:
   ```
   docker ps
   ```

## Step 2: Build Your Docker Image

1. Open a command prompt
2. Navigate to your project directory:
   ```
   cd c:\Users\hp\Desktop\NLP_Project
   ```
3. Build the Docker image:
   ```
   docker build -t multilingual-translator .
   ```
   This may take several minutes as it downloads the base image and installs dependencies.

## Step 3: Run Your Application

1. Start the container using Docker Compose:
   ```
   docker-compose up -d
   ```
2. Check that the container is running:
   ```
   docker ps
   ```
   You should see your container named "multilingual_translator" in the list.

## Step 4: Access Your Application

1. Open a web browser
2. Go to http://localhost:5000
3. You should see your translator application

## Monitoring and Management

- View container logs:
  ```
  docker logs multilingual_translator
  ```

- Stop the application:
  ```
  docker-compose down
  ```

- Restart the application:
  ```
  docker-compose restart
  ```

## Troubleshooting

### Docker Desktop Not Running
If you see errors like "cannot connect to Docker daemon" or "open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified":
1. Make sure Docker Desktop is running
2. Try restarting Docker Desktop
3. Check if Docker service is enabled in Windows Services

### Container Exits Immediately
If the container starts but exits right away:
1. Run with console output to see errors:
   ```
   docker-compose up
   ```
2. Check logs:
   ```
   docker logs multilingual_translator
   ```

### Memory Issues
If you see out-of-memory errors:
1. Edit docker-compose.yml and increase the memory limit
2. Make sure your computer has enough free memory
3. Close other memory-intensive applications

## Deploying to Production

When you're ready to deploy to a production server:

1. Make sure Docker is installed on your server
2. Clone your repository to the server
3. Run the same build and deploy commands
4. Consider using a reverse proxy like Nginx for SSL and better security

## Alternative Deployment Options

If Docker deployment is challenging, consider these alternatives:

1. **Heroku**: Deploy using their Python buildpack
2. **Render**: Use their free tier for Python applications
3. **DigitalOcean App Platform**: Simple deployment with their UI
4. **Amazon Elastic Beanstalk**: AWS's platform-as-a-service option