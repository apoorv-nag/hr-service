import json

from bson import json_util
from app.api.base import Base

from app import db

class Project(Base):
    def get(self, id):
        projects = db.projects.find({"_id.$oid": id})
        return json.loads(json_util.dumps(projects))
