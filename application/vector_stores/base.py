from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict


class VectorStore(ABC):

    @abstractmethod
    async def insert(self) -> None: ...

    @abstractmethod
    async def query(self) -> None: ...

    @abstractmethod
    async def asimilarity_search(self, query:str) -> str: ...
