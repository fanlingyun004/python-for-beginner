"""
Exercise 10: Tuples

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def make_point(x, y):
    """Return the tuple (x, y)."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def sum_point(point):
    """point is an (x, y) tuple. Unpack it and return x + y."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def first_two(t):
    """Return a tuple of the first two elements of t, using indexing."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def count_occurrences(t, value):
    """Return how many times value appears in tuple t."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def combine(a, b):
    """Return the concatenation of tuples a and b."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert make_point(3, 4) == (3, 4)

    assert sum_point((3, 4)) == 7
    assert sum_point((0, 0)) == 0

    assert first_two((1, 2, 3, 4)) == (1, 2)
    assert first_two(("a", "b")) == ("a", "b")

    assert count_occurrences((1, 2, 2, 3, 2), 2) == 3
    assert count_occurrences((1, 2, 3), 9) == 0

    assert combine((1, 2), (3, 4)) == (1, 2, 3, 4)
    assert combine((), (1,)) == (1,)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
