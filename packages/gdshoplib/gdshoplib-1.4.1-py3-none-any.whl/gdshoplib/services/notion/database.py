from gdshoplib.services.notion.notion import BasePage
from gdshoplib.services.notion.page import Page
from gdshoplib.services.notion.property import Property


class Database(BasePage):
    def initialize(self):
        self.page = self.notion.get_database(self.id)
        self.properties = Property(self.page)

    def refresh(self):
        self.notion.get_database(self.id)
        self.initialize()

    def pages(self, filter=None, params=None):
        if not filter:
            for page in self.notion.get_pages(self.id, params=params):
                yield Page(page["id"], notion=self.notion, parent=self)
            return

        for page in self.notion.get_pages(self.id, params=params):
            filtered = True
            for k, v in filter.items():
                page = Page(page["id"], notion=self.notion, parent=self)
                if str(page.__getattr__(k)).lower() != str(v).lower():
                    filtered = False
            if filtered:
                yield page

    def commit(self):
        # Проитерироваться по изменениям и выполнить в Notion
        ...

    def to_json(self):
        # Вернуть товар в json
        ...
