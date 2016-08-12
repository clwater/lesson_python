#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#     self.name = name
#     self.score = score

# class Student(object):
#
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def pr(self):
#         print('%s : %s' % (self.__name , self.__score) )
#
#
# list1 = Student('aa', 59)
# list2 = Student('bb' ,61)
# list1.pr()
# list2.pr()
#
# print(list1.__name)

# class Father(object):
#     def run(self):
#         print('Father is running...')
#
# class Child(Father):
#     def run(self):
#         print('Child is running...')
#
# father = Father()
# father.run()
# child = Child()
# child.run()


# print(type(None))

class Student(object):
    test = 'Student'
    def __init__(self,name):
        self.name = name

s = Student('Bob')
print(s.test)