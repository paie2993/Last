from typing import Any
from flask import Blueprint
from flask import make_response

from container.container import container
from web.controller import Controller
from web.serializer import Serializer

__controller: Controller = container.resolve(Controller)
__serializer: Serializer = container.resolve(Serializer)


def __serialize(dictionary):
    return __serializer.serialize_dictionary(dictionary)


domain = Blueprint("domain", __name__)


# get dictionaries
@domain.route("/dictionary")
def dictionary():
    dictionary = __controller.get_dictionary()
    return __serialize(dictionary)


@domain.route("/user/dictionary")
def user_dictionary():
    user_dictionary = __controller.get_user_dictionary()
    return __serialize(user_dictionary)


# add word
@domain.route("/user/dictionary/add/<word>")
def user_dictionary_add_word(word: str):
    __controller.add_word_to_user_dictionary(word)
    return make_response()


# remove definitions
@domain.route("/user/dictionary/remove/<word>")
def user_dictionary_remove_word(word: str):
    print(f"Received request to remove: {word}", flush=True)
    __controller.remove_definitions_from_user_dictionary([word])
    return make_response()


# texts
@domain.route("/texts/titles")
def texts():
    return __controller.get_texts_titles()


@domain.route("/texts/content/<title>")
def text_content(title: str):
    return __controller.get_raw_text_by_title(title)


@domain.route("/texts/definitions/<title>")
def text_definitions_by_text_title(title: str):
    definitions = __controller.from_title_to_definitions(title)
    return __serialize(definitions)
