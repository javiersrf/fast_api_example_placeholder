from fastapi import Query, Header
from fastapi.exceptions import HTTPException
from starlette.status import (
    HTTP_401_UNAUTHORIZED,

)
from core.utils.auth import decode_token
from datetime import datetime, timedelta
async def get_auth(authorization=Header(default=None)):
    not_authenticated_exception = HTTPException(
            HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    if authorization is None:
        raise not_authenticated_exception
    try:
        auth_data = decode_token(authorization)
    except Exception:
        raise not_authenticated_exception
    delta_time:timedelta = auth_data.get("expired_date") - datetime.now()
    if delta_time.days > 100:
        raise HTTPException(
            HTTP_401_UNAUTHORIZED,
            detail="Expired token"
        )
    return auth_data