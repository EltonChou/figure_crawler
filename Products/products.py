from abc import ABC

from Parsers.alter import AlterProductParser as __alter_parser
from Parsers.gsc import GSCProductParser


class Product(ABC):
    def __init__(self, url, parser):
        parser = parser(url)

        self.__url = url
        self.__name = parser.parse_name()
        self.__series = parser.parse_series()
        self.__manufacturer = parser.parse_manufacturer()
        self.__category = parser.parse_category()
        self.__price = parser.parse_prices()
        self.__release_date = parser.parse_release_date()
        self.__order_period = parser.parse_order_period()
        self.__size = parser.parse_size()
        self.__scale = parser.parse_scale()
        self.__sculptor = parser.parse_sculptors()
        self.__paintwork = parser.parse_paintworks()
        self.__resale = parser.parse_resale()
        self.__adult = parser.parse_adult()
        self.__copyright = parser.parse_copyright()
        self.__releaser = parser.parse_releaser()
        self.__distributer = parser.parse_distributer()
        self.__jan = parser.parse_JAN()
        self.__maker_id = parser.parse_maker_id()
        self.__images = parser.parse_images()

    @property
    def url(self):
        return self.__url

    @property
    def maker_id(self):
        return self.__maker_id

    @property
    def name(self):
        return self.__name

    @property
    def series(self):
        return self.__series

    @property
    def manufacturer(self):
        return self.__manufacturer

    @property
    def category(self):
        return self.__category

    @property
    def price(self):
        return self.__price

    @property
    def release_date(self):
        return self.__release_date

    @property
    def order_period(self):
        return self.__order_period

    @property
    def scale(self):
        return self.__scale

    @property
    def size(self):
        return self.__size

    @property
    def sculptor(self):
        return self.__sculptor

    @property
    def paintwork(self):
        return self.__paintwork

    @property
    def resale(self):
        return self.__resale

    @property
    def adult(self):
        return self.__adult

    @property
    def copyright(self):
        return self.__copyright

    @property
    def releaser(self):
        return self.__releaser

    @property
    def distributer(self):
        return self.__distributer

    @property
    def jan(self):
        return self.__jan

    @property
    def images(self):
        return self.__images

    def keys(self):
        return [
            "adult",
            "category",
            "distributer",
            "images",
            "jan",
            "maker_id",
            "manufacturer",
            "name",
            "order_period",
            "paintwork",
            "price",
            "release_date",
            "releaser",
            "resale",
            "scale",
            "sculptor",
            "series",
            "size",
            "url"
        ]

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "[{manufacturer}] {name} {category}".format(**self)


class GSCProduct(Product):
    def __init__(self, url, parser=None):
        parser = parser or GSCProductParser
        super().__init__(url, parser)


class AlterProduct(Product):
    def __init__(self, url, parser=None):
        parser = parser = __alter_parser
        super().__init__(url, parser)