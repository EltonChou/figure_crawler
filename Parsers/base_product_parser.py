from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from utils import get_page


class ProductParser(ABC):
    def __init__(self, url, headers, cookies):
        self.__url = url
        self.__page = get_page(url, headers, cookies)

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
    def parse_price(self) -> List[int]:
        pass

    @abstractmethod
    def parse_release_date(self) -> List[datetime]:
        pass

    @abstractmethod
    def parse_sculptor(self) -> List[str]:
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

    def parse_distributer(self):
        return None

    def parse_adult(self) -> bool:
        return False

    def parse_order_period(self) -> tuple:
        return None

    def parse_paintwork(self) -> List[str]:
        return None

    def parse_JAN(self) -> str:
        return None

    def parse_maker_id(self) -> str:
        return None
