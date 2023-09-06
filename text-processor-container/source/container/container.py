import atexit

from pymple import Container

from data_structures.aggregators.aggregator import Aggregator
from database.database import Database
from container.libraries import HyphenedWordClassifier
from container.libraries import Tagger
from processor.expander import Expander
from processor.lemmatizer import Lemmatizer
from processor.sentence_segmenter import SentenceSegmenter
from processor.tokenizer import Tokenizer
from web.controller import Controller
from web.serializer import Serializer

container = Container()


def __register_database(container):
    database = Database()
    database.open()
    return database


def __unregister_database():
    database: Database = container.resolve(Database)
    database.close()


def __register_hyphenated_classifier(container: Container):
    database: Database = container.resolve(Database)
    return database.get_hyphenated_classifier()


def __register_tokenizer(container: Container):
    expander = container.resolve(Expander)
    hyphenated_classifier = container.resolve(HyphenedWordClassifier)
    return Tokenizer(expander, hyphenated_classifier)


def __register_tagger(container: Container):
    database: Database = container.resolve(Database)
    return database.get_tagger()


def __register_lemmatizer(container: Container):
    database: Database = container.resolve(Database)
    dictionary = database.get_dictionary()
    return Lemmatizer(dictionary)


def __register_controller(container: Container):
    database: Database = container.resolve(Database)
    segmenter: SentenceSegmenter = container.resolve(SentenceSegmenter)
    tokenizer: Tokenizer = container.resolve(Tokenizer)
    tagger: Tagger = container.resolve(Tagger)
    aggregator: Aggregator = container.resolve(Aggregator)
    lemmatizer: Lemmatizer = container.resolve(Lemmatizer)
    return Controller(database, segmenter, tokenizer, tagger, aggregator, lemmatizer)


container.register(Database, __register_database)
container.register(Aggregator, lambda c: Aggregator())
container.register(SentenceSegmenter, lambda c: SentenceSegmenter())
container.register(Expander, lambda c: Expander())
container.register(HyphenedWordClassifier, __register_hyphenated_classifier)
container.register(Tokenizer, __register_tokenizer)
container.register(Tagger, __register_tagger)
container.register(Lemmatizer, __register_lemmatizer)
container.register(Controller, __register_controller)
container.register(Serializer, lambda c: Serializer())

atexit.register(__unregister_database)
