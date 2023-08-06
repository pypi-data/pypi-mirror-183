from multiprocessing import Pool

import typer
from rich import print

from gdshoplib import Platform, Product
from gdshoplib.core.settings import CacheSettings
from gdshoplib.packages.cache import KeyDBCache
from gdshoplib.services.notion.notion import Notion

app = typer.Typer()


@app.command()
def sku_set():
    notion = Notion(caching=True)
    for page in Product.query(
        notion=notion,
        params={
            "filter": {
                "and": [
                    {"property": "Наш SKU", "rich_text": {"is_empty": True}},
                    {"property": "Цена (eur)", "number": {"is_not_empty": True}},
                ]
            }
        },
    ):
        sku = page.generate_sku()
        while not Product.query(notion=notion, filter={"sku": sku}):
            sku = page.generate_sku()

        page.notion.update_prop(
            page.id, params={"properties": {"Наш SKU": [{"text": {"content": sku}}]}}
        )
        print(Product(page.id, notion=notion).sku)


@app.command()
def cache_clean():
    settings = CacheSettings()
    cache = KeyDBCache(dsn=f"{settings.CACHE_DSN}{settings.CACHE_DB}", cache_period=0)
    cache.clean("[blocks|pages|databases]*")


def warm_product(id):
    product = Product(id)
    product.price.now
    product.kit
    product.notes
    product.specifications
    product.tags
    product.media
    product.description
    print(product.sku)


@app.command()
def cache_warm():
    with Pool(5) as p:
        for product in Product.query(notion=Notion(caching=True)):
            p.apply_async(warm_product, (product.id,))


@app.command()
def cache_count(pattern="*"):
    settings = CacheSettings()
    cache = KeyDBCache(
        dsn=f"{settings.CACHE_DSN}/{settings.CACHE_DB}", cache_period=7 * 24 * 60 * 60
    )
    print(len(cache.search(pattern)))


def warm_product_media(id):
    for media in Product(id).media:
        media.fetch()
        print(f"{media.file_key}")


@app.command()
def media_warm():
    with Pool(10) as p:
        for product in Product.query(notion=Notion(caching=True)):
            p.apply_async(warm_product_media, (product.id,))


def warm_platfrom_feed(platform_key):
    print(platform_key)
    settings = CacheSettings()
    cache = KeyDBCache(
        dsn=f"{settings.CACHE_DSN}/{settings.CACHE_DB}", cache_period=7 * 24 * 60 * 60
    )
    feed = Platform.get_platform(key=platform_key).feed()
    cache[f"feed/{platform_key.lower()}"] = feed


@app.command()
def feed_warm(platform_key=None):
    if platform_key:
        warm_platfrom_feed(platform_key=platform_key)
        return

    for platform in Platform():
        warm_platfrom_feed(platform_key=platform.manager.KEY)


if __name__ == "__main__":
    app()
