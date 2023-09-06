import nltk


class Tagger:
    def __init__(self):
        self.__tagger = nltk.PerceptronTagger()

    def train(self, train_data):
        self.__tagger.train(train_data)

    def tag_word(self, word: str):
        return self.__tagger.tag([word])[0]

    def tag_sent(self, words: list[str]) -> list[tuple[str, str]]:
        return self.__tagger.tag(words)

    def tag_sents(self, sents: list[list[str]]):
        return [self.tag_sent(sent) for sent in sents]
