from numpy import array_split
from connection import Connection
from dictionary_interface import OnlineDictionary
from os import environ

DICTIONARY_COLLECTION = environ['DICTIONARY_COLLECTION']

class DictionarySeeder:
    __BATCH_SIZE = 25  # arbitrary constant

    def __init__(self, dictionary: OnlineDictionary, connection: Connection):
        self.__dictionary: OnlineDictionary = dictionary
        self.__connection: Connection = connection

    def seed(self, words: set[str]):
        batches = array_split(list(words), DictionarySeeder.__BATCH_SIZE)
        for batch in batches:
            try:
                filtered_words = [ word for word in batch if word ]
                definitions: dict[str, dict[str, list[str]]] = self.__dictionary.get_words_definitions(filtered_words)
                filtered_definitions = { key: value for key, value in definitions.items() if key and value }
                if not filtered_definitions:
                    continue
                self.__connection.set_definitions(filtered_definitions)
            except Exception as e:
                print(e, flush=True)