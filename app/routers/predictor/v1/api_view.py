"""Defines API endpoints. Uses `controller.py` to handle the actual logic"""
from datetime import date, datetime, timedelta, timezone
from typing import List, Optional

import structlog
from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from fastapi.params import Query

from app.routers.predictor.v1.api_models import PredictorGroups, PredictorsResponseModel
from app.routers.predictor.v1.controller import PredictorController

router = APIRouter()

controller = PredictorController()

logger = structlog.get_logger(__name__)

today = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=timezone.utc)


@router.get("/", response_model=PredictorsResponseModel)
async def get_predictors(
    start: datetime = Query(  # noqa: B008
        ...,
        description="Start datetime (UTC ISO 8601)",
        example=(today - timedelta(days=30)).isoformat(),
    ),
    end: datetime = Query(  # noqa: B008
        ...,
        description="End datetime (UTC ISO 8601)",
        example=(today + timedelta(days=2)).isoformat(),
    ),
    lat: Optional[float] = Query(  # noqa: B008
        None,
        description="Lattitude of the location of interest (required for weather data).",
        example=51.984,
    ),
    lon: Optional[float] = Query(  # noqa: B008
        None,
        description="Longitude of the location of interest (required for weather data).",
        example=5.894,
    ),
    predictor_groups: Optional[List[PredictorGroups]] = Query(  # noqa: B008
        None, description="The requested predictor groups"
    ),
    resolution: str = Query(  # noqa: B008
        "15min",
        description="The requested resolution (pandas format) of the predictors",
    ),
) -> PredictorsResponseModel:
    """Get predictors a forecast.

    Returns:
        PredictorsResponseModel.
    """
    # perform extra query validation
    if [lat, lon].count(None) != 0 and PredictorGroups.WEATHER_DATA in predictor_groups:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Need to supply lat, lon when requesting weather predictors",
        )
    return controller.get_predictors(start, end, lat, lon, resolution, predictor_groups)
