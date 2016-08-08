#!/usr/bin/env python3
# -*- coding: utf-8 -*-'



import os,subprocess
media_path="/Users/haizhi/Desktop/lesson_python/kebiao/shengyin.wav"



import pygame,sys,time


def shouvoice():

    n = 0
    pygame.init()
    pygame.mixer.init()
    pygame.time.delay(1000)
    soundwav=pygame.mixer.Sound("shengyin.wav")
    soundwav.play()

    while n < 5:
        time.sleep(1)
        soundwav.play()
        n = n + 1


shouvoice()