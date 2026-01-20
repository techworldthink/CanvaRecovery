#!/bin/bash

# Stop the existing container
docker stop canva-recovery

# Remove the existing container
docker rm canva-recovery

# Rebuild the image
docker build -t canva-recovery .

# Run the new container
docker run -d -p 8084:8084 -v $(pwd)/data:/app/data --name canva-recovery canva-recovery
 
echo "Redeployment successful. Application updated and running on port 8084."
