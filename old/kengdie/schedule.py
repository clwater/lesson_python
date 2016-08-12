#!/usr/bin/env python3
# -*- coding: utf-8 -*-'
from urllib.request import urlretrieve

from PIL import Image
import pytesseract
from selenium import webdriver
import urllib
import pyocr




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
    # urllib.urlretrieve = urlretrieve('http://cityjw.dlut.edu.cn:7001/ACTIONVALIDATERANDOMPICTURE.APPPROCESS', './yanzhengma.jpg', reporthook=None, data=None)
    im = Image.open('./yanzhengma.jpg')
    im = im.convert('L')
    binaryImage = im.point(initTable(), '1')
    #binaryImage.show()


    print(pytesseract.image_to_string(binaryImage, lang='eng'))



def init():
    #arguments = docopt(__doc__)
    getschedule()



if __name__ == '__main__':
    init()