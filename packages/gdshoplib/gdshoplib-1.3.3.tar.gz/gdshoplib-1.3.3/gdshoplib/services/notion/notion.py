# Менеджер управления Notion
from gdshoplib.core.settings import NotionSettings
from gdshoplib.packages.manager import RequestManager
from gdshoplib.services.notion.users import User


class Notion(RequestManager):
    def __init__(self, caching=False) -> None:
        self.notion_settings = NotionSettings()
        super().__init__(caching)

    def get_headers(self):
        return {
            **self.auth_headers(),
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
            "Accept": "application/json",
        }

    def auth_headers(self):
        return {"Authorization": "Bearer " + self.notion_settings.NOTION_SECRET_TOKEN}

    # TODO: Сделать декоратор для обработки запросов
    def get_user(self, user_id, params=None):
        data = self.make_request(f"users/{user_id}", method="get", params=params).json()
        if data.get("results"):
            data = data.get("results")[0]
        return User.parse_obj(
            {**data, "email": data.get("person", {}).get("email") or data.get("name")}
        )

    def get_capture(self, block):
        _capture = block[block["type"]].get("caption")
        return _capture[0].get("plain_text") if _capture else ""

    def get_blocks(self, parent_id, params=None):
        blocks = []
        for block in self.pagination(
            f"blocks/{parent_id}/children", method="get", params=params
        ):
            if not block.get("has_children"):
                blocks.append(block)
            else:
                blocks.extend(self.get_blocks(block.get("id")))
        return blocks

    def get_block(self, block_id, cached=True, params=None):
        return self.make_request(
            f"blocks/{block_id}", method="get", cached=cached, params=params
        )

    def get_page(self, page_id, cached=True, params=None):
        return self.make_request(
            f"pages/{page_id}", method="get", cached=cached, params=params
        )

    def get_database(self, database_id, cached=True, params=None):
        return self.make_request(
            f"databases/{database_id}", method="get", cached=cached, params=params
        )

    def get_pages(self, database_id, params=None):
        return self.pagination(
            f"databases/{database_id}/query", method="post", params=params
        )

    def update_prop(self, product_id, params=None):
        # TODO: Переделать в обновление параметра
        self.make_request(
            f"pages/{product_id}",
            method="patch",
            params=params,
            cached=False
            # params={"properties": {"Наш SKU": [{"text": {"content": sku}}]}},
        )

    def update_block(self, block_id, params):
        self.make_request(
            f"blocks/{block_id}",
            method="patch",
            params=params
            # params={"code": {"rich_text": [{"text": {"content": content}}]}},
        )


class BasePage:
    def __init__(self, id, *, notion=None, parent=None):
        self.id = id
        self.notion = Notion() if not notion else notion
        self.parent = parent
        self.history = {}
        self.change_log = {}
        self.initialize()

    def __str__(self) -> str:
        return f"{self.__class__}: {self.id}"

    def __repr__(self) -> str:
        return f"{self.__class__}: {self.id}"

    def __getitem__(self, key):
        try:
            return super(BasePage, self).__getattribute__(key)
        except AttributeError:
            return self.__getattr__(key)

    def __getattr__(self, name: str):
        if self.page and name in self.page.keys():
            return self.page[name]

        return self.properties[name]
        # return super(BasePage, self).__getattr__(name)
