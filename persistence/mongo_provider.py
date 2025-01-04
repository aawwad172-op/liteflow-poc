from bson import UuidRepresentation
from liteflow.providers.mongo import MongoPersistenceProvider
from pymongo import MongoClient


def get_persistence_provider():
    # MongoDB connection URI
    mongo_uri = "mongodb://127.0.0.1:27017/"
    db_name = "liteflow"

    # Return the MongoDB persistence provider
    return MongoPersistenceProvider(mongo_uri, db_name)
