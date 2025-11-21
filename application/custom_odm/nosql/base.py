from abc import ABC
from pydantic import BaseModel
from typing import TypeVar, Generic
from ..db.mongo import mongo_connection

from dotenv import load_dotenv
load_dotenv()
import os

MONGO_DATABASE = os.getenv("MONGO_DATABASE")


T = TypeVar("T")

_mongo_db = mongo_connection.get_database(MONGO_DATABASE)

class CustomODM(BaseModel, Generic[T], ABC):

    @classmethod
    def find(cls) -> T: ...


    def get_collection_name(self): ...