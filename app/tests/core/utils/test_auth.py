from datetime import datetime, timedelta
from app.core.utils.auth import (
    decode_token,
    create_token
)

def test_createand_read_token():
    teste_token = create_token({
        "user":"test",
        })
    data_decoded = decode_token(teste_token)
    assert teste_token.count(".") == 2
    assert "expired_date" in data_decoded
    token_date = data_decoded.get("expired_date")
    assert type(token_date) == datetime
    assert data_decoded.get("user") == "test"
