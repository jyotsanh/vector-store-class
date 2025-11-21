from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
import os

DATABASE_HOST = os.getenv("DATABASE_HOST")


class MongoDatabaseConnector:
    _instance:MongoClient | None
    def __new__(cls, *args, **kwargs) -> MongoClient:
        if cls._instance is None:
            try:
                cls._instance = MongoClient(host=DATABASE_HOST)
            except Exception as e:
                print(f"error in mongo connection:\nDATABASE_HOST{DATABASE_HOST}")
                raise
        print("mongo connection successfull")
        return cls._instance
    
mongo_connection = MongoDatabaseConnector()