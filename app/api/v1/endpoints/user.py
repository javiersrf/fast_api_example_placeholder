from fastapi import APIRouter
from fastapi import Depends
import core.crud.user as crud
from core.authentication import get_auth
from core.schemas import (
    user as schema
)
#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"name": "Not found"}},
)

@router.get("/", response_model=schema.UserListSchema)
async def read_root(name:str=None, auth=Depends(get_auth)):
    users = crud.get_users(name)
    return {
        "users":[el.to_json() for el in users]
    }

@router.get("/websites", response_model=schema.WebsitesListSchema)
async def read_users_websites():
    users = crud.get_users_websites()
    return {
        "websites":[el.to_json() for el in users]
    }

@router.get("/detail", response_model=schema.DetailListSchema)
async def read_item_detail(auth=Depends(get_auth)):
    users = crud.get_users_details()
    return {
        "users":[el.to_json() for el in users]
    }
