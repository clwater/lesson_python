#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# coding: utf-8

"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               高铁
    -d               动车
    -t               特快
    -k               快速
    -z               直达

Example:
    tickets 北京 大连 2016-07-01
    tickets -dg 北京 大连 2016-07-01
"""
import os

from docopt import docopt
from stations import stations
from prettytable import PrettyTable
from colorama import init,Fore
import requests , re  , time

def cli():
    """command-line interface"""

    arguments = docopt(__doc__)

    Status_gt = arguments.get('-g')
    Status_dc = arguments.get('-d')
    Status_tk = arguments.get('-t')
    Status_ks = arguments.get('-k')
    Status_zd = arguments.get('-z')

    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    date = arguments['<date>']
    date = checkdate(date)
    url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
         date, from_station, to_station)
    r = requests.get(url,verify=False)
   # print(r.json())

    rows = r.json()['data']['datas']
    init(autoreset=True)

    headers = '车次 车站 时间 历时 商务 特等 一等 二等 高软 软卧 硬卧 硬座 无座 其他'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)
    for row in rows:
        if check(Status_gt , Status_dc , Status_tk , Status_ks , Status_zd):
            addrow(row , pt)
        else :
            if Status_gt:
                if re.match('G',row['station_train_code']):
                    addrow(row , pt)
            if Status_dc:
                if re.match('D',row['station_train_code']):
                    addrow(row , pt)
            if Status_tk:
                if re.match('T',row['station_train_code']):
                    addrow(row , pt)
            if Status_ks:
                if re.match('K',row['station_train_code']):
                    addrow(row , pt)
            if Status_zd:
                if re.match('Z',row['station_train_code']):
                    addrow(row , pt)

    clear()
    print(Fore.YELLOW+'查询日期: '+ date)
    print(pt)


def addrow(row , pt):
    pt.add_row([row['station_train_code'], Fore.RED + row['from_station_name'] + Fore.RESET + '\n' + Fore.GREEN + row[
        'to_station_name'] + Fore.RESET,
                row['start_time'] + '\n' + row['arrive_time'], row['lishi'],
                row['swz_num'], row['tz_num'], row['zy_num'], row['ze_num'], row['gr_num'],
                row['rw_num'], row['yw_num'], row['yz_num'], row['wz_num'], row['qt_num']])

def check(*Status):
    for status in Status:
        if status == True:
            return False
    return True

def checkdate(date):
    try:
        if time.strptime(date, "%Y-%m-%d"):
            date = date
    finally:
        if len(date) == 8:
            temp = date
            date = temp[:4] +  '-'
            if (len(temp[5:6]) > 1) :
                date +=  str(temp[5:6])
            else:
                date += '0' + str(temp[5:6])
            date += '-'
            if (len(temp[-2:]) > 1) :
                date +=  str(temp[-2:])
            else:
                date += '0' + str(temp[-2:])
        return date

def clear():
    for i in range(2):
        print ('\n')


if __name__ == '__main__':
    cli()



