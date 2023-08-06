from gdshoplib.services.notion.notion import BasePage, Notion
from gdshoplib.services.notion.property import Property


class Block(BasePage):
    def initialize(self):
        self.page = self.notion.get_block(self.id)
        self.properties = Property(self.page)

    def refresh(self):
        Notion(caching=True).get_block(self.id)
        self.initialize()

    def get_capture(self):
        capture = self[self.type].get("caption")
        return capture[0].get("plain_text") if capture else ""

    def commit(self):
        # Проитерироваться по изменениям и выполнить в Notion
        ...

    def to_json(self):
        # Вернуть товар в json
        ...
