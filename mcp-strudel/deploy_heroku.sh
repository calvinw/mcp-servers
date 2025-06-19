#!/bin/bash
# Deploy to Heroku using Container Registry
# Usage: ./deploy_heroku.sh [app-name]
# If no app-name provided, will use current directory name
# Example: ./deploy_heroku.sh mcp-dolt-database
#

# If app name not provided, use current directory name
if [ -z "$1" ]; then
    APP_NAME=$(basename "$PWD")
    echo "🔍 No app name provided, using directory name: $APP_NAME"
else
    APP_NAME="$1"
fi

set -e

echo "🚀 Stack set container for $APP_NAME"
heroku stack:set container -a "$APP_NAME" 

echo "🚀 Deploying $APP_NAME to Heroku..."
echo "App name: $APP_NAME"

# Check if Dockerfile exists
if [ ! -f "Dockerfile" ]; then
    echo "❌ Error: Dockerfile not found in current directory"
    exit 1
fi

# Login to Heroku Container Registry
echo "🔐 Logging into Heroku Container Registry..."
heroku container:login

# Build and push the Docker image
echo "🔨 Building and pushing Docker image..."
heroku container:push web -a "$APP_NAME"

# Release the container
echo "🚢 Releasing the container..."
heroku container:release web -a "$APP_NAME"

echo "✅ $APP_NAME deployed successfully!"

# Get the actual app URL from Heroku
APP_URL=$(heroku info -a "$APP_NAME" | grep "Web URL:" | awk '{print $3}')
if [ -n "$APP_URL" ]; then
    echo "🌐 App URL: $APP_URL"
else
    echo "🌐 Could not retrieve URL from Heroku"
fi

if [ -n "$APP_URL" ]; then
    # Remove trailing slash if present, then add /sse
    SSE_URL="${APP_URL%/}/sse"
    echo "Please open manually: $SSE_URL"
fi
