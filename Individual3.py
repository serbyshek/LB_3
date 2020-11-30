#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = 0
for i in range(20, 100):
    a = i // 10
    b = i % 10
    if (a + b) % 3 == 0:
        n += i
    else:
        n += 0
print( n , "сумма чисел кратных 3")
