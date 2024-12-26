import pandas as pd
stockavg = 200
name = 'AAPL';

import sys
stock = sys.argv[2]
stockavg = float(sys.argv[1])

csv = pd.read_csv(r'%s.csv' % stock)

data = csv
data.set_index ('date', inplace= True)
data.index = pd.to_datetime(data.index)

from stockstats import wrap

df = wrap(data)

import matplotlib.pyplot as plt
#plt.use('TkAgg')
df['svg'] = stockavg
df.svg.plot(color='blue', linestyle='--')
df['min'] = df.close[(df.close.shift(1) > df.close) & (df.close.shift(-1) > df.close)]
df['max'] = df.close[(df.close.shift(1) < df.close) & (df.close.shift(-1) < df.close)]
plt.scatter(df.index, df['min'], c='r')
plt.scatter(df.index, df['max'], c='g')
df.close.plot()

print(df) #'min', 'max'
print(df.describe())
df['close_avg'] = df['close'].mean()
print(df['close_avg'][0], df['high'].max(), df['low'].min())

from stockstats import StockDataFrame
stockStat = StockDataFrame.retype(df)
stockStat[['volume', 'change_rate', 'turnover_rate']].plot(grid=True, subplots=True)
plt.gcf().autofmt_xdate()
#plt.show()
plt.savefig(f'{stock}1.png')
p = stockStat[['close', 'close_5_sma', 'svg', 'close_avg']]
#print(p)
p.plot(figsize=(10,6), grid=True, subplots=False)
#plt.show()
plt.savefig(f'{stock}2.png')
stockStat[['volume', 'close','low']].plot(subplots=True, figsize=(10,6), grid=True)
#plt.show()
plt.savefig(f'{stock}3.png')
#https://github.com/dsxkline/dsxkline_python/blob/main/setup.py