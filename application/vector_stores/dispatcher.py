from enum import Enum
class VectorDB(Enum):
    PINECONE = "pinecone"
    MILVUS = "milvus"
    QDRANT = "qdrant"
    CHROMA = "chroma"

class VectorDispatcher:
    def __init__(self) -> None:
        self._vector_db = {}

    @classmethod
    def build(cls) -> "VectorDispatcher":
        dispatcher = cls()
        return dispatcher
    
    def register_pinecone_db(): ...
    def register_milvus_db(): ...
    def register_qdrant_db(): ...
    def register_chroma_db(): ...

    def get_vector_db(self, vector_db_name:VectorDB): ...