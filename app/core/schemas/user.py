from typing import List
from pydantic import BaseModel
from core.schemas.company import CompanySchema


class UserSchema(BaseModel):
    id:int
    name:str

class UserDetailSchema(BaseModel):
    name:str
    email:str
    company:CompanySchema
    class Config:
        orm_mode = True

class WebsitesSchema(BaseModel):
    website:str

class UserListSchema(BaseModel):
    users:List[UserSchema]

class WebsitesListSchema(BaseModel):
    websites:List[WebsitesSchema]

class DetailListSchema(BaseModel):
    users:List[UserDetailSchema]