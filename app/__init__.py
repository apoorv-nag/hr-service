import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

db = None


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'app.sqlite')
    )

    app.config["MONGO_URI"] = os.getenv('MONGO_URI')
    mongodb_client = PyMongo(app)
    global db
    db = mongodb_client.db

    app.config.update(TESTING=True, SECRET_KEY=os.getenv('SECRET_KEY'))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    api = Api(app)

    from app.api.v1.project import Project
    api.add_resource(Project, '/api/v1/projects/<string:id>')

    return app
