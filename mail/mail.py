#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

# /usr/bin/python
from urllib import request

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
import time



#'/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs'


# from selenium import webdriver
#
# url = "http://jira.haizhi.com/issues/?jql=assignee%20in%20(currentUser())"
# driver = webdriver.PhantomJS(executable_path='/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs')
# #executable_path为你的phantomjs可执行文件路径
# driver.get(url)
#
# #或得js变量的值
# r = driver.execute_script('')
# print (r)
#
#
# print (driver.find_element_by_id("jira").text)

#
# from selenium import webdriver
#
#
# url = 'http://mail.weibangong.com/?v=1470651451924#/dashboard/receive'
# url = 'http;//www.baidu.com'
# url = 'http://city.dlut.edu.cn/'
#
# driver = webdriver.PhantomJS(executable_path='/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs')
#
# print('1')
#
# driver.get(url)
# time.sleep(6)
#
# print (driver.page_source)
#
# print('2')



# 引入selenium中的webdriver
from selenium import webdriver
import time

# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
driver = webdriver.PhantomJS(executable_path="/Users/haizhi/Desktop/MyPythonShell/phantomjs-2.1.1-macosx/bin/phantomjs")

# 使用浏览器请求页面
driver.get("http://jira.haizhi.com/login.jsp?os_destination=%2Fsecure%2FDashboard.jspa")

print( driver.page_source)



