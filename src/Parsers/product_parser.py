from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Union

from src.utils import get_page
from src.utils._class import OrderPeriod


class ProductParser(ABC):
    def __init__(self, url, headers, cookies, page):
        self.__url = url
        self.__page = page if page else get_page(url, headers, cookies)

    @property
    def url(self):
        return self.__url

    @property
    def page(self):
        return self.__page

    @abstractmethod
    def _parse_detail(self):
        pass

    @abstractmethod
    def parse_name(self) -> str:
        pass

    @abstractmethod
    def parse_series(self) -> str:
        pass

    @abstractmethod
    def parse_manufacturer(self) -> str:
        pass

    @abstractmethod
    def parse_category(self) -> str:
        pass

    @abstractmethod
    def parse_prices(self) -> List[int]:
        pass

    @abstractmethod
    def parse_release_dates(self) -> List[datetime]:
        pass

    @abstractmethod
    def parse_sculptors(self) -> List[str]:
        pass

    @abstractmethod
    def parse_scale(self) -> str:
        pass

    @abstractmethod
    def parse_size(self) -> int:
        pass

    @abstractmethod
    def parse_copyright(self) -> str:
        pass

    @abstractmethod
    def parse_releaser(self) -> str:
        pass

    @abstractmethod
    def parse_resale(self) -> bool:
        pass

    @abstractmethod
    def parse_images(self) -> List[str]:
        pass

    def parse_distributer(self) -> Union[str, None]:
        return None

    def parse_adult(self) -> bool:
        return False

    def parse_order_period(self) -> OrderPeriod:
        return OrderPeriod(None, None)

    def parse_paintworks(self) -> List:
        return []

    def parse_JAN(self) -> Union[str, None]:
        return None

    def parse_maker_id(self) -> Union[str, None]:
        return None
