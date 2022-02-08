"""Classes that implement business logic / use cases.

Classes:
    PirateController: implements pirate functionality
"""
from typing import List, Optional

from app.routers.pirates.v1.repository import Pirate, PirateRepository


class PirateController(object):
    """Pirate controller.

    Provides the linking layer between the view (REST API interface) and repository (storage).
    """

    def __init__(self):
        self.repository = PirateRepository()

    def get_pirates(self) -> List[Pirate]:
        """Retrieve a horde of pirates."""
        # Note that because the API model has `orm_mode == True`,
        # we don't need to explicitly convert from `Pirate` to `PirateResponseModel`.
        return self.repository.get_pirates()

    def get_pirate(self, uuid: str) -> Optional[Pirate]:
        """Retrieves a single pirate from the repository.

        Args:
            uuid (str): Identifier of the requested pirate.

        Returns:
            Pirate object if found, None otherwise
        """
        return self.repository.get_pirate(uuid)
