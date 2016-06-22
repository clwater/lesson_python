#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字典 键值对
d = { 'a' : 1 , 'b' : 2 , 'c' : 3}
print d['a']
#通过in 判断是否在字典中
print 'v' in d
#get获取对应值,可以指定没有的情况下如何执行
print d.get('r' , -1)
#通过pop(key)的方法删除
d.pop('a')
print d

