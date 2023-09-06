FROM python:latest

RUN ["pip3", "install", "redis"]
RUN ["pip3", "install", "flask"]
RUN ["pip3", "install", "numpy"]
RUN ["pip3", "install", "bs4"]
RUN ["pip3", "install", "pymple"]

COPY [".", "/app/"]

WORKDIR /app/

ENV DATABASE_HOST=localhost \
    DATABASE_PORT=6379 \
    DATABASE_DB=0 \
    VOCABULARY_COLLECTION="vocabulary" \
    DICTIONARY_COLLECTION="dictionary" \
    TOKENIZED_COLLECTION="tokenized" \
    FLASK_APP="/app/entrypoint.py"

ENTRYPOINT ["flask", "run"]

CMD ["--host", "0.0.0.0"]
