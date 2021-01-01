import json

def parse_to_dict(json_data: str) -> dict:
    return json.loads(json_data)
def convert_dictionary_to_json(dictionary: dict) -> str:
    return json.dumps(dictionary)
