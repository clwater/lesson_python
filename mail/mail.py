#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

"""查看Bug和Bug提醒

Usage:
    mail [-l]

Options:
    -h,--help        显示帮助菜单
    -l               显示bug列表

Example:
    mail
    mial -l
"""

from selenium import webdriver
from prettytable import PrettyTable
from docopt import docopt
import pygame,time


def show():
    n = 0
    pygame.init()
    pygame.mixer.init()
    pygame.time.delay(1000)
    soundwav = pygame.mixer.Sound("shengyin.wav")
    soundwav.play()
    while n < 2:
        time.sleep(1)
        soundwav.play()
        n = n + 1

    #showwarning("Bug来了=-=  ", "改bug去吧")


def mail():
    """command-line interface"""
    arguments = docopt(__doc__)
    status_l = arguments.get('-l')
    while True:
        getstatus(status_l)
        time.sleep(300)

def getstatus(status_l):
    driver = webdriver.PhantomJS(executable_path="/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs")
    driver.get("http://jira.haizhi.com/login.jsp")
    driver.find_element_by_id('login-form-username').send_keys('gengzhibo')
    driver.find_element_by_id('login-form-password').send_keys('haizhi1234')
    driver.find_element_by_id('login-form-submit').submit()
    driver.get("http://jira.haizhi.com/issues/?jql=assignee%20in%20(currentUser())")
    text = driver.find_element_by_id('issuetable').text


    text = text.replace('\n' , ' ')
    text = text.replace('CLONE - ' , '')
    list = text.split(' ')

    headers = '关键字 主题 经办人 报告人 状态 解决结果 创建日期'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)

    size = int((len(list) - 9 ) / 7 - 1)
    list = list[9:]
    for i in range(0 , size):
        pt.add_row([list[ i * 7 ] , list[ i * 7 + 1] , list[ i * 7 + 2] , list[ i * 7 + 3] , list[ i * 7 + 4] , list[ i * 7 + 5] , list[ i * 7 + 6]])
        if(list[ i * 7 + 4] == '开始' or list[ i * 7 + 4] == 'Reopene'):
            show()

    if(status_l):
        print(pt)

mail()





