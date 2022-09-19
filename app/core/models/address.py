from core.utils.custom_json_decode import to_json_converter
class AddressModel:
    def __init__(self, street, suite, city, zipcode, geo:dict = {}):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.lat = geo.get("lat")
        self.lng = geo.get("lng")

    def to_json(self):
        return to_json_converter(self)

    @classmethod
    def from_json(cls, data:dict):
        cls = AddressModel(**data)
        return cls