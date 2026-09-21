from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_deployment_validation():
    response = client.post(
        "/deployments",
        json={
            "service": "billing-api",
            "environment": "staging",
            "version": "1.4.2",
        },
    )
    assert response.status_code == 201
    assert response.json()["status"] == "validated"


def test_production_requires_version():
    response = client.post(
        "/deployments",
        json={
            "service": "billing-api",
            "environment": "prod",
            "version": "latest",
        },
    )
    assert response.status_code == 400
