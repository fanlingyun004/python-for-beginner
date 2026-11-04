"""
Exercise 06: Booleans & Comparisons

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def is_falsy(value):
    """Return True if Python would treat `value` as falsy in an `if` check."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def in_range(n, low, high):
    """Return whether n is between low and high, inclusive. Use a chained comparison."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def both_positive(a, b):
    """Return True only if both a and b are greater than 0."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def at_least_one_true(a, b, c):
    """Return True if at least one of a, b, c is True."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def flip(value):
    """Return the boolean opposite of value."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert is_falsy(0) is True
    assert is_falsy("") is True
    assert is_falsy([]) is True
    assert is_falsy(None) is True
    assert is_falsy(False) is True
    assert is_falsy(1) is False
    assert is_falsy("a") is False
    assert is_falsy([0]) is False

    assert in_range(5, 1, 10) is True
    assert in_range(1, 1, 10) is True
    assert in_range(10, 1, 10) is True
    assert in_range(11, 1, 10) is False
    assert in_range(0, 1, 10) is False

    assert both_positive(1, 2) is True
    assert both_positive(-1, 2) is False
    assert both_positive(0, 2) is False

    assert at_least_one_true(False, False, True) is True
    assert at_least_one_true(False, False, False) is False
    assert at_least_one_true(True, True, True) is True

    assert flip(True) is False
    assert flip(False) is True

    print("All checks passed!")


if __name__ == "__main__":
    _check()
