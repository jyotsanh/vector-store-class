from abc import ABC
import uuid
from pydantic import BaseModel, UUID4, Field
from typing import TypeVar, Generic, Type
from db.mongo import mongo_connection

from dotenv import load_dotenv
load_dotenv()
import os

MONGO_DATABASE = os.getenv("MONGO_DATABASE")

# bound: 'T' must be CustomODM or a subclass of CustomODM.
T = TypeVar("T", bound="CustomODM")

_mongo_db = mongo_connection.get_database(MONGO_DATABASE)

class CustomODM(BaseModel, Generic[T], ABC):
    id:UUID4=Field(default_factory=uuid.uuid4)

    @classmethod
    def find(cls: Type[T], **kwargs) -> T:
        print(kwargs)

    @classmethod
    def get(cls: Type[T], **kwargs) -> T: ...

    @classmethod
    def insert_one(cls: Type[T], **kwargs) -> T:
        print(kwargs)

    @classmethod
    def insert_many(cls: Type[T], **kwargs) -> T: ... 

    @classmethod
    def from_mongo(cls: Type[T], data:dict):
        if not data:
            raise ValueError(
                "Data is empty"
            )
        if "_id" in data:
            data["id"] = data.pop("_id")

        return cls(**data)

    @classmethod
    def get_collection_name(cls: Type[T]) -> str:
        if not hasattr(cls, "Settings") or not hasattr(cls.Settings, "name"):
            raise Exception(
                "Document should define an Settings configuration class with the name of the collection."
            )
        return cls.Settings.name

    def to_mongo(self: T, **kwargs):
        """parse 'id' (UUID object) into '_id' (str object)"""
        _exclude_unset = kwargs.pop("exclude_unset", False) # -> takes default value if not set.
        _by_alias = kwargs.pop("by_alias", True) # -> takes alias field name if set.

        parsed = self.model_dump(
            by_alias=_by_alias,
            exclude_unset=_exclude_unset,
            **kwargs
        )

        if "_id" not in parsed and "id" in parsed:
            parsed["_id"] = parsed.pop("id")

        for key, value in parsed.items():
            if isinstance(value, uuid.UUID):
                parsed[key] = str(value)
        return parsed

    def model_dump(self: T, **kwargs) -> dict:
        dict_ = super().model_dump(**kwargs)

        for key, value in dict_.items():
            if isinstance(value) is uuid.UUID:
                dict_[key] = str(value)
        return dict_

    def save(self: T, **kwargs) -> T | None:
        collection = _mongo_db[self.get_collection_name()]
        try:
            
            collection.insert_one(self.to_mongo(**kwargs))
            return self
        except Exception as error:
            print("Failed to insert document.")
            print(error)
            return None