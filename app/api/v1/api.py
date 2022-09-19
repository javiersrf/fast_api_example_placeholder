from fastapi import APIRouter
from api.v1.endpoints import (
    user,
    index
)

router = APIRouter()
router.include_router(index.router)
router.include_router(user.router)