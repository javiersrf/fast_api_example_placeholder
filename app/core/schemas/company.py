from pydantic import BaseModel


class CompanySchema(BaseModel):
    name:str
    class Config:
        orm_mode = True