import json
import requests_mock
from app.core.crud.user import (
    get_all_users
)

from app.core.settings import (
    BASE_URL
)
import os

def test_get_all_users(requests_mock):
    with open(os.curdir + "/app/tests/mock_files/data_mocked.html", encoding="utf-8") as file:
        resp_data = json.loads(file.read())
    requests_mock.get(BASE_URL, json=lambda _,__: resp_data)
    user = next(iter(get_all_users()))
    assert user.id == 1
    assert user.name == "Leanne Graham"
    assert user.username == "Bret"
    assert user.email == "Sincere@april.biz"
    assert user.address.street == "Kulas Light"
    assert user.company.catch_phrase == "Multi-layered client-server neural-net"
