from fastapi.testclient import TestClient
from ....main import app
import pytest
client = TestClient(app)

@pytest.mark.anyio
def test_read_main_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Api online"
