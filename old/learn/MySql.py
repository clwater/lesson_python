#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#
# conn =mysql.connector.connector(user='root' , password='' , database='pythontest')
# cursor =conn,cursor()

import pymysql

conn = pymysql.connect(user='root' , password='' , database='pythontest' ,  )
cur = conn.cursor()

# cur.execute('insert  into test values(\'7\')')
# conn.commit()

cur.execute('select * from test')

for r in cur:
    print('number:' + str(cur.rownumber))
    print('id: ' + str(r[0]))
cur.close()
conn.close()