FROM python

RUN ["pip3", "install", "redis"]

COPY ["./entrypoint.py", "/app/"]

WORKDIR /app/

ENV VOCABULARY=vocabulary \
	HYPHENED=hyphened \
	INVALID_HYPHENED=invalid_hyphened \
	STOPWORDS=stopwords \
	DATABASE_HOST=localhost \
	DATABASE_PORT=6379 \
	DATABASE_DB=0

ENTRYPOINT ["python3", "-m", "entrypoint"]
