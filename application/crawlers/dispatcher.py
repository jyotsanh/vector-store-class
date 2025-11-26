from .base import BaseCrawler
from .github_crawler import GithubCrawler
from .medium_crawler import MediumCrawler
from urllib.parse import urlparse


class CrawlerDispatcher():
    def __init__(self):
        self._crawlers: dict = {}

    def register_github_crawler(self):
        self._register_crawler(netloc="github.com" ,crawler=GithubCrawler)

    def register_medium_crawler(self):
        self._register_crawler(netloc="medium.com", crawler=MediumCrawler)

    def _register_crawler(self, netloc:str, crawler:type[BaseCrawler]):
        if netloc in self._crawlers: # already in dictionary then return
            return
        self._crawlers[netloc] == crawler
        
    @classmethod
    def build(cls) -> "CrawlerDispatcher":
        dispatcher = cls()
        return dispatcher


    def get_crawler(self, url:str) -> BaseCrawler:
        output = urlparse(url=url)
        domain = output.netloc
        if domain in self._crawlers:
            return self._crawlers[domain]
        raise Exception(
            f"no crawler is available for this domain {domain}"
        )