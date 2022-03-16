from mongoengine import Document

from app.models.base import Base


class Project(Document):
    _id = Base.String
    pass