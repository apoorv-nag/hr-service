from app.models.base import Base


class ProjectModel(Base):
    def __init__(self):
        super().__init__()

    def get_all(self):
        print(self.instance)
        return self.instance.projects.find()
