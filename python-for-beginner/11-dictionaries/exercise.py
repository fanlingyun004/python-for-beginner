"""
Exercise 11: Dictionaries

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def get_or_default(d, key, default):
    """Return d[key] if present, otherwise default. Use .get()."""
    # 中文翻译：返回 d[key]；发生 KeyError 时返回“not found”。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def add_or_update(d, key, value):
    """Set d[key] = value (mutating d) and return d."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def word_counts(words):
    """Return a dict mapping each word to its count in the `words` list."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def merge_with_overrides(defaults, overrides):
    """Return a new dict: defaults with overrides layered on top."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def invert(d):
    """Return a new dict with d's keys and values swapped."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert get_or_default({"a": 1}, "a", 0) == 1
    assert get_or_default({"a": 1}, "b", 0) == 0

    d = {"a": 1}
    result = add_or_update(d, "b", 2)
    assert result == {"a": 1, "b": 2}
    assert d == {"a": 1, "b": 2}

    assert word_counts(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}
    assert word_counts([]) == {}

    assert merge_with_overrides({"a": 1, "b": 2}, {"b": 20}) == {"a": 1, "b": 20}
    assert merge_with_overrides({"a": 1}, {}) == {"a": 1}

    assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    print("All checks passed!")


if __name__ == "__main__":
    _check()
