"""Classes responsible for the (indirect) retrieval of pirates.

Classes:
    Pirate: describes a priate object.
    PirateRepository: retrieves pirate objects
"""
import json
from copy import deepcopy
from pathlib import Path
from typing import List


class Pirate(object):
    """Pirate data structure.

    Note that this class should be independent of the API and is therefore
    not the same as the API model which is defined in `app/routers/pirates/v1/api_view.py`.
    """

    def __init__(
        self,
        id: str,
        name: str,
        nickname: str,
        quote: str,
        wooden_leg: bool,
        hook_hand: bool,
    ):
        self.uuid = str(id)
        self.name = name
        self.nickname = nickname
        self.quote = quote
        self.wooden_leg = wooden_leg
        self.hook_hand = hook_hand


class PirateRepository(object):
    """Pirate repositry based on a local file database.

    Note that for this simple example, the 'database' is
    loaded only once upon instantiation of the repository from a local file.
    Changes in the database that occur afterwards are not reflected.

    In your actual application, you will more likely connect to a database like HANA.
    """

    def __init__(self):
        pirates_path = Path("./data/pirates.json")
        pirates_json = json.loads(pirates_path.read_text())
        self.pirates = [Pirate(**pirate_data) for pirate_data in pirates_json]

    def get_pirates(self) -> List[Pirate]:
        return deepcopy(self.pirates)

    def get_pirate(self, uuid: str) -> Pirate:
        query_result = [pirate for pirate in self.pirates if pirate.uuid == uuid]
        if query_result:
            return deepcopy(query_result[0])
        return None
