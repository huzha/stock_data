import tushare as ts
import time
import requests

a_stock = ['601111', '000635']

h_stock = '01810'
h_url = 'http://hq.sinajs.cn/list=hk'


def get_a_stock():
    df = ts.get_realtime_quotes(a_stock)[['code', 'name', 'price', 'high', 'time']]
    for index, row in df.iterrows():
        print(row['code'], row['name'], row['price'], row['high'], row['time'])


def get_h_stock():
    res = requests.get(h_url + h_stock)
    temp = res.text.split('=')[1][:-2][1:-1].split(',')
    print(h_stock + " " + temp[1] + " " + temp[6] + " " + temp[4] + " " + temp[18])


if __name__ == '__main__':
    while True:
        time.sleep(2)
        get_a_stock()
        get_h_stock()
        print('---------------------------------------')
