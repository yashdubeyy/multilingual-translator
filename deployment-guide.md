# Deployment Guide for TranslateNow

This guide provides detailed instructions for deploying the TranslateNow application on Render.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Preparing Your Repository](#preparing-your-repository)
- [Creating a Render Account](#creating-a-render-account)
- [Deploying to Render](#deploying-to-render)
- [Monitoring and Troubleshooting](#monitoring-and-troubleshooting)
- [Custom Domain Configuration](#custom-domain-configuration)
- [Managing Environment Variables](#managing-environment-variables)
- [Scaling and Performance](#scaling-and-performance)

## Prerequisites

Before deploying your application, make sure you have:

- A complete, working version of the TranslateNow application on your local machine
- A GitHub account
- Git installed on your computer
- The following files in your project:
  - `render.yaml`
  - `build.sh`
  - `requirements.txt`
  - `Procfile`

## Preparing Your Repository

### 1. Initialize Git Repository (if not already done)

```bash
cd path/to/your/project
git init
```

### 2. Add Project Files to Git

```bash
git add .
git commit -m "Initial commit for deployment"
```

### 3. Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top-right corner and select "New repository"
3. Name your repository (e.g., "multilingual-translator")
4. Choose public or private visibility
5. Do not initialize the repository with any files
6. Click "Create repository"

### 4. Link Local Repository to GitHub

```bash
git remote add origin https://github.com/yashdubeyy/multilingual-translator.git
git branch -M main
git push -u origin main
```

## Creating a Render Account

1. Go to [Render's website](https://render.com/)
2. Click "Sign Up" in the top-right corner
3. You can sign up with your GitHub account for easier integration
4. Complete the registration process

## Deploying to Render

### 1. Create a New Web Service

1. Log in to your Render dashboard
2. Click the "New +" button and select "Web Service"

### 2. Connect Your Repository

1. If you haven't connected your GitHub account, you'll be prompted to do so
2. Select the repository you created earlier
3. Authorize Render to access your repositories if prompted

### 3. Configure Your Service

Since you have a `render.yaml` file, many settings will be automatically configured:

1. **Name**: "multilingual-translator" (or the name specified in your render.yaml)
2. **Environment**: Python
3. **Region**: Choose the region closest to your users
4. **Branch**: main
5. **Build Command**: "./build.sh" (from render.yaml)
6. **Start Command**: "gunicorn -w 2 -k uvicorn.workers.UvicornWorker 'translator.app:app'" (from render.yaml)
7. **Plan**: Free (as specified in render.yaml)

Review the settings to ensure they match your render.yaml configuration, then click "Create Web Service".

### 4. Deployment Process

1. Render will begin the deployment process, which includes:
   - Cloning your repository
   - Running the build command
   - Installing dependencies
   - Starting your application

2. This process may take 10-15 minutes, especially for the first deployment, due to:
   - Downloading and installing Python packages
   - Downloading machine learning models
   - Compiling dependencies

3. You can monitor the deployment progress in the "Events" tab of your service

## Monitoring and Troubleshooting

### View Logs

1. Navigate to your web service in the Render dashboard
2. Select the "Logs" tab
3. You can filter logs by:
   - Build logs
   - Runtime logs
   - System logs

### Common Issues and Solutions

#### Memory Limitations

**Issue**: The free tier has 512MB RAM, which may be insufficient for multiple ML models.

**Solutions**:
- Modify your code to load models on demand and unload unused ones
- Use smaller, quantized models
- Implement a caching strategy
- Upgrade to a paid plan with more resources

#### Cold Starts

**Issue**: On the free tier, your service will spin down after 15 minutes of inactivity.

**Solutions**:
- Set up a health check service to ping your application
- Inform users about potential initial delays
- Implement a loading screen for first-time users
- Upgrade to a paid plan to avoid spin-downs

#### Storage Limitations

**Issue**: The free tier has limited disk space for storing models.

**Solutions**:
- Stream models from Hugging Face Hub instead of storing them locally
- Use model quantization to reduce size
- Implement a cleanup strategy to remove unused models

## Custom Domain Configuration

### 1. Add a Custom Domain

1. Go to the "Settings" tab of your Render service
2. Scroll to the "Custom Domain" section
3. Click "Add Domain"
4. Enter your domain name (e.g., translator.yourdomain.com)
5. Follow the instructions to verify your domain

### 2. Configure DNS

1. Go to your domain registrar's website
2. Add a CNAME record pointing to your Render URL:
   - Type: CNAME
   - Name: translator (or whatever subdomain you want)
   - Value: your-app.onrender.com (your Render URL without https://)
   - TTL: 3600 (or as recommended by your registrar)

3. Wait for DNS propagation (can take up to 48 hours, but usually much less)

## Managing Environment Variables

### Adding Environment Variables

1. Go to the "Environment" tab in your Render dashboard
2. Click "Add Environment Variable"
3. Enter the key-value pairs for your variables
4. Click "Save Changes"

### Secret Environment Variables

For sensitive information like API keys:

1. Add them as environment variables in the Render dashboard
2. Mark them as "secret" to encrypt them
3. Reference them in your code using `os.environ.get('VARIABLE_NAME')`

## Scaling and Performance

### Upgrading Your Plan

If you need more resources:

1. Go to the "Settings" tab of your service
2. Under "Plan", click "Change Plan"
3. Select a plan that meets your requirements
4. Confirm your selection

### Auto-scaling (Paid Plans Only)

For services on paid plans:

1. Go to the "Settings" tab
2. Scroll to "Scaling"
3. Configure your auto-scaling preferences
4. Click "Save Changes"

### Performance Monitoring

1. Use the "Metrics" tab to monitor:
   - CPU usage
   - Memory usage
   - Network traffic
   - Response times

2. Set up alerts for critical metrics to be notified of issues

---

By following this guide, you should be able to successfully deploy your Multilingual Text Translator application on Render and configure it for optimal performance.

For further assistance, refer to the [Render Documentation](https://render.com/docs) or contact Render support.
