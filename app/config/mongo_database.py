from pymongo import MongoClient
from app import app_consts

# Tworzymy klienta MongoDB
mongo_client = MongoClient(app_consts.MONGO_HOST, app_consts.MONGO_PORT)

# Wybieramy bazę
mongo_db = mongo_client[app_consts.MONGO_DB_NAME]

# Kolekcje
mongo_record_collection = mongo_db[app_consts.MONGO_COLLECTION_RECORD]
mongo_person_collection = mongo_db[app_consts.MONGO_COLLECTION_PERSON]
