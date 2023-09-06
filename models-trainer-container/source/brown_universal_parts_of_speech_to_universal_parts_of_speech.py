from importlib.machinery import SourceFileLoader

universal = SourceFileLoader(
    "universal_parts_of_speech", "/universal/universal_parts_of_speech.py"
).load_module()


BROWN_UNIVERSAL_TO_UNIVERSAL = {
    "NOUN": universal.NOUN,
    ".": universal.PUNCTUATION,
    "X": universal.OTHER,
    "ADV": universal.ADVERB,
    "VERB": universal.VERB,
    "ADP": universal.ADPOSITION,
    "NUM": universal.NUMERAL,
    "PRT": universal.PARTICLE,
    "ADJ": universal.ADJECTIVE,
    "DET": universal.DETERMINER,
    "PRON": universal.PRONOUN,
    "CONJ": universal.CONJUNCTION,
}
