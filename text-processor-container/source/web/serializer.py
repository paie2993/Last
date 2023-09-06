from typing import Any

class Serializer:
    def serialize_dictionary(self, definitions: dict):
        json_array = []
        for word in definitions.keys():
            json = dict()
            json["name"] = word
            json["partsOfSpeech"]: list[dict] = []
            for pos, defs in definitions[word].items():
                pos_definitions_pair: dict[str, Any] = dict()
                pos_definitions_pair["tag"] = pos
                pos_definitions_pair["definitions"] = defs
                json["partsOfSpeech"].append(pos_definitions_pair)
            json_array.append(json)
        return json_array