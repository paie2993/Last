from importlib.machinery import SourceFileLoader

universal = SourceFileLoader(
    "universal_parts_of_speech", "/universal/universal_parts_of_speech.py"
).load_module()

DICTIONARY_MAPPING = {
    "noun": universal.NOUN,
    "pl n": universal.NOUN,
    "verb": universal.VERB,
    "verb phrases": universal.VERB,
    "auxiliary verb": universal.VERB,
    "verb (used with object)": universal.VERB,
    "verb (used without object)": universal.VERB,
    "adverb": universal.ADVERB,
    "adjective": universal.ADJECTIVE,
    "conjunction": universal.CONJUNCTION,
    "pronoun": universal.PRONOUN,
    "interjection": universal.OTHER,
}

OTHER = universal.OTHER
