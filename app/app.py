import logging
import os

from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

from app.lib.rabbitmq.publisher import Publisher
from app.resources.routes import initialize_routes

mongodb = None

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

LOGGER = logging.getLogger()


def create_app(test_config=None):
    LOGGER.info('Starting app in %s environment', os.getenv('FLASK_ENV'))
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        DATABASE=os.path.join(app.instance_path, 'app.sqlite')
    )

    app.config["MONGO_URI"] = os.getenv('MONGO_URI')
    mongodb_client = PyMongo(app)

    global mongodb
    mongodb = mongodb_client.db

    app.config.update(TESTING=os.getenv('TESTING'), SECRET_KEY=os.getenv('SECRET_KEY'))

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

    initialize_routes(api)

    @app.route('/create-job/<cmd>')
    def add(cmd):
        return Publisher.add(cmd)

    @app.route('/')
    def index():
        return 'It works'

    return app
