"""Classes that implement business logic / use cases regarding pets.

Classes:
    PetController: implements pet functionality
"""

from typing import List

from app.routers.pets.v1.api_models import PetResponseModel
from app.routers.pets.v1.repository import Pet, PetRepository


class PetController(object):
    """Pet controller.

    Provides the linking layer between the view (REST API interface) and repository (storage).
    """

    def __init__(self):
        self.repository = PetRepository()

    def get_pets(self) -> List[Pet]:
        """Retrieves all pets from the repository.

        Returns:
            List of pet objects
        """
        # Note that because the API model has `orm_mode == True`,
        # we don't need to explicitly convert from `Pet` to `PetResponseModel`.
        return self.repository.get_pets()
