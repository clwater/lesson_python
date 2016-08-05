#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Plane tickets query via command-line.

Usage:
    plane [-g] <from> <to> <date>

Options:
    -h,--help        显示帮助菜单
    -g               啥


Example:
    tickets 北京 大连 2016-07-01
    tickets -g 北京 大连 2016-07-01
"""

from docopt import docopt

import requests


def ptc():
    """command-line interface"""

    arguments = docopt(__doc__)
    #print(arguments)

    from_station = arguments['<from>']
    to_station = arguments['<to>']
    date = arguments['<date>']

    url = 'http://flights.ctrip.com/booking/BJS-DLC-day-1.html?DDate1=2016-09-09'
  #  url = 'http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport={}&searchArrivalAirport={}&searchDepartureTime={}'.format(
   #      from_station, to_station, date)
    r = requests.get(url, verify=False)

    #print(r.url + '\n')
    print(r.text+ '\n')
    #print()





if __name__ == '__main__':
    ptc()


