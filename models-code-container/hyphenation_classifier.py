import nltk
from extractor import HyphenedFeatureExtractor


class HyphenedWordClassifier:
    def __init__(self, feature_extractor: HyphenedFeatureExtractor):
        self.__feature_extractor = feature_extractor
        self.__classifier: nltk.NaiveBayesClassifier

    def train(self, labeled_train_data):
        featured_train_data = [
            (self.__get_features(hyphenation), label)
            for hyphenation, label in labeled_train_data
        ]
        self.__classifier = nltk.NaiveBayesClassifier.train(featured_train_data)

    def is_valid_hyphanation(self, hyphenation: str) -> bool:
        features = self.__feature_extractor.get_features(hyphenation)
        return self.__classifier.classify(features)

    def __get_features(self, hyphenation):
        return self.__feature_extractor.get_features(hyphenation)
