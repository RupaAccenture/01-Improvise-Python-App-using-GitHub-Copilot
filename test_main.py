from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_token():
    response = client.post("/generate-token/", json={"text": "hello world"})
    assert response.status_code == 200
    assert "checksum" in response.json()
    assert response.json()["checksum"] == "a948904f2f0f479b8f8197694b30184b0d2e42c6faff7b3c5d5c6e6ff255b4c6"
