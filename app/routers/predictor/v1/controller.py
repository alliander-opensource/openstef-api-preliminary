import types
from datetime import datetime
from typing import List, Optional

import structlog
from openstef_dbc.database import DataBase
from pydantic.networks import stricturl

from app.core.settings import Settings
from app.models.v1.utils import predictors_df_to_predictors_model
from app.routers.predictor.v1.api_models import PredictorGroups, PredictorsResponseModel


# Convert pydantic settings to openstef-dbc config data structure
def convert_settings_to_openstef_dbc_config(settings):
    config = types.SimpleNamespace(
        # Influx API access is not required
        api=types.SimpleNamespace(
            username="",
            password="",
            admin_username="",
            admin_password="",
            url="",
        ),
        influxdb=types.SimpleNamespace(
            username=settings.influxdb_username,
            password=settings.influxdb_password.get_secret_value(),
            host=settings.influxdb_host,
            port=settings.influxdb_port,
        ),
        mysql=types.SimpleNamespace(
            username=settings.mysql_username,
            host=settings.mysql_host,
            port=settings.mysql_port,
            password=settings.mysql_password.get_secret_value(),
            database_name=settings.mysql_database,
        ),
        proxies=None,
    )
    return config


class PredictorController:
    def __init__(self):
        config = convert_settings_to_openstef_dbc_config(Settings)
        self.repository = DataBase(config)
        self.logger = structlog.get_logger(self.__class__.__name__)

    def get_predictors(
        self,
        start: datetime,
        end: datetime,
        lat: float,
        lon: float,
        resolution: str = "15min",
        predictor_groups: Optional[List[PredictorGroups]] = None,
    ) -> PredictorsResponseModel:
        self.logger.info("Get predictors from repository")
        predictors = self.repository.get_predictors(
            datetime_start=start,
            datetime_end=end,
            location=(lat, lon),
            forecast_resolution=resolution,
            predictor_groups=predictor_groups,
        )
        return predictors_df_to_predictors_model(predictors)
