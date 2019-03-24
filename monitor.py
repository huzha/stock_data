import tushare as ts
import time

my_stock = ['601111','000635']

while True:
    time.sleep(2)
    df = ts.get_realtime_quotes(my_stock)[['code', 'name', 'price', 'high', 'time']]
    for index, row in df.iterrows():
        print(row['code'], row['name'], row['price'], row['high'], row['time'])
    print('---------------------------------------')
