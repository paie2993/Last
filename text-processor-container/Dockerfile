FROM python:latest

RUN ["pip3", "install", "redis"]
RUN ["pip3", "install", "nltk"]
RUN ["pip3", "install", "flask"]
RUN ["pip3", "install", "flask_cors"]
RUN ["pip3", "install", "pymple"]

COPY [ "./nltk_initialize.py", "/" ]

RUN [ "python3", "-m", "nltk_initialize" ]

RUN [ "rm", "/nltk_initialize.py" ]

COPY ["./source", "/app/"]

EXPOSE 5000

ENV DATABASE_HOST="localhost" \                                                                 
    DATABASE_PORT=6379 \                                                               
    DATABASE_DB=0 \                                                                  
    VOCABULARY_COLLECTION="vocabulary" \
    DICTIONARY_COLLECTION="dictionary" \
    USER_VOCABULARY_COLLECTION="user_vocabulary" \
    USER_DICTIONARY_COLLECTION="user_dictionary" \
    TAGGER_NAME="tagger" \
    HYPHENATED_CLASSIFIER="hyphened_classifier" \
    RAW_COLLECTION=raw \
	TOKENIZED_COLLECTION=tokenized	\
    FLASK_APP=/app/entrypoint.py

ENTRYPOINT ["flask", "run"]

CMD ["--host", "0.0.0.0"]

