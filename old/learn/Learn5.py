#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print(abs(-1))
#
# print(max(1,2,-1))
#
# print(hex(10))

# def my_abs(x):
#     if x > 0 :
#         return x
#     else :
#         return -x
#         pass
#
# print(my_abs(-4))

# import math
# def move(x , y ,step , angle = 0):
#     nx = x + step * math.cos(angle)
#     ny = x + step * math.sin(angle)
#     return nx , ny
# r = move(100 , 100 , 60 , math.pi / 6)
# print(r)

def power(x , n = 2):
    s = 1
    while n > 0 :
        n = n -1
        s = s * x
    return s
print(power(5))