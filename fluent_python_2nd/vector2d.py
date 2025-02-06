"""
vector2d.py：一个简单的类，演示一些特殊方法

只是演示，一些问题做简化处理。缺少错误处理，尤其是__add__和__mul__方法。

本书后文还会扩充这个示例。

加法::

    >>> v1 = Vector(2, 4)
    >>> v2 = Vector(2, 1)
    >>> v1 + v2
    Vector(4, 5)

绝对值::

    >>> v = Vector(3, 4)
    >>> abs(v)
    5.0

标量积::

    >>> v * 3
    Vector(9, 12)
    >>> abs(v * 3)
    15.0
"""

import math

class Vector:
    """一个简单的二维向量"""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
