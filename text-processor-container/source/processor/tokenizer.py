import re

from nltk.tokenize import RegexpTokenizer


class Tokenizer:
    _hyphenation_pattern = re.compile(r"(?:\'?(?:\w+\'?)+-\'?(?:\w+\'?)+)+")

    def __init__(self, expander, hyphenation_classifier):
        self.__tokenizer = RegexpTokenizer(
            r'(?:\'?(?:\w+\'?)+#\'?(?:\w+\'?)+)+|[][)(}{\'\-.,!?:;"*$&]+|\w+'
        )  # simple words | hyphened words | punctuation characters
        self.__expander = expander
        self.__hyphenation_classifier = hyphenation_classifier

    def tokenize(self, raw_text: str) -> list[str]:
        # remove newlines
        raw_text = self.remove_extra_space_characters(raw_text)

        # expand the contractions
        raw_text = self.expand_contractions(raw_text)

        # mark the hyphened words
        raw_text = self.mark_hyphened_words(raw_text)

        # lowercase
        raw_text = raw_text.lower()

        # tokenize the text by regex
        tokens: list[str] = self.__tokenizer.tokenize(raw_text)

        # unmark hyphened words
        tokens = list(map(self.unmark_hyphened_word, tokens))

        return tokens

    def remove_extra_space_characters(self, text):
        return re.sub(r"\s+", " ", text)

    def expand_contractions(self, text):
        return self.__expander.expand_contractions(text)

    def mark_hyphened_words(self, text):
        hyphenations = self.find_all_hyphenations_words(text)
        hyphened_words = [
            h
            for h in hyphenations
            if self.__hyphenation_classifier.is_valid_hyphanation(h)
        ]
        for h in hyphened_words:
            substitution = self.hyphened_word_substitution(h)
            text = re.sub(h, substitution, text)
        return text

    def find_all_hyphenations_words(self, text: str) -> list[str]:
        return self._hyphenation_pattern.findall(text)

    def hyphened_word_substitution(self, word):
        return re.sub(r"-", "#", word)

    def unmark_hyphened_word(self, word: str) -> str:
        return re.sub(r"#", "-", word)
