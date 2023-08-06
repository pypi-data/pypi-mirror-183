from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.packages.feed import Feed


class AvitoManager(BasePlatformManager, Feed):
    KEY = "AVITO"
