#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module'

__author__ = 'gzb'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('hello')
    elif len(args==2):
        print('H, %s' % args[1])
    else:
        print('too')

if __name__ == '__main__':
    test()

