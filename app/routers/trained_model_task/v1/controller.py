from app.database import db_model_as_dict
from app.models.v1.db_models import TrainModelTask
from app.routers.trained_model_task.v1.api_models import TrainModelTaskReponseModel
from app.routers.trained_model_task.v1.repository import TrainModelTaskRepository


class TrainModelTaskController:
    def __init__(self) -> None:
        self.repository = TrainModelTaskRepository()

    def create_train_model_task(self, train_task_id) -> TrainModelTask:
        return self.repository.create_train_model_task(train_task_id)

    def read_train_model_task(self, train_task_id: str) -> TrainModelTaskReponseModel:
        train_model_task = self.repository.read_train_model_task(train_task_id)
        if train_model_task is None:
            return
        return TrainModelTaskReponseModel(**db_model_as_dict(train_model_task))

    def update_train_model_task(self, train_task):
        return self.repository.update_train_model_task(train_task)
