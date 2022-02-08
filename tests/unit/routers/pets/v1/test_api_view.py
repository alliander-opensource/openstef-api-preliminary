import pytest
import responses
from fastapi import FastAPI
from starlette.testclient import TestClient

from app.routers.pets.v1.api_view import router


@pytest.fixture
def api_client():
    app = FastAPI()
    app.mount("/", router)

    return TestClient(app)


@responses.activate
def test__get_pets__returns_pets(api_client, petstore_json_response):
    responses.add(
        responses.GET,
        "https://petstore.swagger.io/v2/pet/findByStatus?status=available",
        json=petstore_json_response,
        status=200,
    )
    res = api_client.get("/")
    assert res.status_code == 200
    pets = res.json()
    assert len(pets) == 2
    assert "uuid" in pets[0]
    assert pets[0]["uuid"] == "9216678377732764866"
    assert "name" in pets[0]
    assert pets[0]["name"] == "Woef"
