"""
Exercise 19: OOP Basics (Classes & Objects)

Implement the BankAccount class below. Run this file directly to
self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


class BankAccount:
    def __init__(self, owner, balance=0):
        """Store owner and balance as instance attributes."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError

    def deposit(self, amount):
        """Add amount to self.balance."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError

    def withdraw(self, amount):
        """Subtract amount from self.balance; raise ValueError if amount > balance."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError

    def get_balance(self):
        """Return the current balance."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError


def _check():
    account = BankAccount("Ava", 100)
    assert account.owner == "Ava"
    assert account.get_balance() == 100

    account.deposit(50)
    assert account.get_balance() == 150

    account.withdraw(30)
    assert account.get_balance() == 120

    try:
        account.withdraw(1000)
        assert False, "expected ValueError"
    except ValueError as e:
        assert str(e) == "insufficient funds"
    assert account.get_balance() == 120  # unchanged after failed withdrawal（取款失败后余额保持不变）

    # instances are independent（各个实例彼此独立）
    other = BankAccount("Sam")  # default balance（默认余额）
    assert other.get_balance() == 0
    other.deposit(10)
    assert other.get_balance() == 10
    assert account.get_balance() == 120  # unaffected by `other`（中文说明：unaffected by `other`）

    print("All checks passed!")


if __name__ == "__main__":
    _check()
