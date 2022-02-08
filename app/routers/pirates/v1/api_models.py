from typing import Optional

from pydantic import Field

from app.core.base_model import BaseModel


class PirateResponseModel(BaseModel):
    """Pirate API Response Model"""

    uuid: str = Field(
        ..., description="", example="5a67891c-c076-4b61-94d1-21d2e4e04108"
    )
    name: str = Field(..., description="", example="Example Pirate")
    nickname: Optional[str] = Field(None, description="", example="Crazy Joe")
    quote: str = Field(..., description="", example="Arhr!! I'm a pirate!")
    wooden_leg: bool = Field(False, description="", example=False)
    hook_hand: bool = Field(False, description="", example=False)
