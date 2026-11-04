"""
Exercise 01: Hello, World & Comments

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def hello_world():
    """Return the exact string "Hello, World!"."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def say_hello(name):
    """Return "Hello, <name>!" built using string concatenation (+)."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def two_lines():
    """Return one string that prints as two lines: "First line" then "Second line"."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert hello_world() == "Hello, World!"

    assert say_hello("Ava") == "Hello, Ava!"
    assert say_hello("Sam") == "Hello, Sam!"

    assert two_lines() == "First line\nSecond line"
    assert two_lines().count("\n") == 1

    print("All checks passed!")


if __name__ == "__main__":
    _check()
