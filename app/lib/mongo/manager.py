import os

from dotenv import load_dotenv
from pymongo import MongoClient

# load config file
load_dotenv()
MONGODB_URL = os.getenv('MONGO_URI')
MONGODB_PORT = int(os.getenv('MONGO_PORT'))

# connect to mongodb
mongo_manager = MongoClient(MONGODB_URL, port=MONGODB_PORT)
