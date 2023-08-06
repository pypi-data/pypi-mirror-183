import functools

from gdshoplib.core.settings import PriceSettins

price_settings = PriceSettins()


class Price:
    def __init__(self, product):
        self.product = product

    def handle_ratio(*rations):
        def decor(func):
            @functools.wraps(func)
            def wrap(self, *args, **kwargs):
                ration = sum([1, *rations])
                return func(self, *args, **kwargs) * ration

            return wrap

        return decor

    def round(func):
        @functools.wraps(func)
        def wrap(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            return int(round(result, 0))

        return wrap

    @property
    def eur(self):
        return self.product.price_eur

    @property
    @handle_ratio(price_settings.EURO_PRICE)
    def base(self):
        return self.product.price_eur

    @property
    @round
    def now(self):
        return self.profit

    @property
    @round
    @handle_ratio(
        price_settings.PRICE_PROFIT_RATIO,
        price_settings.PRICE_NEITRAL_RATIO,
        price_settings.PRICE_VAT_RATIO,
    )
    def profit(self):
        return self.base

    # Коэфиценты
    # 0.16 - Себестоимость
    # 0.40 - Безубыточность
    # 0.60 - Ходовая
    # x.xx - Добавочная стоимость категории
    # x.xx - Добавочная стоимость бренда
    # x.xx - Добавочная стоимость платформы
