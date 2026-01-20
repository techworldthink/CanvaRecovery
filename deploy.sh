#!/bin/bash

# Build the Docker image
docker build -t canva-recovery .

# Run the container
mkdir -p data
docker run -d -p 8084:8084 -v $(pwd)/data:/app/data --name canva-recovery canva-recovery

echo "Deployment successful. Application running on port 8084."
