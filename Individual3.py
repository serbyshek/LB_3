#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = 0
    for i in range(20, 100):
        a = i // 10
        b = i % 10
        if (a + b) % 3 == 0:
         n += i
    print( n , "сумма чисел кратных 3")
