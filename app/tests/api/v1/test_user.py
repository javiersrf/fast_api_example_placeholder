import pytest
from fastapi.testclient import TestClient
from app import main
from ...conftest import (
    auth_header
)


client = TestClient(main.app)

@pytest.mark.anyio
def test_read_root_without_auth():
    response = client.get("/user")
    assert response.status_code == 401


@pytest.mark.anyio
def test_read_root(auth_header):
    response = client.get("/user", headers=auth_header)
    assert response.status_code == 200
    body_response = response.json()
    assert type(body_response) == dict
    assert "users" in body_response
    assert len(body_response.get("users")) == 10

@pytest.mark.anyio
def test_read_users_websites(auth_header):
    response = client.get("/user/websites", headers=auth_header)
    assert response.status_code == 200
    body_response = response.json()
    assert type(body_response) == dict
    assert "websites" in body_response
    assert len(body_response.get("websites")) == 10


@pytest.mark.anyio
def test_read_item_detail(auth_header):
    response = client.get("/user/detail", headers=auth_header)
    assert response.status_code == 200
    body_response = response.json()
    assert type(body_response) == dict
    assert "users" in body_response
    assert len(body_response.get("users")) == 10
    assert "company" in next(iter(body_response.get("users")))
