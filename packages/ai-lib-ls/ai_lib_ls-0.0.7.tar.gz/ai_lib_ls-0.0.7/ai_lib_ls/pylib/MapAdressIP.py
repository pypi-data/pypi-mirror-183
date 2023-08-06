# -*- coding: utf-8 -*-
import pandas as pd
import requests

tasks = []


# 高德地图, 查询 ip 的具体地址 ,或者输入名称搜索经纬度
class MapAdressIPUtils:
    def __init__(self):

        self.GaoDeKey = '85d518322dbdd7bc39df891a52a3d4b5'  # 高德 key

        pass

    def getLacationAddress(self, keywords):  # 输入地址名称 返回经纬度
        '''
                "id":
                    "B0H0JSSUO2",
                "name":
                    "成都·三圣乡",
                "district":
                    "四川省成都市锦江区",
                "adcode":
                    "510104",
                "location":
                    "104.163395,30.583071",
                "address":
                    "花乡农居景区内水杉路332号(近天鹅湖)",
                "typecode":
                    "050100",

            '''
        params = {
            'key': self.GaoDeKey,
            'keywords': keywords,
            'output': 'json'
        }
        response = requests.get('https://restapi.amap.com/v3/assistant/inputtips', params=params)

        if response.status_code == 200:
            response = response.json()
            data = response.get('tips')
            # print(data, type(data))
            if len(data) > 0:
                if len(data[0].get('location'))>0:
                    print(data[0].get('location').split(','))

    def getIpAddress(self, ip):  # 输入地址名称 返回经纬度
        '''{'status': '1','info': 'OK', 'infocode': '10000', 'province': '浙江省', 'city': '嘉兴市', 'adcode': '330400',
        'rectangle': '120.6058502,30.61248612;120.9298825,30.86848863'}
        '''
        params = {
            'key': self.GaoDeKey,
            'ip': ip,
            'output': 'json'
        }
        response = requests.get('https://restapi.amap.com/v3/ip', params=params)

        print(response.json())
        return response.json()


if __name__ == '__main__':  # 222
    util = MapAdressIPUtils()
   # util.getIpAddress('122.231.250.116')
    util.getLacationAddress('成都三圣乡')

    pass
