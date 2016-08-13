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
from PIL import Image
import pytesseract
from docopt import docopt
from selenium.webdriver.support.select import Select
from selenium import webdriver


def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table


def getYzm():
    im = Image.open('./yzm.jpg')
    im = im.convert('L')
    binaryImage = im.point(initTable(), '1')
    yzm = pytesseract.image_to_string(binaryImage)
    return yzm


def checkinfo(lists):
    pd = True
    for list in lists:
        if(list == '健康教育选课学生' or list == '尔雅通识课选课学生' or list == '校内通识课选课学生' or list == '13软件1-6班'):
            pd = False
    return pd


def showSchedule(body):
    headers = '课程编号 课程名称 课序 学分 学时 任课教师 上课人数 上课时间 上课班级'.split()
    from prettytable import PrettyTable
    pt = PrettyTable()
    pt._set_field_names(headers)
    for tr in body:
        list = str(tr.text).split()
        if(checkinfo(list)):
            print(list)
            print('\n')
            pt.add_row([list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8]+list[9]+list[10]+list[11] , list[12]])

    print(pt)


def getSchedule():
    driver = webdriver.PhantomJS(executable_path="/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs")
    driver.get("http://cityjw.dlut.edu.cn:7001/ACTIONLOGON.APPPROCESS?mode=3")
    #driver.switch_to_frame('_Logon')
    driver.find_element_by_id('WebUserNO').send_keys('201312026')
    driver.find_element_by_id('Password').send_keys('221628')

    driver.save_screenshot('./all.jpg')
    imgelement = driver.find_element_by_xpath('//img[@src="ACTIONVALIDATERANDOMPICTURE.APPPROCESS"]')
    location = imgelement.location
    size = imgelement.size
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width'] + 10),
              int(location['y'] + size['height']) + 10)
    i = Image.open("./all.jpg")
    frame4 = i.crop(rangle)
    frame4.save('./yzm.jpg')
    yzm = getYzm()
    driver.find_element_by_name('Agnomen').send_keys(yzm)
    driver.find_element_by_name('submit').submit()
    driver.get('http://cityjw.dlut.edu.cn:7001/Main.jsp')

    driver.switch_to_frame(driver.find_element_by_name('BoardMenu'))
    driver.find_element_by_link_text('全校课表清单查询').click()
    time.sleep(3)
    driver.switch_to_default_content()
    driver.switch_to_frame(driver.find_element_by_name('mainFrame'))

    Select(driver.find_element_by_name('DeptNo')).select_by_value("001")
    Select(driver.find_element_by_name('MajorNo')).select_by_value("001002")
    Select(driver.find_element_by_name('YearTerm')).select_by_value("201620171")
    Select(driver.find_element_by_name('GradeYear')).select_by_value("2013")
    Select(driver.find_element_by_name('ClassNo')).select_by_value("13010202")

    driver.find_element_by_name('bt_Query').click()
    time.sleep(3)



    body = driver.find_elements_by_xpath('/html/body/table/tbody/tr/td/form/table[2]/tbody/tr')

    showSchedule(body)








def init():
    arguments = docopt(__doc__)
    getSchedule()


if __name__ == '__main__':
    init()

