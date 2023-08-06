import re
from random import randrange

from gdshoplib.apps.products.brand import Brand
from gdshoplib.apps.products.description import ProductDescription
from gdshoplib.apps.products.media import ProductMedia
from gdshoplib.apps.products.price import Price
from gdshoplib.core.settings import ProductSettings
from gdshoplib.services.notion.database import Database
from gdshoplib.services.notion.page import Page


class Product(Page):
    SETTINGS = ProductSettings()

    def __init__(self, *args, **kwargs):
        self._images = None
        self._videos = None
        self._price = None
        self._description = None
        self._kit = None

        super(Product, self).__init__(*args, **kwargs)

    @classmethod
    def query(cls, filter=None, params=None, notion=None):
        for page in Database(cls.SETTINGS.PRODUCT_DB, notion=notion).pages(
            filter=filter, params=params
        ):
            yield cls(page["id"], notion=page.notion, parent=page.parent)

    @property
    def brand(self):
        if self.brand_field:
            return Brand(self.brand_field, notion=self.notion, parent=self)

    @property
    def media(self):
        return [*self.images, *self.videos]

    @property
    def videos(self):
        if not self._videos:
            self._videos = list(
                ProductMedia(block.id, notion=self.notion, parent=self)
                for block in self.blocks(filter={"type": "video"})
            )
        return self._videos

    @property
    def images(self):
        if not self._images:
            self._images = list(
                ProductMedia(block.id, notion=self.notion, parent=self)
                for block in self.blocks(filter={"type": "image"})
            )
        return self._images

    @property
    def price(self):
        if not self._price:
            self._price = Price(self)
        return self._price

    @property
    def description(self):
        if not self._description:
            self._description = ProductDescription(self)
        return self._description

    @staticmethod
    def split(source):
        if not source:
            return []
        return [tag for tag in source.split("/")]

    @property
    def tags(self):
        return self.split(self.tags_field)

    @property
    def specifications(self):
        return self.split(self.specifications_field)

    @property
    def notes(self):
        return self.split(self.notes_field)

    @property
    def kit(self):
        if not self.kit_field:
            return

        if not self._kit:
            self._kit = []
            for page_id in self.kit_field:
                if self.id == page_id:
                    continue
                self._kit.append(
                    Product(page_id, notion=self.notion, parent=self.parent)
                )
        return self._kit

    def available(self):
        result = bool(
            self.quantity
            and self.status_publication in ("Готово", "Обновление", "Проверка")
        )
        return result

    def generate_sku(self):
        # Сгенерировать SKU на основе продукта
        # Категория.Бренд.Цена_покупки.месяц_добавления.год_добавления.случайные_4_числа

        sku = (
            f"{self.brand.title.upper() if self.brand else ''}"
            f"{int(self.price.eur)}"
            f"{randrange(1111, 9999)}"
        )

        return re.sub(r"\W", "", sku)

    def __str__(self) -> str:
        return f"{self.__class__}: {self.sku}"

    def __repr__(self) -> str:
        return f"{self.__class__}: {self.sku}"
