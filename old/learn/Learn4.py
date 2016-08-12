#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# age = 3
# if age > 18:
#     print('age: ' , age)
#     print('adilt')
# else:
#     print('age: ' , age)
#     print('teenager')

# birth = input('birth:')
# birth = int(birth)
# if birth < 2000:
#     print('qian')
# else:
#     print('hou')

# high = input('enter high')
# high = float(high)
# weight = input('enter weight')
# weight = int(weight)
#
# bmi = weight / (high * high)
# print(bmi)

# names = ['1' , '2' , '3']
# for name in names:
#     print(name)

# sum = 0 ;
# for x in range(101):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)


# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#     print('hello: ' , x)

d = {'a' : 1 , 'b' : 2 , 'c' : 3}
print(d['a'])

d['d'] = 4
print(d)

print('a' in d)
print('3' in d)

print(d.get('a'))
print(d.get('e') , -1)


print(d)

d.pop('a')
print(d)


s = set([1,1,1,1,2])
print(s)