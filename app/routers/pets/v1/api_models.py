"""Defines request and response data models"""
from pydantic import Field

from app.core.base_model import BaseModel


class PetResponseModel(BaseModel):
    """Pet API Response Model"""

    uuid: str = Field(
        ...,
        description="Unique identifier",
        example="f6c487f3-35e4-4fc4-9ffc-ce402c2df484",
    )
    name: str = Field(..., description="Pet name", example="Fluffy")
