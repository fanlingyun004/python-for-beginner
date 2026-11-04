"""
Exercise 22: Iterators & Generators

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def count_up_to(n):
    """Generator function: yield 1, 2, ..., n in order."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement (use yield, not return). Delete the two lines below（待完成：implement (use yield, not return). Delete the two lines below）
    # once you do -- they only exist so this stays a generator function（完成后删除这些占位行。）
    # (the mere presence of `yield` in a function makes it one) until you（函数中出现 yield 就会成为生成器。）
    # write your own yield statement(s).（请写出自己的 yield 语句。）
    raise NotImplementedError
    yield


def even_numbers_up_to(n):
    """Generator function: yield only the even numbers from 1 to n inclusive."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement (use yield, not return). Same note as above.（待完成：implement (use yield, not return). Same note as above.）
    raise NotImplementedError
    yield


def first_two(iterable):
    """Return a tuple of the first two items of `iterable`, using iter()/next()."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def squares_generator_expr(n):
    """Return a generator expression computing the squares of 0 through n - 1."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert list(count_up_to(5)) == [1, 2, 3, 4, 5]
    assert list(count_up_to(1)) == [1]

    assert list(even_numbers_up_to(10)) == [2, 4, 6, 8, 10]
    assert list(even_numbers_up_to(1)) == []

    assert first_two([10, 20, 30]) == (10, 20)
    assert first_two("abcdef") == ("a", "b")
    assert first_two(count_up_to(5)) == (1, 2)  # works on a generator too, not just a list（同样适用于生成器，而不仅是列表）

    gen = squares_generator_expr(5)
    assert list(gen) == [0, 1, 4, 9, 16]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
