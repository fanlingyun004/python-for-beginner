"""
Exercise 25: Regular Expressions

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。

import re


def contains_digit(text):
    """Return whether text contains at least one digit."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def extract_numbers(text):
    """Return a list of every run of digits in text, as strings."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def mask_digits(text):
    """Return text with every run of digits replaced by "#"."""
    # 中文翻译：将文本中连续出现的一段数字替换为“#”。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def is_valid_hex_color(text):
    """Return whether text is "#" followed by exactly 6 hex digits."""
    # 中文翻译：判断文本是否为“#”后跟恰好 6 位十六进制数字。
    # TODO: implement (anchor with ^ and $)（待完成：实现，并使用 ^ 和 $ 进行锚定）
    raise NotImplementedError


def extract_date_parts(text):
    """Find a YYYY-MM-DD date in text; return (year, month, day) strings, or None."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using capture groups（待完成：使用捕获组实现）
    raise NotImplementedError


def _check():
    assert contains_digit("order #42") is True
    assert contains_digit("no numbers here") is False

    assert extract_numbers("a1 b22 c333") == ["1", "22", "333"]
    assert extract_numbers("no numbers") == []

    assert mask_digits("a1 b22 c333") == "a# b# c#"
    assert mask_digits("clean") == "clean"

    assert is_valid_hex_color("#1A2b3C") is True
    assert is_valid_hex_color("#ffffff") is True
    assert is_valid_hex_color("1A2b3C") is False
    assert is_valid_hex_color("#12") is False
    assert is_valid_hex_color("#1A2b3CZZ") is False

    assert extract_date_parts("Date: 2026-01-15 confirmed") == ("2026", "01", "15")
    assert extract_date_parts("no date here") is None

    print("All checks passed!")


if __name__ == "__main__":
    _check()
