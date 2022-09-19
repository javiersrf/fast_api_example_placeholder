from fastapi import APIRouter
#APIRouter creates path operations for item module
router = APIRouter(
    tags=["Home"],
    responses={404: {"name": "Not found"}},
)

@router.get("/")
async def read_main_root():
    return "Api online"