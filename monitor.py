import tushare as ts
import time
import requests

a_stock = ['000635']

h_stock = ['01810']


def get_a_stock():
    df = ts.get_realtime_quotes(a_stock)[['code', 'name', 'price', 'high', 'time']]
    return df


def get_h_stock():
    h_url = 'http://hq.sinajs.cn/list='
    h_stocks = ''
    for h in h_stock:
        h_stocks += 'hk' + h + ','
    response = requests.get(h_url + h_stocks)
    res_list = response.text.split('\n')
    return res_list


if __name__ == '__main__':
    while True:
        time.sleep(2)
        df = get_a_stock()
        res_list = get_h_stock()
        for index, row in df.iterrows():
            print(row['code'], row['name'], row['price'], row['high'], row['time'])
        # for res in res_list:
        #     if str(res).find('=') > 0:
        #         temp = res.split('=')[1][:-2][1:].split(',')
        #         print(h_stock[res_list.index(res)] + " " + temp[1] + " " + temp[6] + " " + temp[4] + " " + temp[18])
        print('--------------------------------------------')

