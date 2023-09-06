FROM python:latest

RUN ["pip3", "install", "redis"]

ENV DATABASE_HOST=localhost \
	DATABASE_PORT=6379 \
	DATABASE_DB=0 \
	RAW_COLLECTION=raw \
	TOKENIZED_COLLECTION=tokenized	

COPY ["./entrypoint.py", "/app/"]

WORKDIR /app/

ENTRYPOINT ["python3", "-m", "entrypoint"]
