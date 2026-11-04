"""A small, already-working ShoppingCart — the subject under test for this module."""
# 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。


class ShoppingCart:
    def __init__(self):
        self._items = {}  # item name -> quantity（商品名称 -> 数量）

    def add(self, name, quantity=1):
        self._items[name] = self._items.get(name, 0) + quantity

    def remove(self, name):
        if name not in self._items:
            raise KeyError(f"{name!r} is not in the cart")
        del self._items[name]

    def total_items(self):
        return sum(self._items.values())

    def __contains__(self, name):
        return name in self._items
