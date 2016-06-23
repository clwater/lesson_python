#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#常见函数
#abs 
# print abs(-4)

# #max 可以多个参数
# print max(1,2,3)

# #数据类型转换
# print int('123')
# print int(123.456)
# print float(12)
# print str(1.123)
# print bool(1)
# print bool('')

# #可以使用'别名'
# a = abs
# print a(-1)

# #定义函数
# def shoumax(a,b):
# 	if a >= b :
# 		return a
# 	else :
# 		return b

# print shoumax(3,4)


# import math

# def move( x , y , step , angele = 0):
# 	nx = x + step * math.cos(angele)
# 	ny = y - step * math.sin(angele)
# 	return nx , ny

# x , y = move(100 ,100 ,60 , math.pi / 6)
# print x, y

# import math

# def quadratic(a, b ,c):
# 	r = b * b - 4 * a * c
# 	if r <= 0 :
# 		print 'error'
# 		return

# 	r = math.sqrt(r)
# 	return (-b + r) / 2 * a , (-b - r) / 2 * a

# print quadratic(1,3,-4)

# def jiecheng(x , n = 2):
# 	d = x
# 	while n > 1:
# 		x = x * d
# 		n = n - 1
# 	return x

# print jiecheng(5 , 3)

def cals(*numbers):
	sum = 0 
	for n in numbers:
		sum = sum + n * n
	return sum

print cals(1,2,3)

