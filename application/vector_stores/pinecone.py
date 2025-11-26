# builder design pattern.

from .base import VectorStore

class PineconeVectorStore(VectorStore):
    def __init__(self) -> None:
        super().__init__()
    
    async def insert(self):
        pass

    