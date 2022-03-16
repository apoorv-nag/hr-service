import os

from dotenv import load_dotenv
from pymongo import MongoClient

# load config file
load_dotenv()
MONGODB_URL = os.getenv('MONGO_URI')

# connect to mongodb
mongo_manager = MongoClient(MONGODB_URL)
