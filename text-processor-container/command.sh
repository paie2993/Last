#!/bin/bash

docker stop text-processor-container 2>/dev/null ; \
docker rm -v text-processor-container 2>/dev/null ; \
docker build -t text-processor-container:latest . && \
docker run --net container:internal-network-container \
	--volumes-from models-code-container \
	--volumes-from universal-parts-of-speech-container \
	--name text-processor-container \
	text-processor-container
