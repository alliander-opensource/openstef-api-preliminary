from typing import List

from fastapi import APIRouter, HTTPException, Path

from app.core.errors.additional_responses import ERROR_RESPONSE
from app.routers.pirates.v1.api_models import PirateResponseModel
from app.routers.pirates.v1.controller import PirateController

"""Handles REST API requests and responses.
"""

router = APIRouter()

controller = PirateController()


@router.get("/", response_model=List[PirateResponseModel])
async def get_pirates():
    """Retrieve a list of pirate objects.

    Returns:
        List of all available pirate objects.
    """
    return controller.get_pirates()


@router.get(
    "/{uuid}",
    response_model=PirateResponseModel,  # the response model for one pirate
    responses={404: ERROR_RESPONSE},  # the error model in case the pirate doesn't exist
)
async def get(uuid: str = Path(..., description="Pirate identifier", example="1")):
    """Retrieve a specific pirate.

    Args:
        uuid (str): identifier of the pirate object.

    Returns:
        pirate with uuid if existing

    Raises:
        404: pirate with uuid could not be found.
    """
    pirate = controller.get_pirate(uuid)
    if pirate is None:
        raise HTTPException(status_code=404, detail="Pirate not found")
    return pirate
