#!/bin/bash

docker stop frontend-container 2>/dev/null ; \
docker rm frontend-container 2>/dev/null ; \
docker build -t frontend-container:latest . && \
docker run --rm -d --net container:internal-network-container --name frontend-container frontend-container
