#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#切片
#L = ['a' , 'b' , 'c' , 'd' ,'e']

#print L[1:4]

# L = list(range(100))

# print L[10:20]

# print L[-10:]

# print L[::5]

# print 'asdfghsjkxcvnnv'[:6]
# print 'asdfghsjkxcvnnv'[::2]

#迭代
# from collections import Iterable
# print isinstance('abc', Iterable)

# for i , value in enumerate(['a','b','c'],1):
# 	print (i,value)


#列表生成器
# L1 =[x * x for x in range(1,11) if x % 2 == 0]
# L2 = [m + n for m in 'ABC' for n in 'XYZ']

# import os
# L3 = [d for d in os.listdir('.')]

# d = {'x': 'A', 'y': 'B', 'z': 'C' }
# L4 = [k + '=' + v for k , v in d.items()]

# L5 = ['Hello', 'World', 'IBM', 'Apple']
# L6 = [s.lower() for s in L5]

# print L6

#生成器
#g = (x * x for x in xrange(1,10))

# print g
# for x in xrange(1,10):
# 	print next(g)

#print '----------------------'
#for x in g:
#	print x

# def fib(max):
# 	n , a, b = 0 , 1 , 1
# 	while n < max:
# 		print a
# 		a , b = b , a + b
# 		n = n + 1
# 	return 'done'

#fib(6)



# def fib2(max):
# 	n , a , b = 0 , 1 ,1
# 	while  n < max:
# 		yield a 
# 		a , b = b , a + b
# 		n = n + 1
# 	return 

# f = fib2(6)
# for n in f:
# 	print(n)

# f = fib2(10)

# for x in f:
# 	print next(f)


# def odd():
# 	print 's1'
# 	yield 1
# 	print 's2'
# 	yield 3
# 	print 's3'
# 	yield 5

# o = odd()
# print next(o)
# print next(o)
# print next(o)
# print next(o)













