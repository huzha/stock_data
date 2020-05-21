import tushare as ts
import sqlite3
from sqlalchemy import create_engine

conn = sqlite3.connect('stock.db')

print("连接sqlite成功")

# df_hs300 = ts.get_hs300s()

df_sz50 = ts.get_sz50s()

engine = create_engine('sqlite:///stock.db', echo=True)

df_sz50.to_sql('sz_50', engine, if_exists='replace')

print(df_sz50)
