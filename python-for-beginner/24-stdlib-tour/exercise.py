"""
Exercise 24: Standard Library Tour

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。

import json
from collections import Counter
from datetime import datetime


def days_between(date1_text, date2_text):
    """Parse two "YYYY-MM-DD" strings and return the absolute number of days between them."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using datetime.strptime（待完成：使用 datetime.strptime 实现）
    raise NotImplementedError


def format_pretty_date(year, month, day):
    """Return the date formatted as "Month DD, YYYY", e.g. "January 05, 2026"."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using datetime(...).strftime（待完成：使用 datetime(...).strftime 实现）
    raise NotImplementedError


def to_json(data):
    """Return `data` serialized as a JSON string."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using json.dumps（待完成：使用 json.dumps 实现）
    raise NotImplementedError


def from_json(text):
    """Return the Python value parsed from the JSON string `text`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using json.loads（待完成：使用 json.loads 实现）
    raise NotImplementedError


def most_common_word(words):
    """Return the single most common word in the list `words`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement using collections.Counter（待完成：使用 collections.Counter 实现）
    raise NotImplementedError


def _check():
    assert days_between("2026-01-01", "2026-01-15") == 14
    assert days_between("2026-01-15", "2026-01-01") == 14  # order-independent（与参数顺序无关）

    assert format_pretty_date(2026, 1, 5) == "January 05, 2026"
    assert format_pretty_date(2026, 12, 25) == "December 25, 2026"

    assert to_json({"a": 1}) == '{"a": 1}'
    assert to_json([1, 2, 3]) == "[1, 2, 3]"

    assert from_json('{"a": 1}') == {"a": 1}
    assert from_json("[1, 2, 3]") == [1, 2, 3]

    assert most_common_word(["a", "b", "a", "c", "b", "a"]) == "a"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
