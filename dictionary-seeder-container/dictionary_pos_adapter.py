from importlib.machinery import SourceFileLoader
from dictionary_pos_mapping import DICTIONARY_MAPPING, OTHER


# maps from dictionary.com parts-of-speech to universal parts-of-speech
class DictionaryPosAdapter:
    def dictionary_pos_to_universal_pos(self, dpos: str) -> str:
        dpos = dpos.strip(" .,")
        dpos = dpos.lower()
        if dpos not in DICTIONARY_MAPPING:
            return OTHER
        return DICTIONARY_MAPPING[dpos]
