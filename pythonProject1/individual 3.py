#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите число: "))

    if 0 < n < 32:
        print(n, "Января")
    elif 32 < n < 60:
        g = n - 31
        print(g, "Февраля")
    elif 60 < n < 91:
        g = n - 59
        print(g, "Марта")
    elif 91 < n < 121:
        g = n - 90
        print(g, "Апреля")
    elif 121 < n < 152:
        g = n - 120
        print(g, "Мая")
    elif 152 < n < 182:
        g = n - 151
        print(g, "Июня")
    elif 182 < n < 213:
        g = n - 181
        print(g, "Июля")
    elif 213 < n < 244:
        g = n - 212
        print(g, "Августа")
    elif 244 < n < 274:
        g = n - 243
        print(g, "Сентября")
    elif 274 < n < 305:
        g = n - 273
        print(g, "Октября")
    elif 305 < n < 335:
        g = n - 304
        print(g, "Ноября")
    elif 335 < n < 366:
        g = n - 334
        print(g, "Декабря")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
