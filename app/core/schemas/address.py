from pydantic import BaseModel


class AddressSchema(BaseModel):
    street:str
    suite:str
    city:str
    zipcode:str
    lat:str
    lng:str
