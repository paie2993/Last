from hyphenation_pattern import HYPHENATION_REGEX_PATTERN
from tagger import Tagger


class HyphenedFeatureExtractor:
    def __init__(self, pos_tagger: Tagger):
        self.__tagger = pos_tagger

    def get_features(self, hyphenation: str) -> dict:
        tagged_components = self.__tagged_components(hyphenation)
        components_number = len(tagged_components)
        features = dict()
        features["len"] = components_number
        features["matches-structure"] = self.__matches_hyphenation_pattern(hyphenation)
        for i in range(components_number):
            features[f"{i}-pos"] = tagged_components[i][1]
        return features

    def __matches_hyphenation_pattern(self, hyphenation: str) -> bool:
        return bool(HYPHENATION_REGEX_PATTERN.fullmatch(hyphenation))

    def __tagged_components(self, hyphenation: str) -> list[tuple[str, str]]:
        components = self.__components(hyphenation)
        return self.__tag_components(components)

    def __components(self, hyphenation: str) -> list[str]:
        return hyphenation.split("-")

    def __tag_components(self, components: list[str]) -> list[tuple[str, str]]:
        return self.__tagger.tag_sent(components)
