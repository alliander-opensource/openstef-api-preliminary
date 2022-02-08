"""Classes responsible for the (indirect) retrieval of pets.

Classes:
    Pet: describes a pet object.
    PetRepository: retrieves pet objects
"""
from typing import List

from app.routers.pets.v1.client import PetClient


class Pet(object):
    """Pet data structure.

    Note that this class should be independent of the API and is therefore
    not the same as the API model which is defined in `app/routers/pets/v1/api_view.py`.
    """

    def __init__(self, uuid: str, name: str):
        """Creates a new instance of the pet class.

        Args:
            uuid (str): unique identifier
            name (str): pet name
        """
        self.uuid = uuid
        self.name = name

    def __str__(self) -> str:
        """Pretty prints a pet object instance.

        Returns:
            Formatted string representation of the pet class.
        """
        return f"<class='Pet', uuid='{self.uuid}', name='{self.name}'>"


class PetRepository(object):
    """Data structure which (indirectly) retrieves pets.

    Provides retrieval methods for pet objects.

    Uses `client.py` to handle the actual request to the external API or database.
    """

    def __init__(self):
        self.client = PetClient()

    def get_pets(self, limit: int = 10) -> List[Pet]:
        """Retrieves pet instances from the Swagger Petstore.

        Returns:
            List of all pet instances
        """
        pet_responses = self.client.get_pets()
        pets = [p for p in map(self.map_to_pet, pet_responses) if p is not None]
        return pets[:limit]

    def map_to_pet(self, pet_response):
        """Converts a Swagger pet store pet to a local pet instance.

        Args:
            pet_response (dict): Swagger pet store pet

        Returns:
            Pet instance if the input was valid, None otherwise
        """
        if "id" in pet_response and "name" in pet_response:
            return Pet(str(pet_response["id"]), pet_response["name"])
        else:
            return None
