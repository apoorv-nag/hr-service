from app.models.v1.project import ProjectModel
from app.repositories.base import BaseRepository


class ProjectRepository(BaseRepository):

    def __init__(self):
        super().__init__(ProjectModel())

    def get_all(self):
        return super().get_all()
