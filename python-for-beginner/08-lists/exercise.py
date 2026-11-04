"""
Exercise 08: Lists

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def first_and_last_items(items):
    """Return a tuple (first, last) of items, using indexing."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def add_to_front(items, item):
    """Return a NEW list with item at the front. Don't modify the original items."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def remove_item(items, target):
    """Remove the first occurrence of target from items (in place) and return items."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def total_and_average(numbers):
    """Return a tuple (total, average) using sum() and len()."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def sort_descending(numbers):
    """Return a NEW list of numbers sorted largest to smallest. Don't mutate the original."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert first_and_last_items([1, 2, 3, 4]) == (1, 4)
    assert first_and_last_items(["only"]) == ("only", "only")

    original = [1, 2, 3]
    result = add_to_front(original, 0)
    assert result == [0, 1, 2, 3]
    assert original == [1, 2, 3]  # original must be unchanged（原对象必须保持不变）

    items = ["a", "b", "c", "b"]
    result = remove_item(items, "b")
    assert result == ["a", "c", "b"]
    assert items == ["a", "c", "b"]  # mutated in place（对象会被原地修改）

    assert total_and_average([1, 2, 3]) == (6, 2.0)
    assert total_and_average([10, 20]) == (30, 15.0)

    numbers = [3, 1, 4, 1, 5]
    result = sort_descending(numbers)
    assert result == [5, 4, 3, 1, 1]
    assert numbers == [3, 1, 4, 1, 5]  # original must be unchanged（原对象必须保持不变）

    print("All checks passed!")


if __name__ == "__main__":
    _check()
