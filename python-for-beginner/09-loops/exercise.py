"""
Exercise 09: Loops (for / while)

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def sum_of_range(n):
    """Return the sum of all integers from 1 to n inclusive, using a for loop."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def count_vowels(word):
    """Return how many characters in word are a, e, i, o, or u (lowercase)."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def first_negative(numbers):
    """Return the first negative number in numbers, or None if there isn't one."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def countdown(n):
    """Return a list counting down from n to 1 inclusive, using a while loop."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def skip_multiples_of_three(n):
    """Return a list of 1..n inclusive, excluding multiples of 3. Use `continue`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert sum_of_range(5) == 15
    assert sum_of_range(1) == 1
    assert sum_of_range(10) == 55

    assert count_vowels("hello world") == 3
    assert count_vowels("xyz") == 0
    assert count_vowels("aeiou") == 5

    assert first_negative([1, 2, -3, 4, -5]) == -3
    assert first_negative([1, 2, 3]) is None

    assert countdown(3) == [3, 2, 1]
    assert countdown(1) == [1]

    assert skip_multiples_of_three(9) == [1, 2, 4, 5, 7, 8]

    print("All checks passed!")


if __name__ == "__main__":
    _check()
