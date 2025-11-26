from .base import BaseCrawler
from typing import override


class MediumCrawler(BaseCrawler):

    @override
    def extract(self):
        return "extract method of medium blogs"