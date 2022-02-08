
from fastapi import status

# TODO implement api test
# def test__get_pirates__returns_list_of_pirates(api_client):
#     response = api_client.get("/api/v1/pirates")

#     assert response.ok
#     pirates = response.json()
#     assert len(pirates) == 2


# def test__get_pirate__returns_pirate(api_client):
#     response = api_client.get("/api/v1/pirates/1")

#     assert response.ok
#     pirate = response.json()
#     assert "name" in pirate
#     assert pirate["name"] == "LeChuck"


# def test__get_pirate__invalid_id_raises_404(api_client):
#     response = api_client.get("/api/v1/pirates/42")

#     assert not response.ok
#     assert response.status_code == status.HTTP_404_NOT_FOUND
