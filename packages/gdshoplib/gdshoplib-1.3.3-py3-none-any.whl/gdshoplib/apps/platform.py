from gdshoplib.apps.platforms.base import BasePlatformManager
from gdshoplib.apps.product import Product


class Platform:
    def __init__(self, manager=None):
        self.manager = manager
        self.__iterator = None

    def feed(self):
        assert self.manager, "В платформе не определен менеджер"
        return self.manager.get_feed(
            Product.query(filter=dict(status_description="Готово"))
        )

    @classmethod
    def get_platform(cls, *args, key, **kwargs):
        return cls(manager=BasePlatformManager.get_platform_manager_class(key=key)())

    @classmethod
    def iterator(cls):
        for platform in BasePlatformManager.__subclasses__():
            yield platform

    def __iter__(self):
        self.__iterator = self.__class__.iterator()
        return self

    def __next__(self):
        platform = Platform(manager=next(self.__iterator)())
        return platform
