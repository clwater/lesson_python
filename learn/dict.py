#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # #字典 键值对
# d = { 'a' : 1 , 'b' : 2 , 'c' : 3}
# print d['a']
# #通过in 判断是否在字典中
# print 'v' in d
# #get获取对应值,可以指定没有的情况下如何执行
# print d.get('r' , -1)
# #通过pop(key)的方法删除
# d.pop('a')
# print d
# d['d']=4
# print d




#set key的集合 不存储value 自动过滤重复
s = set([1,2,3,3,3,3,4])
print s
s.add(6)
print s
s.remove(3)
print s

#数集中的交并计算
s1 = set([1,2,3])
s2 = set([3,4])

print s1 & s2
print s1 | s2