
from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from core.settings import (
    SECRET_KEY_CLIENTE,
    ALGORITHM,
    DATETIME_FORMAT
)

 
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")  

def decode_token(token:str):
    splited_token = token.split(" ")
    new_token = "".join(el for el in splited_token if "Bearer" not in el)
    data = jwt.decode(new_token, SECRET_KEY_CLIENTE, ALGORITHM)
    data["expired_date"] = datetime.strptime(data["expired_date"], DATETIME_FORMAT)
    return data

def create_token(data:dict):
    to_enconde = data.copy()
    to_enconde["expired_date"] = (datetime.now() + timedelta(days=100)).strftime(DATETIME_FORMAT)
    token = jwt.encode(to_enconde,SECRET_KEY_CLIENTE, ALGORITHM)
    return token
