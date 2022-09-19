import requests
from core.models.user import UserModel
from fastapi.exceptions import HTTPException
from starlette.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT
)
from core.settings import (
    BASE_URL
)

def get_all_users():
    response = requests.get(BASE_URL)
    if response.status_code != HTTP_200_OK:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
        )
    users_response = response.json()
    users = [UserModel.from_json(el) for el in users_response]
    return users

def get_users(name:str = None,):
    users = get_all_users()
    if not name:
        return users
    return list(filter(lambda usr: name in usr.name, users))

def get_users_details():
    users = get_all_users()
    return users

def get_users_websites():
    users = get_all_users()
    return users