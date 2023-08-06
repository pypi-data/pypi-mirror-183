import os
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, DirectoryPath

BASEPATH = Path(os.path.dirname(os.path.realpath(__file__))).parent


class GeneralSettings(BaseSettings):
    TEMPLATES_PATH: DirectoryPath = (BASEPATH / "templates").resolve()


class NotionSettings(BaseSettings):
    NOTION_SECRET_TOKEN: str
    CACHE_ENABLED: bool = True


class FeedSettings(BaseSettings):
    PHONE: str = "+7 499 384 44 03"
    ADDRESS: str = "Москва, ул. Крупской, 4к1"
    MANAGER_NAME: str = "Менеджер магазина"
    SHOP_NAME: str = "Grey Dream Horse Shop (Конный магазин)"
    COMPANY_NAME: str = "GD Horse Shop (Конный магазин)"
    SHOP_URL: str = "https://www.instagram.com/gd_horse_shop/"
    ULA_CATEGORY_ID: int = 5
    ULA_SUBCATEGORY_ID: int = 507


class S3Settings(BaseSettings):
    ENDPOINT_URL: str = "https://storage.yandexcloud.net"
    BUCKET_NAME: str = "gdshop"
    ACCESS_KEY: str
    SECRET_KEY: str


class CacheSettings(BaseSettings):
    CACHE_CLASS: str = "KeyDBCache"
    CACHE_DSN: Optional[str]
    CACHE_HSTORE: str = "notion"


class ProductSettings(BaseSettings):
    PRODUCT_DB: str = "2d1707fb-877d-4d83-8ae6-3c3d00ff5091"


class PriceSettins(BaseSettings):
    PRICE_VAT_RATIO: float = 0.16
    PRICE_NEITRAL_RATIO: float = 0.40
    PRICE_PROFIT_RATIO: float = 0.60
    EURO_PRICE: int = 75
