#!/bin/bash

# Deployment verification script for TranslateNow
echo "=== TranslateNow Deployment Verification ==="
echo

# Check Python version
echo "1. Checking Python version..."
python3 --version

# Check if all required files exist
echo
echo "2. Checking deployment files..."
files=(
    "render.yaml"
    "Procfile"
    "requirements.txt"
    "build.sh"
    "runtime.txt"
    "main.py"
    "translator/app.py"
    "translator/translator.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✓ $file exists"
    else
        echo "✗ $file missing"
    fi
done

# Check if build script is executable
echo
echo "3. Checking build script permissions..."
if [ -x "build.sh" ]; then
    echo "✓ build.sh is executable"
else
    echo "✗ build.sh is not executable"
    echo "  Run: chmod +x build.sh"
fi

# Test if dependencies can be installed
echo
echo "4. Testing dependency installation..."
pip install -r requirements.txt --dry-run > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ All dependencies are available"
else
    echo "✗ Some dependencies may have issues"
fi

# Test if the app can import successfully
echo
echo "5. Testing application import..."
python3 -c "from translator.app import app; print('✓ Application imports successfully')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "✗ Application import failed"
fi

echo
echo "=== Deployment file verification complete ==="
echo
echo "Ready for deployment to:"
echo "  • Render (using render.yaml)"
echo "  • Heroku (using Procfile + runtime.txt)"
echo "  • Railway (using Procfile + build process)"