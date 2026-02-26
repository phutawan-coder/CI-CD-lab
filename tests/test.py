from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test():
    res = client.get('/')
    assert res.status_code == 200
