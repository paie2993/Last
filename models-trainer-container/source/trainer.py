from random import shuffle
from importlib.machinery import SourceFileLoader

tagger_module = SourceFileLoader("tagger", "/models/tagger.py").load_module()

SourceFileLoader("hyphenation_pattern", "/models/hyphenation_pattern.py").load_module()

feature_extractor_module = SourceFileLoader(
    "extractor", "/models/extractor.py"
).load_module()

hyphenation_classifier = SourceFileLoader(
    "hyphenation_classifier", "/models/hyphenation_classifier.py"
).load_module()

Tagger = tagger_module.Tagger
HyphenedFeatureExtractor = feature_extractor_module.HyphenedFeatureExtractor
HyphenedWordClassifier = hyphenation_classifier.HyphenedWordClassifier


class Trainer:
    def __init__(self, tagger_train_data, labeled_hyphenations):
        self.__tagger_train_data = tagger_train_data
        self.__labeled_hyphenations = labeled_hyphenations

    def train_tagger(
        self,
    ):
        tagger = Tagger()
        tagger.train(self.__tagger_train_data)
        return tagger

    def train_hyphenation_classifier(self, tagger: Tagger):
        feature_extractor = HyphenedFeatureExtractor(tagger)
        hyphenation_classifier = HyphenedWordClassifier(feature_extractor)
        hyphenation_classifier.train(self.__labeled_hyphenations)
        return hyphenation_classifier
