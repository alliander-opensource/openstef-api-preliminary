"""Defines API endpoints. Uses `controller.py` to handle the actual logic"""
from typing import List

from fastapi import APIRouter

from app.routers.pets.v1.api_models import PetResponseModel
from app.routers.pets.v1.controller import PetController

router = APIRouter()

controller = PetController()


@router.get("/", response_model=List[PetResponseModel])
async def get_pets():
    """Retrieve a list of pet objects.

    Returns:
        List of all available pet objects.
    """
    return controller.get_pets()
