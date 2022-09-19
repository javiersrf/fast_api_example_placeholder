from core.utils.custom_json_decode import to_json_converter
from core.models import (
    company,
    address
)
class UserModel:
    def __init__(self, id, name, username, address, email, phone, website, company):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def to_json(self):
        return to_json_converter(self)


    @classmethod
    def from_json(cls, data:dict):
        if "company" in data:
            data["company"] = company.CompanyModel.from_json(data["company"])
        if "address" in data:
            data["address"] = address.AddressModel.from_json(data["address"])
        cls = UserModel(**data)
        return cls

