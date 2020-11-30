#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input("Введите значение а"))
b = int(input("Введите значение b"))
c = int(input("Введите значение c"))

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    print("Среди чиселй есть четное")
else:
    print("Среди чисел нет четного")

