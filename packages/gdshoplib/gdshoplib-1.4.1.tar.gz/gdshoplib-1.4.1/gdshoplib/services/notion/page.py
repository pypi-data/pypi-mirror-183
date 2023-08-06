from gdshoplib.services.notion.block import Block
from gdshoplib.services.notion.notion import BasePage
from gdshoplib.services.notion.property import Property


class Page(BasePage):
    def initialize(self):
        self.page = self.notion.get_page(self.id)
        self.properties = Property(self.page)

    def refresh(self):
        self.notion.get_page(self.id)
        self.initialize()

    def blocks(self, filter=None):
        if not filter:
            for block in self.notion.get_blocks(self.id):
                yield Block(block["id"], notion=self.notion, parent=self)
            return

        for block in self.notion.get_blocks(self.id):
            for k, v in filter.items():
                block = Block(block["id"], notion=self.notion, parent=self)
                if str(block.__getattr__(k)).lower() == str(v).lower():
                    yield block

    def commit(self):
        # Проитерироваться по изменениям и выполнить в Notion
        ...

    def to_json(self):
        # Вернуть товар в json
        ...
