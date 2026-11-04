"""
Exercise 18: File I/O

Implement each function below. Run this file directly to self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。

import os
import tempfile
from pathlib import Path


def write_lines(path, lines):
    """Write each string in `lines` to the file at `path`, one per line ("w" mode)."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def read_lines(path):
    """Read the file at `path`; return a list of its lines with "\\n" stripped."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def append_line(path, line):
    """Add `line` as a new line at the END of the file at `path` ("a" mode)."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def count_lines(path):
    """Return how many lines are in the file at `path`."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def file_exists(path):
    """Return whether a file exists at `path`, using pathlib.Path."""
    # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
    # TODO: implement（待完成：实现此函数）
    raise NotImplementedError


def _check():
    tmp_dir = tempfile.mkdtemp()
    path = os.path.join(tmp_dir, "notes.txt")

    assert file_exists(path) is False

    write_lines(path, ["first", "second", "third"])
    assert file_exists(path) is True
    assert read_lines(path) == ["first", "second", "third"]
    assert count_lines(path) == 3

    append_line(path, "fourth")
    assert read_lines(path) == ["first", "second", "third", "fourth"]
    assert count_lines(path) == 4

    # "w" mode must overwrite, not append（“w”模式必须覆盖写入，而不是追加写入）
    write_lines(path, ["only line"])
    assert read_lines(path) == ["only line"]

    os.remove(path)
    os.rmdir(tmp_dir)

    print("All checks passed!")


if __name__ == "__main__":
    _check()
