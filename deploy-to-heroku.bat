@echo off
echo === LinguaSync Translator - Heroku Deployment Script ===
echo.

REM Check if Heroku CLI is installed
heroku --version > NUL 2>&1
if %errorlevel% neq 0 (
    echo Heroku CLI is not installed or not in your PATH.
    echo Please install the Heroku CLI first: https://devcenter.heroku.com/articles/heroku-cli
    exit /b 1
)

echo Step 1: Logging into Heroku
echo Please login to your Heroku account when the browser opens...
heroku login

echo.
echo Step 2: Creating a new Heroku application
set /p app_name="Enter a name for your Heroku app (leave blank for random name): "

if "%app_name%"=="" (
    heroku create
) else (
    heroku create %app_name%
)

echo.
echo Step 3: Setting up Heroku buildpacks
heroku buildpacks:add heroku/python

echo.
echo Step 4: Configuring environment variables
heroku config:set PYTHON_VERSION=3.10.11
heroku config:set WEB_CONCURRENCY=1
heroku config:set MALLOC_TRIM_THRESHOLD_=65536

echo.
echo Step 5: Deploying to Heroku
echo Adding files to Git...
git add .
git commit -m "Prepare for Heroku deployment"

echo Pushing to Heroku...
git push heroku main

echo.
echo Step 6: Ensuring a web dyno is running
heroku ps:scale web=1

echo.
echo Step 7: Opening the application in your browser
heroku open

echo.
echo === Deployment Complete ===
echo Your LinguaSync Translator is now available on Heroku!
echo.
echo To check your application logs, run:
echo   heroku logs --tail
echo.
echo To make changes to your application:
echo 1. Edit your files locally
echo 2. Commit changes with Git
echo 3. Push to Heroku with: git push heroku main
echo.