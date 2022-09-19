from json import JSONDecoder

def to_json_converter(obj):
    return {key:parse_object(value) for key, value in obj.__dict__.items()}

def parse_object(obj):
    if hasattr(obj, "to_json"):
        return obj.to_json()
    return obj