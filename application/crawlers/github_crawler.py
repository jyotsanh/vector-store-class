from .base import BaseCrawler
from typing import override


class GithubCrawler(BaseCrawler):

    @override
    def extract(self):
        return "github crawlers for github repo."