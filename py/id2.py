#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 2. В следующих заданиях требуется реализовать абстрактный базовый класс,
определив в нем абстрактные методы и свойства. Эти методы определяются в производных классах.
В базовых классах должны быть объявлены абстрактные методы ввода/вывода, которые реализуются
в производных классах.

Вызывающая программа должна продемонстрировать все варианты вызова переопределенных абстрактных
методов. Написать функцию вывода, получающую параметры базового класса по ссылке и демонстрирующую
виртуальный вызов.
Номер варианта необходимо получить у преподавателя.

Вариант 29(12) 12. Создать абстрактный базовый класс Integer (целое) с виртуальными арифметическими
операциями и функцией вывода на экран. Определить производные классы Decimal (десятичное) и Binary
(двоичное), реализующие собственные арифметические операции и функцию вывода на экран. Число представляется
массивом, каждый элемент которого — цифра.
"""
import decimal
from abc import ABC, abstractmethod


class Integer(ABC):
    @property
    @abstractmethod
    def number(self):
        return self._number

    @number.setter
    @abstractmethod
    def number(self, value):
        self._number = value

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def sub(self, other):
        pass

    @abstractmethod
    def mul(self, other):
        pass

    @abstractmethod
    def display(self):
        print("\nБазовый абстрактный класс Integer")

    @abstractmethod
    def input(self):
        pass


class Decimal(Integer):
    def __init__(self, value):
        self._number = decimal.Decimal(value)

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def add(self, other):
        # Реализация сложения для Decimal
        if isinstance(other, Decimal):
            return self.number + other.number
        else:
            raise ValueError()

    def sub(self, other):
        # Реализация вычитания для Decimal
        if isinstance(other, Decimal):
            return self.number - other.number
        else:
            raise ValueError()

    def mul(self, other):
        if isinstance(other, Decimal):
            return self.number * other.number
        else:
            raise ValueError()

    def display(self):
        # Реализация вывода на экран для Decimal
        print(f"Decimal: {self.number}")

    def input(self):
        self.number = decimal.Decimal(input("Введите десятичное (Decimal) число: "))


class Binary(Integer):
    def __init__(self, value):
        self._number = bin(value)[2:]

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = bin(value)[2:]

    def add(self, other):
        # Реализация сложения для Binary
        if isinstance(other, Binary):
            return bin(int(self.number, 2) + int(other.number, 2))[2:]
        else:
            raise ValueError()

    def sub(self, other):
        # Реализация вычитания для Binary
        if isinstance(other, Binary):
            return bin(int(self.number, 2) - int(other.number, 2))[2:]
        else:
            raise ValueError()

    def mul(self, other):
        # Реализация умножения для Binary
        if isinstance(other, Binary):
            return bin(int(self.number, 2) * int(other.number, 2))[2:]
        else:
            raise ValueError()

    def display(self):
        # Реализация вывода на экран для Binary
        print(f"Binary: {self.number}")

    def input(self):
        # Реализация ввода для Binary
        self._number = bin(int(input("Введите число для перевода в Binary: ")))[2:]


if __name__ == '__main__':
    print("Попытка создания экземпляра абстрактного класса:")
    try:
        int1 = Integer(4)
        int1.add(6)
    except:
        print("Err")

    print("\nКласс Decimal")
    dec1 = Decimal(10.23)
    dec2 = Decimal(5.52)
    print(f"Сложение: {dec1.add(dec2):.2f}")
    print(f"Вычитание: {dec1.sub(dec2):.2f}")
    print(f"Умножение: {dec1.mul(dec2):.2f}")
    dec1.display()
    dec2.display()
    print("Ввод")
    dec1.input()
    dec1.display()
    print("\nКласс Binary")
    bin1 = Binary(3)
    bin2 = Binary(2)
    print(f"Сложение: {bin1.add(bin2)}")
    print(f"Вычитание: {bin1.sub(bin2)}")
    print(f"Умножение: {bin1.mul(bin2)}")
    bin1.display()
    bin2.display()
    bin2.input()
    bin2.display()