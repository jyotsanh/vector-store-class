from abc import ABC, abstractmethod

class BaseCrawler(ABC):
    
    @abstractmethod
    def extract(self): ...