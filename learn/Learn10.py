#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import os
#
# print(os.uname())
#
# print(os.path.abspath('.'))

# import json
#
# d = dict(name='Bob' , age = 10 , score = 88)
#
# print(json.dumps(d))
#
# print(json.loads(json.dumps(d)))

import time , threading

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5 :
        n = n + 1
        print('th read %s >>> %s' % (threading.current_thread().name , n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop , name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)