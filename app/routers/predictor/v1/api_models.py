from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic.fields import Field

from app.core.base_model import BaseModel


# FIXME we should use the models from a central source, this model is also defined in
# openstef-dbc but without the str super-class
# Need to be a sub-class from str and Enum for FastAPI to work properly
# see https://fastapi.tiangolo.com/tutorial/path-params/#predefined-values
class PredictorGroups(str, Enum):
    MARKET_DATA = "market_data"
    WEATHER_DATA = "weather_data"
    LOAD_PROFILES = "load_profiles"


#

# RESPONSE MODELS ######################################################################
class PredictorsResponseModel(BaseModel):
    index: List[datetime] = Field(
        ...,
        description="Datetime index of predictors",
        example=[
            "2021-04-30T14:00:00.000Z",
            "2021-04-30T14:15:00.000Z",
            "2021-04-30T14:30:00.000Z",
        ],
    )
    columns: List[str] = Field(
        ...,
        description="The names of the predictor columns",
        example=["temperature", "electricity_price"],
    )
    data: List[List[Union[float, int, str, None]]] = Field(
        ...,
        description="The data of the predictor columns",
        # TODO better example
        example=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    )
