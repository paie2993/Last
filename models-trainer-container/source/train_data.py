import nltk
from environment import INVALID_HYPHENATIONS_COLLECTION, VALID_HYPHENATIONS_COLLECTION
from random import shuffle

from mapper_to_universal_tagset import map_brown_to_universal

TAGGER_TRAIN_DATA_PERCENT = 0.05
VALID_HYPHENATIONS_LIMIT = 10
INVALID_HYPHENATIONS_LIMIT = 10


def get_tagger_train_data():
    brown_tagged_train_data = nltk.corpus.brown.tagged_sents(tagset="universal")
    sents_number = len(brown_tagged_train_data)
    train_data_end_index = int(sents_number * TAGGER_TRAIN_DATA_PERCENT)
    brown_train_data = brown_tagged_train_data[:train_data_end_index]
    return [map_brown_to_universal(sent) for sent in brown_train_data]


def __get_valid_hyphenations(connection):
    return connection.smembers(VALID_HYPHENATIONS_COLLECTION)


def __get_invalid_hyphenations(connection):
    return connection.smembers(INVALID_HYPHENATIONS_COLLECTION)


def __label_valid_hyphenations(valid_hyphenations):
    valid = list(valid_hyphenations)
    shuffle(valid)
    valid = valid[:VALID_HYPHENATIONS_LIMIT]
    return list(map(lambda h: (h, True), valid))


def __label_invalid_hyphenations(invalid_hyphenations):
    invalid = list(invalid_hyphenations)
    shuffle(invalid)
    invalid = invalid[:INVALID_HYPHENATIONS_LIMIT]
    return list(map(lambda h: (h, False), invalid))


def get_hyphenated_classifier_train_data(connection):
    valid = __get_valid_hyphenations(connection)
    invalid = __get_invalid_hyphenations(connection)
    return __label_valid_hyphenations(valid) + __label_invalid_hyphenations(invalid)
