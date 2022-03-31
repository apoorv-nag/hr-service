from app.resources.v1.project import ProjectAPI


def initialize_routes(api):
    initialize_v1_routes(api)


def initialize_v1_routes(api):
    api.add_resource(ProjectAPI, '/api/v1/projects', '/api/v1/projects/<string:id>')
