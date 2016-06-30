#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#变量可以指向函数
# f = abs
# print f(-10)

# def add(x, y, f):
# 	return f(x) + f(y)

# print add(-5 ,6 ,abs)

def f(x):
	return x * x

r = map(f , [1,2,3,4,5,6,7,8,9])
print list(r)



