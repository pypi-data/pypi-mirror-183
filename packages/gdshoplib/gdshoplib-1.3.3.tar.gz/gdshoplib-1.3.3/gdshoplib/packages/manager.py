import functools
import logging

import requests as r

from gdshoplib.core.settings import CacheSettings
from gdshoplib.packages.cache import BaseCache

logger = logging.getLogger(__name__)


class RequestManager:
    BASE_URL = "https://api.notion.com/v1/"

    def __init__(self, caching=False) -> None:
        self.caching = caching
        self.cache_settings = CacheSettings()
        if self.cache_settings.CACHE:
            self.CACHE = BaseCache.get_class(self.cache_settings.CACHE_CLASS)(
                dsn=self.cache_settings.CACHE_DSN + str(self.cache_settings.CACHE_DB),
                cache_period=self.cache_settings.CACHE_PERIOD,
            )

    def get_cache_key(self, path, **kwargs):
        return f"{path} | {str(kwargs.get('params', ''))}"

    def check_cacheble(self, *args, **kwargs):
        return kwargs.get("method").upper() == "GET" or "query" in args[0]

    def cache_response(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            if self.cache_settings.CACHE and not kwargs.get("cached") is False:
                cached = self.CACHE.get(self.get_cache_key(*args, **kwargs))

                if cached and not self.caching:
                    return cached

            data = func(self, *args, **kwargs)

            if self.check_cacheble(*args, **kwargs):
                self.CACHE[self.get_cache_key(*args, **kwargs)] = data

            return data

        return wrap

    @cache_response
    def make_request(self, path, *, method, params=None, cached=True):
        _path = f"{self.BASE_URL}{path}"
        _params = (
            dict(params=params) or {}
            if method.upper() == "GET"
            else dict(json=params) or {}
        )

        _r = r.request(
            method,
            _path,
            headers=self.get_headers(),
            **_params,
        )
        if not _r.ok:
            logger.warning(_r.json())
            if _r.status_code == 404:
                raise NotFoundException
            assert (
                False
            ), f"Запрос {method.upper()} {_path} прошел с ошибкой {_r.status_code}/n"
        return _r.json()

    def pagination(self, url, *, params=None, **kwargs):
        _params = params or {}
        response = None
        result = []
        while True:
            response = self.make_request(url, params=_params, **kwargs)
            result.extend(response["results"])

            if not response.get("has_more"):
                return result
            _params["start_cursor"] = response["next_cursor"]


class NotFoundException(Exception):
    ...
