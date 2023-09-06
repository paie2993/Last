import atexit

from flask import Flask, make_response
from pymple import Container
from time import time

from connection import Connection
from dictionary_interface import OnlineDictionary
from dictionary_pos_adapter import DictionaryPosAdapter
from dictionary_seeder import DictionarySeeder

container = Container()


def register_connection(c):
    connection = Connection()
    connection.open()
    return connection


def unregister_connection():
    connection = container.resolve(Connection)
    connection.close()


def register_dictionary_seeder(c):
    online_dictionary = container.resolve(OnlineDictionary)
    connection = container.resolve(Connection)
    return DictionarySeeder(online_dictionary, connection)


container.register(DictionaryPosAdapter, lambda c: DictionaryPosAdapter())
container.register(
    OnlineDictionary, lambda c: OnlineDictionary(c.resolve(DictionaryPosAdapter))
)
container.register(Connection, register_connection)
container.register(DictionarySeeder, register_dictionary_seeder)

app = Flask(__name__)


@app.route("/texts")
def texts():
    connection = container.resolve(Connection)
    return connection.texts()


@app.route("/seed/random/<int:number>")
def seed_random(number: int):
    start = time()
    connection = container.resolve(Connection)
    seeder = container.resolve(DictionarySeeder)
    words = connection.random_vocabulary_words(number)
    seeder.seed(words)
    end = time()
    return f"Done in {end - start}s\n"


@app.route("/seed/text/<string:title>")
def seed_with_text(title: str):
    start = time()
    connection: Connection = container.resolve(Connection)
    words = connection.text_vocabulary(title)
    seeder = container.resolve(DictionarySeeder)
    seeder.seed(words)
    end = time()
    return f"Done in {end - start}s\n"


atexit.register(unregister_connection)
