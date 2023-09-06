from importlib.machinery import SourceFileLoader

universal = SourceFileLoader(
    "universal_parts_of_speech", "/universal/universal_parts_of_speech.py"
).load_module()

IGNORE = {"ignore"}
OTHER = universal.OTHER

UNIVERSAL_TO_WORDNET = {
    universal.ADJECTIVE: {"a", "s"},
    universal.ADPOSITION: IGNORE,
    universal.ADVERB: {"r"},
    universal.CONJUNCTION: IGNORE,
    universal.DETERMINER: IGNORE,
    universal.NOUN: {"n"},
    universal.NUMERAL: IGNORE,
    universal.PARTICLE: IGNORE,
    universal.PRONOUN: IGNORE,
    universal.VERB: {"v"},
    universal.PUNCTUATION: IGNORE,
    universal.OTHER: IGNORE,
}

WORDNET_TO_UNIVERSAL = {
    "a": universal.ADJECTIVE,
    "s": universal.ADJECTIVE,
    "r": universal.ADVERB,
    "n": universal.NOUN,
    "v": universal.VERB,
    "ignore": universal.OTHER,
}
