import requests

url = 'http://hq.sinajs.cn/list=hk01810'

res = requests.get(url)

temp = res.text.split('=')[1][:-2][1:-1].split(',')

print("名称："+temp[0])
print("股票名称："+temp[1])
print("今日开盘价："+temp[2])
print("昨日收盘价："+temp[3])
print("最高价："+temp[4])
print("最低价："+temp[5])
print("现价："+temp[6])
print("涨跌："+temp[7])
print("涨幅："+temp[8])
print("买一："+temp[9])
print("卖一："+temp[10])
print("成交额："+temp[11])
print("成交量："+temp[12])
print("市盈率："+temp[13])
print("周息率："+temp[14])
print("52周最高："+temp[15])
print("52周最低："+temp[16])
print("日期："+temp[17])
print("时间："+temp[18])



