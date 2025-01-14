#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('tradecheck.db')
print ("trade.db opened")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS COMPANY 
       (ID INTEGER PRIMARY KEY AUTOINCREMENT,
       CODE           TEXT     NOT NULL,
       BUY            REAL     NOT NULL,
       TIME           CHAR(20),
       SELL           REAL);''')
print ("trade.db created")
'''
c.execute("DELETE from COMPANY where ID=0;")
c.execute("DELETE from COMPANY where ID=1;")
conn.commit()
print ("trade.db deleted")

c.execute("INSERT INTO COMPANY (ID, CODE, BUY, TIME, SELL) \
      VALUES (1, 'ORCL', 165.3, '2025-01-07=>10:18:09', 170)")
conn.commit()
'''
c.execute("UPDATE COMPANY set BUY = 2.763 where ID=1")
c.execute("UPDATE COMPANY set CODE = '00558' where ID=1")
conn.commit()

cursor = c.execute("SELECT CODE, BUY, TIME, SELL from COMPANY")
for row in cursor:
   print( "CODE = ", row[0])
   print( "BUY = ", row[1])
   print( "TIME = ", row[2])
   print( "SELL = ", row[3], "\n")

print ("trade.db printed")

conn.close()

print ("trade.db closed")

import efinance as ef

#efinance.stock.get_quote_history(stock_codes: str | List[str], beg: str = '19000101', end: str = '20500101', klt: int = 101, fqt: int = 1, market_type: MarketType | None = None, suppress_error: bool = False, use_id_cache: bool = True, **kwargs) 

# write a boduan
stock_code = '00558'; stockavg = 2.9; zgs = 13.64# yi
st = '20250108'
#st = '20241210'
et  = '20250114'

from datetime import datetime
date1 = datetime.strptime(st, "%Y%m%d")
date2 = datetime.strptime(et, "%Y%m%d")

# Calculate the difference between the two dates
delta = date2 - date1

# Extract the number of days from the difference
number_of_days = delta.days

df = ef.stock.get_quote_history(stock_code, beg = st, end= et, klt = 101)
#left = df.tail(5).iloc[:, [1, 2,3]]
#print(left.to_markdown(numalign="left", stralign="left"))
#print(df.columns)
d = [0, 2, 4, 5, 6]


left = df.iloc[:, d]
#print(left.to_csv(index=False))
trade_of_days = left.shape[0]


#left = df.tail(days).iloc[:, d]
#s = (left.to_string())
#for i in s.split('\n'): print(i.split(' '))

#s = (left.to_string())
#for i in s.split('\n'): print(i.split(' '))
print (left)

m = left.iloc[:, 2].mean()
avg = m
#print ("avg close", avg)
print()

print ("max")
mx = (left.iloc[:, 3].max())
print(mx)
t = left.iloc[:, 3]==mx
print (left[t])
print()

print ("min")
mx = (left.iloc[:, 4].min())
print(mx)
t = left.iloc[:, 4]==mx
print (left[t])
print()

d = [0, 2, 7, 8, 11, 12]
left = df.iloc[:, d]

mx = (left.iloc[:, 2].max())
t = left.iloc[:, 2]==mx
#date = (left[t].iloc[:, 1].to_string(index=False))
print ("max trade")
print (left[t].iloc[:, [0, 1, 2, 4, 5]])
print()


print(f"days between {st} and {et}: {number_of_days}")
print(f"trade between {st} and {et}: {trade_of_days}")
m = left.iloc[:, 3] / left.iloc[:, 2]  
mm = m.mean()
print ("people vwmp:", mm)
mx = (m.min())
t = left.iloc[:, 3] / left.iloc[:, 2]  ==mx
#date = (left[t])
#date = (left[t].iloc[:, 1].to_string(index=False))
date = (left[t].iloc[:, [1, 4, 5]].to_string(index=False, header = None))
print ("buy at min vwmp?", date, "^ ^")

mx = (left.iloc[:, 2].max())
t = left.iloc[:, 2]==mx
#date = (left[t])
#date = (left[t].iloc[:, 1].to_string(index=False))
date = (left[t].iloc[:, [1, 4, 5]].to_string(index=False, header = None))
print ("sell at max turn?", date)
print (">>>> ma", avg, "\n>>>> me", stockavg)

dl = df["成交量"].to_list()
print ('总股数', zgs, '亿')
print ('一半是', zgs*100000000/10000*0.5, '万')
result = [x / 10000.0 for x in dl]
print ('成交量', result, '万')

l = len(result)+1
for i in range (1, l): 
    s = sum(result[0:i])
    print('累积量', s, '的1/3是主力', 1/3*s)
#print (sum(result))
# = left.iloc[:, 2].mean()


df["pvt"] = df["收盘"] * df["成交量"] 
df["vwap"] = df["pvt"].cumsum() / df["成交量"].cumsum()

#print(df[["涨跌额", "收盘", "vwap"]])
print("=>=> vwap min", df["vwap"].min())
qian = df.sort_values(by='涨跌额', ascending=False)
print ("=>=> avg up", qian["涨跌额"].mean())
print ("=>=> max up", qian["涨跌额"].max())

qt=(qian.tail(7)[['日期', '收盘', "涨跌额", "成交量", "vwap"]])
#['股票名称', '股票代码', '日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅','涨跌额', '换手率'],
s = (qt.to_csv())
print(s)
#for i in s.split('\n'): print(i.split(' '))
