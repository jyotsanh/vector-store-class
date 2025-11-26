# builder design pattern

from .base import VectorDB, VectorStore
from .pinecone import PineconeVectorStore
from .chroma import ChromaVectorStore
from .milvus import MilvusVectorStore
from .qdrant import QdrantVectorStore


class VectorDispatcher:
    def __init__(self) -> None:
        self._vector_db = {}

    @classmethod
    def build(cls) -> "VectorDispatcher":
        dispatcher = cls()
        return dispatcher
    
    def register_pinecone_db(self) -> None:
        self._register_db(
            vector_db=VectorDB.PINECONE,
            vector_store=PineconeVectorStore
        )
        

    def register_milvus_db(self):
        self._register_db(
            vector_db=VectorDB.MILVUS,
            vector_store=MilvusVectorStore
        )


    def register_qdrant_db(self):
        self._register_db(
            vector_db=VectorDB.QDRANT,
            vector_store=QdrantVectorStore
        )

    def register_chroma_db(self):
        self._register_db(
            vector_db=VectorDB.CHROMA,
            vector_store=ChromaVectorStore
        )

    def _register_db(self, vector_db:VectorDB, vector_store:type[VectorStore]):
        if vector_db.name in self._vector_db:
            return 
        self._vector_db[VectorDB.PINECONE] = vector_store

    def get_vector_db(self, vector_db_name:VectorDB) -> VectorStore:
        if vector_db_name in self._vector_db:
            return self._vector_db[vector_db_name]
        raise NotImplementedError(f"'{vector_db_name.value}' is not register")