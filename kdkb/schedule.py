#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

"""查看坑爹课表

Usage:
    shchedule

Options:
    -h,--help        显示帮助菜单

Example:
    shchedule

"""


import time
import urllib
from urllib.request import urlretrieve
from selenium import webdriver
from prettytable import PrettyTable
from docopt import docopt


def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

def getschedule():
    # driver = webdriver.PhantomJS(executable_path="/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs")
    # driver.get("http://cityjw.dlut.edu.cn:7001/ACTIONQUERYALLTABLELIST.APPPROCESS")
    # driver.find_element_by_id('WebUserNO').send_keys('201312026')
    # driver.find_element_by_id('Password').send_keys('221628')
    # urllib.urlretrieve = urlretrieve('http://cityjw.dlut.edu.cn:7001/ACTIONVALIDATERANDOMPICTURE.APPPROCESS', './yanzhengma/yanzhengma.jpg', reporthook=None, data=None)
    im = Image.open('./yanzhengma/yanzhengma.jpg')
    im = im.convert('L')
    binaryImage = im.point(initTable(), '1')
    #binaryImage.show()

    yanzhengma = pytesseract.image_to_string(binaryImage)
    print(yanzhengma)
  # print(pytesseract.image_to_string(binaryImage, config='-psm 7'))


def init():
    arguments = docopt(__doc__)
    getschedule()



if __name__ == '__main__':
    init()



    # driver.get("http://cityjw.dlut.edu.cn:7001/Main.jsp")
    # driver.switch_to_frame("BoardMenu");
    # #driver.find_element_by_name("outlookdivin0").click()
    # driver.find_element_by_link_text("全校课表清单查询").click()
    # # print(a.text)
    # time.sleep(3)
    # #print(driver.t)