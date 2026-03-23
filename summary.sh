#!/bin/bash

# Container name (must match docker run)
CONTAINER_NAME=employee_analytics_container

# Local results folder
HOST_RESULTS_DIR=./results

# Create results folder if it doesn't exist
mkdir -p $HOST_RESULTS_DIR

echo "Copying output files from container..."

# Copy files from container to host
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png $HOST_RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt $HOST_RESULTS_DIR/ 2>/dev/null

echo "Files copied to $HOST_RESULTS_DIR"

# Stop container
docker stop $CONTAINER_NAME

# Remove container
docker rm $CONTAINER_NAME

echo "Container stopped and removed successfully."