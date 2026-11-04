"""
Exercise 13: Functions

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def power(base, exponent=2):
    """Return base raised to exponent, defaulting to squaring."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def full_name(first, last, middle=None):
    """Return "first last", or "first middle last" if middle is given."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def sum_all(*numbers):
    """Return the sum of any number of positional arguments."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def build_profile(**details):
    """Return the details dict built from however many keyword arguments were passed."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def safe_divide(a, b):
    """Return a / b, or None if b is 0."""
    # 中文翻译：返回 a / b；发生 ZeroDivisionError 时返回 None。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert power(3) == 9
    assert power(2, 3) == 8
    assert power(base=5, exponent=0) == 1

    assert full_name("Ava", "Lee") == "Ava Lee"
    assert full_name("Ava", "Lee", "Marie") == "Ava Marie Lee"

    assert sum_all(1, 2, 3) == 6
    assert sum_all() == 0
    assert sum_all(5) == 5

    assert build_profile(name="Ava", age=30) == {"name": "Ava", "age": 30}
    assert build_profile() == {}

    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None

    print("All checks passed!")


if __name__ == "__main__":
    _check()
