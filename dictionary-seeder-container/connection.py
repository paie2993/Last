import json
from random import shuffle
from os import environ
from redis import Redis

HOST = environ["DATABASE_HOST"]
PORT = environ["DATABASE_PORT"]
DB = environ["DATABASE_DB"]

VOCABULARY_COLLECTION = environ["VOCABULARY_COLLECTION"]
DICTIONARY_COLLECTION = environ["DICTIONARY_COLLECTION"]
TOKENIZED_COLLECTION = environ["TOKENIZED_COLLECTION"]


class Connection:
    def __init__(self):
        self.__connection: Redis

    def open(self):
        self.__connection = Redis(
            host=HOST, port=PORT, db=DB, decode_responses=True, charset="utf-8"
        )

    def close(self):
        self.__connection.close()

    def texts(self):
        return list(self.__connection.hkeys(TOKENIZED_COLLECTION))
        

    def vocabulary(self):
       return set(self.__connection.smembers(VOCABULARY_COLLECTION))
    
    def random_vocabulary_words(self, count):
        vocabulary = list(self.__connection.smembers(VOCABULARY_COLLECTION))
        shuffle(vocabulary)
        return set(vocabulary[:count])
    
    def text_vocabulary(self, title):
        json_tokens = self.__connection.hget(TOKENIZED_COLLECTION, title)
        tokens = json.loads(json_tokens)
        return set(tokens)

    def set_definitions(self, word_definitions):
        mapping = { word: json.dumps(pos_definitions) for word, pos_definitions in word_definitions.items() }
        self.__connection.hset(DICTIONARY_COLLECTION, mapping=mapping)
