from .base import VectorDB, VectorStore
from .pinecone import PineconeVectorStore

class VectorDispatcher:
    def __init__(self) -> None:
        self._vector_db = {}

    @classmethod
    def build(cls) -> "VectorDispatcher":
        dispatcher = cls()
        return dispatcher
    
    def register_pinecone_db(self) -> None:
        self._vector_db[VectorDB.PINECONE] = PineconeVectorStore

    def register_milvus_db(self): ...
    def register_qdrant_db(self): ...
    def register_chroma_db(self): ...

    def get_vector_db(self, vector_db_name:VectorDB) -> VectorStore:
        if vector_db_name in self._vector_db:
            return self._vector_db[vector_db_name]
        raise NotImplementedError(f"'{vector_db_name.value}' is not register")