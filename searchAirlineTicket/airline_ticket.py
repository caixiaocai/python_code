# coding = utf-8

import re,os,json,requests
from docopt import docopt
from prettytable import PrettyTable
from colorama import init,Fore
from problem.air_stations import stations

fromCity = input('please input the city you want to leave:')
toCity = input('please input the city you want to arrive:')
tripDate = input('please input the data you want to(example:2018-05-27):')

# init() 把所调用的颜色方法都初始化了
class TrainsCollection():
    header = '航空公司 航班 机场 时间 机票价格 机场建设费'.split()
    def __init__(self, airline_tickets):
        self.airline_tickets = airline_tickets

    @property
    def Plains(self):
        # 航空公司的总表没有找到，但是常见航空公司也不是很多就暂时用这个dict{air_company}来收集！
        # 如果strs没有查询成功，则会返回一个KeyError，表示此dict中未找到目标航空公司，则会用其英文代码显示！
        air_company = {"G5": "华夏航空", "9C": "春秋航空", "MU": "东方航空", "NS": "河北航空", "HU": "海南航空", "HO": "吉祥航空", "CZ": "南方航空",\
                       "FM": "上海航空", "ZH": "深圳航空", "MF": "厦门航空", "CA": "中国国航", "KN": "中国联航"}

        for item in self.airline_tickets:
            try:
                strs = air_company[item['alc']]
            except KeyError:
                strs = item['alc']
            airline_data = [
            Fore.BLUE + strs + Fore.RESET,
            Fore.BLUE + item['fn'] + Fore.RESET,
            '\n'.join([Fore.YELLOW + item['dpbn'] + Fore.RESET,
                    Fore.CYAN + item['apbn'] + Fore.RESET]),
            '\n'.join([Fore.YELLOW + item['dt'] + Fore.RESET,
                    Fore.CYAN + item['at'] + Fore.RESET]),
            item['lp'],
            item['tax'],
            ]
            yield airline_data

    def pretty_print(self):
        # PrettyTable（）用于在屏幕上将查询到的航班信息表逐行打印到终端
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for airline_data in self.Plains:
            pt.add_row(airline_data)
        print(pt)

def doit():
    headers = {
        "Cookie":"tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; Expires=Tue, 08-May-2018 11:04:12 GMT; Path=/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    }
    arguments = {
        'from': fromCity,
        'to': toCity,
        'date': tripDate
    }
    DCity1 = stations[arguments['from']]
    ACity1 = stations[arguments['to']]
    DDate1 = arguments['date']
    url = (
        "http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1={}&ACity1={}&SearchType=S&DDate1={}").format(
        DCity1, ACity1, DDate1)
    try:
        r = requests.get(url, headers=headers, verify=False)
    except Exception as e:
        print(repr(e))
    print(url)
    airline_tickets = r.json()['fis']
    TrainsCollection(airline_tickets).pretty_print()

if __name__ == '__main__':
    doit()
