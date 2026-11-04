"""
Exercise 15: Comprehensions

Implement each function below using a comprehension. Run this file
directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def squares_up_to(n):
    """Return [1, 4, 9, ...] — squares of 1 through n inclusive."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using a list comprehension（待完成：使用列表推导式实现）
    raise NotImplementedError


def evens_only(numbers):
    """Return a list of just the even numbers from `numbers`, order preserved."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using a list comprehension（待完成：使用列表推导式实现）
    raise NotImplementedError


def upper_words(words):
    """Return a new list with every word in `words` uppercased."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using a list comprehension（待完成：使用列表推导式实现）
    raise NotImplementedError


def length_map(words):
    """Return a dict mapping each word in `words` to its length."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using a dict comprehension（待完成：使用字典推导式实现）
    raise NotImplementedError


def unique_lengths(words):
    """Return a set of the distinct word lengths present in `words`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using a set comprehension（待完成：使用集合推导式实现）
    raise NotImplementedError


def _check():
    assert squares_up_to(4) == [1, 4, 9, 16]
    assert squares_up_to(1) == [1]

    assert evens_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert evens_only([1, 3, 5]) == []

    assert upper_words(["hi", "there"]) == ["HI", "THERE"]

    assert length_map(["hi", "hello", "hey"]) == {"hi": 2, "hello": 5, "hey": 3}

    assert unique_lengths(["hi", "hello", "hey", "yo"]) == {2, 5, 3}

    print("All checks passed!")


if __name__ == "__main__":
    _check()
