from data_structures.aggregators.aggregator import Aggregator
from container.container import Tagger
from database.database import Database
from processor.lemmatizer import Lemmatizer
from processor.sentence_segmenter import SentenceSegmenter
from processor.tokenizer import Tokenizer


class Controller:
    def __init__(
        self,
        database: Database,
        segmenter: SentenceSegmenter,
        tokenizer: Tokenizer,
        tagger: Tagger,
        aggregator: Aggregator,
        lemmatizer: Lemmatizer,
    ):
        self.__database = database
        self.__segmenter = segmenter
        self.__tokenizer = tokenizer
        self.__tagger = tagger
        self.__aggregator = aggregator
        self.__lemmatizer = lemmatizer

    # get
    def get_texts_titles(self):
        return self.__get_texts_titles()

    def get_raw_text_by_title(self, title):
        return self.__get_raw_text_by_title(title)

    def get_dictionary(self):
        return self.__database.get_dictionary()

    def get_user_dictionary(
        self,
    ) -> dict[str, dict[str, str]]:
        return self.__database.get_user_dictionary()

    # add definition
    def add_word_to_user_dictionary(self, word):
        self.__database.add_word_to_user_dictionary(word)

    # remove definitions
    def remove_definitions_from_user_dictionary(self, words: list[str]):
        self.__database.remove_definitions_from_user_dictionary(words)

    # nlp workflows
    def from_raw_to_sentenced(self, text: str):
        return self.__get_sentences(text)

    def from_raw_to_tokenized_sentences(self, text: str):
        sents = self.from_raw_to_sentenced(text)
        return self.__get_tokenized_sentences(sents)

    def from_raw_to_tagged_sentences(self, text: str):
        tokenized_sents = self.from_raw_to_tokenized_sentences(text)
        return self.__get_tagged_sentences(tokenized_sents)

    def from_raw_to_universal_tagged_sentences(self, text: str):
        return self.from_raw_to_tagged_sentences(text)

    def from_raw_to_lemmas(self, text: str):
        universal_tagged_sentences = self.from_raw_to_universal_tagged_sentences(text)
        return self.__get_lemmas(universal_tagged_sentences)

    def from_raw_to_definitions(self, text: str):
        lemmas = self.from_raw_to_lemmas(text)

        user_dictionary = self.get_user_dictionary()

        filtered_lemmas = {
            lemma: poses for lemma, poses in lemmas.items() if lemma not in user_dictionary
        }

        dictionary = self.get_dictionary()
        definitions = self.__aggregator.intersect(dictionary, filtered_lemmas)

        return definitions

    def from_title_to_definitions(self, title: str):
        raw_text = self.__get_raw_text_by_title(title)
        return self.from_raw_to_definitions(raw_text)

    # nlp intermediary steps
    def __get_texts_titles(self):
        return self.__database.get_texts_titles()

    def __get_raw_text_by_title(self, title):
        return self.__database.get_raw_text_by_title(title)

    def __get_sentences(self, text: str) -> list[str]:
        return self.__segmenter.segment(text)

    def __get_tokenized_sentences(self, sents: list[str]) -> list[list[str]]:
        return [self.__tokenizer.tokenize(sent) for sent in sents]

    def __get_tagged_sentences(
        self,
        tokenized_sents: list[list[str]],
    ) -> list[list[tuple[str, str]]]:
        return self.__tagger.tag_sents(tokenized_sents)

    def __get_lemmas(self, tagged_sents: list[list[tuple[str, str]]]):
        flattened: list = self.__aggregator.flatten(tagged_sents)

        aggregated_by_word: dict[
            str, set[str]  # word, parts_of_speech
        ] = self.__aggregator.aggregate_by_second_value(flattened)

        return self.__lemmatizer.lemmatize_words(aggregated_by_word)
