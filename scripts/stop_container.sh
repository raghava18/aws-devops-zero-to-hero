#!/bin/bash

echo "Stopping existing container..."

sudo docker stop flask-container || true

sudo docker rm flask-container || true

echo "Container stopped and removed"
