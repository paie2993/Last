from brown_universal_parts_of_speech_to_universal_parts_of_speech import (
    BROWN_UNIVERSAL_TO_UNIVERSAL,
)


def map_brown_to_universal(brown_tagged_words):
    return [(word, __map_tag_to_universal(tag)) for word, tag in brown_tagged_words]


def __map_tag_to_universal(brown_tag):
    if brown_tag in BROWN_UNIVERSAL_TO_UNIVERSAL:
        return BROWN_UNIVERSAL_TO_UNIVERSAL[brown_tag]
    return BROWN_UNIVERSAL_TO_UNIVERSAL["X"]
