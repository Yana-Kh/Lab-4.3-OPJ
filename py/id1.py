#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 1 Составить программу с использованием иерархии классов.
Номер варианта необходимо получить у преподавателя. В раздел программы,
начинающийся после инструкции if __name__ = '__main__': добавить код,
демонстрирующий возможности разработанных классов.

Вариант 29(9) 9. Создать класс Pair (пара чисел); определить методы изменения полей
и вычисления произведения чисел. Определить производный класс RightAngled с полями-катетами.
Определить методы вычисления гипотенузы и площади треугольника.
"""
import math


class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    def mul(self):
        return self._a * self._b


class RightAngled(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypotenuse(self):
        return math.sqrt(math.pow(self._a, 2) + math.pow(self._b, 2))

    def square(self):
        return self._a * self._b / 2


if __name__ == '__main__':
    # Родительский класс
    print("Родительский класс:")
    p1 = Pair(2, 10)
    print(f"a = {p1.a}, b = {p1.b}")
    print(f"Произведение = {p1.mul()}")
    p1.a = 12
    p1.b = 3
    print(f"a = {p1.a}, b = {p1.b}")
    print(f"Произведение = {p1.mul()}")

    # Дочерний класс
    print("\nДочерний класс:")
    p2 = RightAngled(3, 4)
    print(f"Катет 1 = {p2.a}, катет 2 = {p2.b}")
    print(f"Гипотенуза: {p2.hypotenuse():.2f}")
    print(f"Площадь: {p2.square():.2f}")


