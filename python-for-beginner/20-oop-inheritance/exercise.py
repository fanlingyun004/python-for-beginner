"""
Exercise 20: Inheritance & Dunder Methods

Implement the methods marked TODO below. Run this file directly to
self-check:
    python3 exercise.py
"""
# 中文翻译：本文件的练习说明和运行方式。


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        """Generic default sound; Dog and Cat override this."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        return "..."

    def __str__(self):
        """Return "<name> the <ClassName>", e.g. "Rex the Dog"."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError

    def __eq__(self, other):
        """True if other is the exact same class as self AND has the same name."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError


class Dog(Animal):
    def speak(self):
        """Return "<name> says Woof!"."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        """Return "<name> says Meow!"."""
        # 中文翻译：以上英文文档字符串用于说明对象的用途、输入和输出。
        # TODO: implement（待完成：实现此函数）
        raise NotImplementedError


def _check():
    generic = Animal("Generic")
    assert generic.speak() == "..."
    assert str(generic) == "Generic the Animal"

    rex = Dog("Rex")
    assert isinstance(rex, Dog)
    assert isinstance(rex, Animal)  # inheritance: a Dog IS an Animal（继承关系：Dog 是一种 Animal）
    assert rex.speak() == "Rex says Woof!"
    assert str(rex) == "Rex the Dog"

    whiskers = Cat("Whiskers")
    assert whiskers.speak() == "Whiskers says Meow!"
    assert str(whiskers) == "Whiskers the Cat"
    assert not isinstance(whiskers, Dog)

    assert rex == Dog("Rex")
    assert rex != Dog("Buddy")
    assert rex != Cat("Rex")  # same name, different class -> not equal（名称相同但类不同，因此不相等）

    print("All checks passed!")


if __name__ == "__main__":
    _check()
