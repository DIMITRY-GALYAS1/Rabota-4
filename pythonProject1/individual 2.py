#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    q = ()
    otv = ()

    n = int(input("Введите год: "))
    n = (n - 1984) % 60 + 1
    color = (n-1) % 10 + 1
    color = (color - 1) // 2 + 1
    animal = (n - 1) % 12 + 1
    if animal == 1:
        otv = "ой Мыши"
    elif animal == 2:
        otv = "ой Коровы"
    elif animal == 3:
        otv = "ого Тигра"
    elif animal == 4:
        otv = "ого Зайца"
    elif animal == 5:
        otv = "ого Дракона"
    elif animal == 6:
        otv = "ой Змеи"
    elif animal == 7:
        otv = "ой Лошади"
    elif animal == 8:
        otv = "ой Овцы"
    elif animal == 9:
        otv = "ой Обезьяны"
    elif animal == 10:
        otv = "ой Курицы"
    elif animal == 11:
        otv = "ой Собаки"
    elif animal == 12:
        otv = "ой Свиньи"
    else:
        print("Ошибка!", file=sys.stderr)

    if color == 1:
        q = "Зелен"
    elif color == 2:
        q = "Красн"
    elif color == 3:
        q = "Желт"
    elif color == 4:
        q = "Бел"
    elif color == 5:
        q = "Черн"
    else:
        print("Ошибка!", file=sys.stderr)

    print("Год", q+otv)
