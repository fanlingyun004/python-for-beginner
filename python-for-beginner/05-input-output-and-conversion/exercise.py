"""
Exercise 05: Input, Output & Type Conversion

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def sum_from_text(a_text, b_text):
    """a_text/b_text are number-strings like "3". Convert to int and return their sum."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def average_from_text(a_text, b_text, c_text):
    """Three number-strings, e.g. "1", "2", "3". Convert to float and return their average."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def parse_yes_no(text):
    """Return True if text means "yes" (any case), False if it means "no"."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def format_line(label, value):
    """Return "<label>: <value>" — what print(label, value, sep=": ") would show."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert sum_from_text("3", "4") == 7
    assert isinstance(sum_from_text("3", "4"), int)
    assert sum_from_text("-2", "5") == 3

    assert average_from_text("1", "2", "3") == 2.0
    assert isinstance(average_from_text("1", "2", "3"), float)
    assert average_from_text("10", "20", "30") == 20.0

    assert parse_yes_no("yes") is True
    assert parse_yes_no("Yes") is True
    assert parse_yes_no("  YES  ") is True
    assert parse_yes_no("no") is False
    assert parse_yes_no("No") is False

    assert format_line("Age", 25) == "Age: 25"
    assert format_line("Name", "Ava") == "Name: Ava"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
