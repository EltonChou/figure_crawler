from datetime import datetime
from ..PageParsers import YearlyAnnouncement

import requests as rq
from bs4 import BeautifulSoup


class GSCYearlyAnnouncement(YearlyAnnouncement):
    def __init__(self, category, _from=2006, to=None, lang="ja"):
        super().__init__(_from, to)
        self.base_url = make_base_url(category, lang)

    def __iter__(self):
        item_selector = ".hitItem:not(.shimeproduct) > .hitBox > a"
        for year in self.period:
            url = self.base_url(year)
            response = rq.get(url)
            page = BeautifulSoup(response.text, "lxml")
            product_urls = (item["href"] for item in page.select(item_selector))

            yield product_urls


def make_base_url(category, lang):
    def maker(year):
        base_url = "https://www.goodsmile.info/{lang}/products/category/{category}/announced/{year}".format(
            lang=lang,
            category=category,
            year=year,
        )

        return base_url
    return maker
