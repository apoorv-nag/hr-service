import json

from bson import json_util, ObjectId
from flask_restful import reqparse

from app.lib.rabbitmq.publisher import Publisher
from app.resources.base import Base


class ProjectAPI(Base):

    def get(self, identifier=None):
        if identifier is not None:
            return self.show(identifier)

        from app.app import mongodb
        projects = mongodb.projects.find()
        Publisher.add('Wow! Ewww')
        return json.loads(json_util.dumps(projects))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('projectName', type=str)
        parser.add_argument('updateDate', type=str)

        args = parser.parse_args()
        projectName = str(args['projectName'])
        updateDate = str(args['updateDate'])

        from app.app import mongodb
        result = mongodb.projects.insert_one({
            "projectName": projectName,
            "updateDate": updateDate
        })
        project = mongodb.projects.find_one({"_id": result.inserted_id})

        return json.loads(json_util.dumps(project))

    def show(self, identifier):
        from app.app import mongodb
        projects = mongodb.projects.find({"_id": ObjectId(identifier)})
        return json.loads(json_util.dumps(projects))
