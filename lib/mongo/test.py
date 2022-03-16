
# list all databases  in the cluster
from lib.mongo.manager import mongo_manager

for db_info in mongo_manager.list_database_names():
    print(db_info)
