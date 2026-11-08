"""
Exercise 02: Variables & Data Types

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def type_name(value):
    """Return the name of value's type as a string, e.g. type_name(1) == "int"."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    return type(value).__name__
    


def is_none(value):
    """Return True if value is None, False otherwise. Use `is`, not `==`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    return value is None


def swap(a, b):
    """Return (b, a) using multiple assignment, not a temp variable."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def describe_person(name, age):
    """Return an f-string: "<name> is <age> years old."."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert type_name(1) == "int"
    assert type_name(1.5) == "float"
    assert type_name("hi") == "str"
    assert type_name(None) == "NoneType"
    assert type_name(True) == "bool"

    assert is_none(None) is True
    assert is_none(0) is False
    assert is_none("") is False

    assert swap(1, 2) == (2, 1)
    assert swap("a", "b") == ("b", "a")

    assert describe_person("Ava", 30) == "Ava is 30 years old."
    assert describe_person("Sam", 8) == "Sam is 8 years old."

    print("All checks passed!")


if __name__ == "__main__":
    _check()
