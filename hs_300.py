import tushare as ts
import redis
import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('stock.db')

print("连接sqlite成功")

df_hs300 = ts.get_hs300s()

# df_sz50 = ts.get_sz50s()

engine = create_engine('sqlite:///stock.db', echo=True)

df_hs300.to_sql('hs_300', engine, if_exists='append')

# df_zz500 = ts.get_zz500s()

# pool = redis.ConnectionPool(host='127.0.0.1', port='6379')

# r = redis.Redis(connection_pool=pool)

# for index, row in df_hs300.iterrows():
#     print(row['code'], row['name'])
#     r.set(row['code'], row['name'])

# for index, row in df_zz500.iterrows():
#     print(row['code'], row['name'])
#     r.set(row['code'], row['name'])
# if r.get(row['code']) is not None:
#     print(index, row['code'], row['name'])

# if r.get('600001') is not None:
#     print(r.get('600000').decode('utf8'))
# else:
#     print("没找到")

# print(df_sz50)
