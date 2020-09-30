from urllib.parse import urljoin
import requests as rq
from bs4 import BeautifulSoup

from ..PageParsers import YearlyAnnouncement


class AlterYearlyAnnouncement(YearlyAnnouncement):
    def __init__(self, category, _from=2005, to=None):
        super().__init__(_from, to)
        self.url = f"https://alter-web.jp/{category}"

    def __iter__(self):
        base_product_url = "https://alter-web.jp/"
        for year in self.period:
            selector = "figure > a"
            params = { "yy": year }
            response = rq.get(self.url, params=params)
            page = BeautifulSoup(response.text, "lxml")
            product_urls = (urljoin(base_product_url, item["href"]) for item in page.select(selector))

            yield product_urls


if __name__ == "__main__":
    print(__name__)