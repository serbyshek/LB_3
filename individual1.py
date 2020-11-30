#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input("Сколько вам лет? "))
if n < 100:
    print("Вы ввели некорректное число!")
elif n % 10 == 1:
    print("Мне", n, "год")
elif n % 10 == 0 or n % 10 <= 5:
    print("Мне", n, "года")
else:
    print("Мне", n, "лет")