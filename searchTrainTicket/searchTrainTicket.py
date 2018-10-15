#coding = utf-8

import json
import re
import requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from problem.train_stations import searchAllStation

class searchTrain():
    def __init__(self):
        self.trainOption = input('-d动车 -g高铁 -k快速 -t特快 -z直达,Please input the trainType you want to search :')
        self.fromStation = input('Please input the city you want leave :')
        self.toStation = input('Please input the city you will arrive :')
        self.tripDate = input('Please input the date(Example:2017-09-27) :')
        self.headers = {
            "Cookie":"tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; Expires=Tue, 08-May-2018 11:04:12 GMT; Path=/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
            }
        self.available_trains,self.options = self.searchTrain()

    @property
    def trains(self):
        for item in self.available_trains:
            cm = item.split('|')
            train_no = cm[3]
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                train_no,
                '\n'.join([Fore.GREEN + cm[6] + Fore.RESET, #Fore是掉颜色的方法，RESET--重置
                          Fore.RED + cm[7] + Fore.RESET]),
                '\n'.join([Fore.GREEN + cm[8] + Fore.RESET,
                          Fore.RED + cm[9] + Fore.RESET]),
                cm[10],
                cm[32],
                cm[25],
                cm[31],
                cm[30],
                cm[21],
                cm[23],
                cm[28],
                cm[24],
                cm[29],
                cm[26],
                cm[22]   ]
                yield train
                # return train --> yield生成值并不会终止程序运行，类似continue,而return返回值后程序将终止执行，类似break
    def pretty_print(self):
        pt = PrettyTable()
        header = '车次 车站 时间 历时 商务座 特等座 一等 二等 高级软卧 软卧 硬卧 软座 硬座 无座 其他'.split()
        pt._set_field_names(header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)

    def searchTrain(self):
        arguments = {
        'option':self.trainOption,
        'from':self.fromStation,
        'to':self.toStation,
        'date':self.tripDate
        }
        options = ''.join([item for item in arguments['option']])
        # from_station, to_station, date = sas.stations[arguments['from']] , sas.stations[arguments['to']] , arguments['date'] 直接写成一行看起来更美观

        # 两种调用方法--1.调用类，实例化对象去调用类属性，好处，分离函数，降低耦合程度
        sas = searchAllStation()
        print(sas.stations)
        date = arguments['date']
        from_station = sas.stations[arguments['from']]
        to_station = sas.stations[arguments['to']]

        # 2.调用函数方法
        # s = self.stations()
        # print(s)
        # from_station = s[arguments['from']]
        # to_station = s[arguments['to']]
        # date = arguments['date']


        url = ('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT').format(date,from_station,to_station)
        requests.packages.urllib3.disable_warnings()
        html = requests.get(url,headers = self.headers,verify=False)
        available_trains = html.json()['data']['result']
        return available_trains,options

if __name__ == '__main__':
    while True:
        asd = searchTrain()
        asd.pretty_print()