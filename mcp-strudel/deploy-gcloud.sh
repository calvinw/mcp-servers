#!/bin/bash

# Deploy MCP Strudel server to Google Cloud Run

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

PROJECT_ID="mcp-servers-20250621"
REGION="us-central1"
SERVICE_NAME="mcp-strudel"

echo -e "${BLUE}Deploying MCP Strudel Server to Google Cloud Run...${NC}"

# Clean up .venv directory to reduce build size
echo -e "${YELLOW}Cleaning up .venv directory...${NC}"
rm -rf .venv

# Clean up working directories to reduce build size
echo -e "${YELLOW}Cleaning up working directories...${NC}"
rm -rf mcp-strudel.working mcp-strudel.remote.working temp-strudel

# Set project
echo -e "${YELLOW}Setting project to ${PROJECT_ID}...${NC}"
gcloud config set project $PROJECT_ID

# Build and deploy using Cloud Build
echo -e "${YELLOW}Building and deploying with Cloud Build...${NC}"
gcloud builds submit --config cloudbuild.yaml

# Allow unauthenticated access
echo -e "${YELLOW}Setting up public access...${NC}"
gcloud run services add-iam-policy-binding $SERVICE_NAME \
    --region=$REGION \
    --member="allUsers" \
    --role="roles/run.invoker"

# Get the service URL
SERVICE_URL=$(gcloud run services describe $SERVICE_NAME --region=$REGION --format="value(status.url)")

echo -e "${GREEN}Deployment completed successfully!${NC}"
echo -e "${GREEN}MCP Strudel Server URL: ${SERVICE_URL}${NC}"
echo -e "${GREEN}SSE Endpoint: ${SERVICE_URL}/sse${NC}"
echo -e "${GREEN}Web Interface: ${SERVICE_URL}${NC}"
echo -e "${BLUE}Ready to make music patterns with Strudel!${NC}"