from core.utils.custom_json_decode import to_json_converter
class CompanyModel:
    def __init__(self, name, catch_phrase, bs):
        self.name = name
        self.catch_phrase = catch_phrase
        self.bs = bs

    def to_json(self):
        return to_json_converter(self)


    @classmethod
    def from_json(cls, data:dict):
        data["catch_phrase"] = data["catchPhrase"]
        del data["catchPhrase"]
        cls = CompanyModel(**data)
        return cls
