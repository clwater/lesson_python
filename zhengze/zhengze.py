#!/usr/bin/env python3
# -*- coding: utf-8 -*-'

import re


# reip = re.compile(r'(?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d])')
#
# for ip in reip.findall('192.168.0.1 192.168.0.1'):
#     print ("ip>>>", ip)


# text = 'Hello, my name is gzb. Please visit my website at http://www.my.com/.'
# revalue = re.compile('gzb')
# for i in revalue.findall(text):
#     print(i)




# text = 'sales1.xls' \
#        'orders3.xls ' \
#        'sales2.xls ' \
#        'sales1.xls ' \
#        'apac1,xls ' \
#        'europe2.xls ' \
#        'na1.xls ' \
#        'na2.xls ' \
#        'sa1.xls ' \
#        'ca1.xls ' \
#        'sas.xls '

# revalue = re.compile('[ns]a[0-9]\.xls')
# for i in revalue.findall(text):
#     print(i)

# revalue = re.compile('[ns]a[^0-9]\.xls')
# for i in revalue.findall(text):
#     print(i)

# text = '<color name="probation_dialog_background">#FFFFFF</color><color name="probation_textview_shap">#CCCCCC</color>'
#
# revalue = re.compile('#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]')
# for i in revalue.findall(text):
#     print(i)


text = 'my[0] my[1] my[21]'
revalues = re.compile('my\[[\d]+\]')
for i in revalues.findall(text):
    print(i)

