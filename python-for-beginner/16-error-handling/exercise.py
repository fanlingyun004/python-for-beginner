"""
Exercise 16: Error Handling (try / except)

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


def safe_int(text):
    """Convert text to int; return None instead of raising ValueError on failure."""
    # 中文翻译：将文本转换为整数；失败时返回 None，而不是抛出 ValueError。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def safe_divide(a, b):
    """Return a / b, or None if it raises ZeroDivisionError."""
    # 中文翻译：返回 a / b；发生 ZeroDivisionError 时返回 None。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def safe_get_item(items, index):
    """Return items[index], or None if it raises IndexError."""
    # 中文翻译：返回 items[index]；发生 IndexError 时返回 None。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def safe_get_value(d, key):
    """Return d[key], or "not found" if it raises KeyError."""
    # 中文翻译：返回 d[key]；发生 KeyError 时返回“not found”。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def validate_age(age):
    """Return age if age >= 0; otherwise raise ValueError("age cannot be negative")."""
    # 中文翻译：age 大于等于 0 时返回 age，否则抛出 ValueError。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    assert safe_int("42") == 42
    assert safe_int("abc") is None

    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None

    assert safe_get_item([1, 2, 3], 1) == 2
    assert safe_get_item([1, 2, 3], 10) is None

    assert safe_get_value({"a": 1}, "a") == 1
    assert safe_get_value({"a": 1}, "z") == "not found"

    assert validate_age(25) == 25
    try:
        validate_age(-5)
        assert False, "expected ValueError"
    except ValueError as e:
        assert str(e) == "age cannot be negative"

    print("All checks passed!")


if __name__ == "__main__":
    _check()
