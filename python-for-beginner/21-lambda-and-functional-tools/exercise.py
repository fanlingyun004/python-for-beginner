"""
Exercise 21: Lambda & Functional Tools

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。

from functools import reduce


def make_multiplier(n):
    """Return a function (closure) that multiplies its argument by n."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def square_all(numbers):
    """Return a list of every number in `numbers` squared. Use map() and a lambda."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def filter_evens(numbers):
    """Return a list of just the even numbers in `numbers`. Use filter() and a lambda."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def sort_by_length(words):
    """Return `words` sorted shortest to longest. Use sorted() with key=."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def total_with_reduce(numbers):
    """Return the sum of `numbers` using functools.reduce."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    double = make_multiplier(2)
    assert double(5) == 10
    triple = make_multiplier(3)
    assert triple(5) == 15
    assert double(4) == 8  # double still works independently of triple（double 仍可独立于 triple 正常工作）

    assert square_all([1, 2, 3]) == [1, 4, 9]

    assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

    assert sort_by_length(["banana", "kiwi", "fig"]) == ["fig", "kiwi", "banana"]

    assert total_with_reduce([1, 2, 3, 4]) == 10
    assert total_with_reduce([]) == 0

    print("All checks passed!")


if __name__ == "__main__":
    _check()
