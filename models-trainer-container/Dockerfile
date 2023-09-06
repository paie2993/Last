FROM python:latest

RUN ["pip3", "install", "nltk"]
RUN ["pip3", "install", "redis"]

COPY ["./nltk_initialize.py", "/"]

RUN ["python3", "-m", "nltk_initialize"]

RUN [ "rm", "nltk_initialize.py" ]

ENV DATABASE_HOST="localhost" \
    DATABASE_PORT=6379 \
    DATABASE_DB=0 \
    VALID_HYPHENATIONS_COLLECTION="hyphened" \
    INVALID_HYPHENATIONS_COLLECTION="invalid_hyphened" \
    TAGGER_NAME="tagger" \
    HYPHENATED_CLASSIFIER_NAME="hyphened_classifier"

COPY [ "./source/", "/app/" ]

WORKDIR /app/

ENTRYPOINT [ "python3", "-m", "entrypoint" ]
