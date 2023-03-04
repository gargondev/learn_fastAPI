from fastapi.testclient import TestClient
from ....main import app


client = TestClient(app)


def test_show_data_cars():
    response = client.get('/cars/')
    assert response.status_code == 200
