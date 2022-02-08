import pytest

from app.routers.pets.v1.repository import Pet


@pytest.fixture
def api_client():
    from starlette.testclient import TestClient

    from app.main import app

    return TestClient(app)


@pytest.fixture(scope="module")
def pirates():
    pirates_dict = [
        {
            "uuid": "1",
            "name": "LeChuck",
            "nickname": "Chuckie",
            "quote": "It's days like this that make ye glad to be dead",
            "wooden_leg": False,
            "hook_hand": False,
        },
        {
            "uuid": "2",
            "name": "Jack Sparrow",
            "nickname": "",
            "quote": "If you were waiting for the opportune moment, that was it",
            "wooden_leg": False,
            "hook_hand": False,
        },
    ]
    return pirates_dict


@pytest.fixture(scope="module")
def petstore_json_response():
    res = [
        {
            "id": 9216678377732764866,
            "category": {"id": 0, "name": "string"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
            "name": "Woef",
        },
        {
            "id": 9216678377732764872,
            "category": {"id": 0, "name": "string"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        },
        {
            "id": 9216678377732764873,
            "category": {"id": 0, "name": "string"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
            "name": "Kwispel",
        },
        {"id": 9216678377732766260, "photoUrls": [], "tags": [], "status": "available"},
        {
            "id": 9216678377732766350,
            "category": {"id": 0, "name": "string"},
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "available",
        },
    ]
    return res


@pytest.fixture(scope="module")
def pet():
    return Pet("123456", "Zoefer")
