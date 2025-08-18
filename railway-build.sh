#!/bin/bash

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setting up TranslateNow..."
# Don't download models during build
export SKIP_MODEL_DOWNLOAD=true

echo "Build complete!"