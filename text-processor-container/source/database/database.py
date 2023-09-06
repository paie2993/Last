import json
import pickle
from redis import Redis

from environment.environment import (
    DATABASE_DB,
    DATABASE_HOST,
    DATABASE_PORT,
    DICTIONARY_COLLECTION,
    RAW_COLLECTION,
    USER_DICTIONARY_COLLECTION,
    TAGGER_NAME,
    HYPHENATED_CLASSIFIER_NAME,
)


class Database:
    def __init__(self):
        self.__decoding_connection: Redis
        self.__binary_connection: Redis

    def open(self):
        self.__decoding_connection = Redis(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            db=DATABASE_DB,
            charset="utf-8",
            decode_responses=True,
        )
        self.__binary_connection = Redis(
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            db=DATABASE_DB,
        )

    def close(self):
        self.__decoding_connection.close()
        self.__binary_connection.close()

    # get texts
    def get_texts_titles(self):
        return self.__decoding_connection.hkeys(RAW_COLLECTION)

    def get_raw_text_by_title(self, title):
        return self.__decoding_connection.hget(RAW_COLLECTION, title)

    # get collections
    def get_dictionary(self) -> dict[str, dict[str, list[str]]]:
        return self.__get_named_dictionary(DICTIONARY_COLLECTION)

    def get_user_dictionary(self):
        return self.__get_named_dictionary(USER_DICTIONARY_COLLECTION)

    def __get_named_dictionary(self, name):
        serialized_dictionary: dict[str, str] = self.__decoding_connection.hgetall(name)
        dictionary = {
            key: json.loads(value) for key, value in serialized_dictionary.items()
        }
        return dictionary

    # update
    def update_user_dictionary(self, dictionary):
        serialized_dict = {key: json.dumps(value) for key, value in dictionary.items()}
        self.__decoding_connection.hset(
            USER_DICTIONARY_COLLECTION, mapping=serialized_dict
        )

    # add
    def add_word_to_user_dictionary(self, word):
        serialized_definitions = self.__decoding_connection.hget(
            DICTIONARY_COLLECTION, word
        )
        self.__decoding_connection.hset(
            USER_DICTIONARY_COLLECTION, word, serialized_definitions
        )

    # remove definitions
    def remove_definitions_from_user_dictionary(self, words: list[str]):
        self.__decoding_connection.hdel(USER_DICTIONARY_COLLECTION, *words)

    # models
    def get_tagger(self):
        pickled_tagger = self.__binary_connection.get(TAGGER_NAME)
        return pickle.loads(pickled_tagger)

    def get_hyphenated_classifier(self):
        pickled_classifier = self.__binary_connection.get(HYPHENATED_CLASSIFIER_NAME)
        return pickle.loads(pickled_classifier)
