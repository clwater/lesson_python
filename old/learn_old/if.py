#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#if 注意条件后加: 自上至下 某个符合后则忽略后面的
# age = 20
# if age >= 6:
#     print('teenager')
# elif age >= 18:
#     print('adult')
# else:
#     print('kid')


# birth = input('birth: ')
# #通过int()将input得到的str类型转换为int类型
# birth = int(birth)
# if birth > 2000:
# 	print '00后'
# else :
# 	print '00前'


height = input('身高: ')
weight = input('体重: ')
height = float(height)
weight = float(weight)
bmi = weight / (height * height)
if bmi <=18.5:
	print '过轻'
elif bmi < 25:
	print '正常'
elif bmi < 28:
	print '过重'
elif bmi < 32:
	print '肥胖'
else:
	print '严重肥胖'
