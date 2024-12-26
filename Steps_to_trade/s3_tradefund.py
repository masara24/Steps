import argparse

parser = argparse.ArgumentParser(description="How to make trade safe? [README.md]")

parser.add_argument("price", nargs='?', type=float, help="What is the current price?")
parser.add_argument("code", nargs='?', default="cost", help="What is the wanted code?")
parser.add_argument("-p", "--parameter", default="latest", help="What are the parameters?")
parser.add_argument("-v", "--verbose", action='store_true', help="How does the price come?")
parser.add_argument("-f", "--fee", help="How much fee are waste?")
parser.add_argument("-s", "--safe", action='store_true', help="What stratergy is safe?")

args = parser.parse_args()

def sell(price):
    #ratio = 0.05
    result = [price*0.90, price, price*1.05]
    if args.verbose: #print("ratio:", ratio)
        print("""do put from price %f to %f
do call from price %f to %f
or do trade by other options:[gann, elliot, benefit, gold]""" % (result[1], result[2], result[1], result[0])
)
    else: print("trade by 10 %:", result)

def gold(price):
    ratio = [0.5, 0.328,  0.618, 1]
    #ratiodown = [0.5, 0.618, 0.328]
    result = []
    result.append(price)
    ten = 1 * 100
    if 0.1 < price < 1: ten = 1 * 1
    if 1 < price < 10: ten = 1 * 10
    #if price < 0.1 or price > 1000: pass
    price = price * (1+ratio[0]/ten)
    result.append(price)
    price = price * (1-ratio[1]/ten)
    result.append(price)
    price = price * (1+ratio[2]/ten)
    result.append(price)
    price = price * (1-ratio[3]/ten)
    result.append(price)
    if args.verbose: print(list(zip(ratio, result)))
    else: print("trade by gold:", sorted(result[::2]))

def benefit(price):
    ratio = [-0.9, -0.5, -0.3, 0, 0.05, 0.1, 0.4, 0.7, 0.9, 1.15, 1.2, 2]
    priced = map(lambda x: (1+x) * price, ratio)
    result = list(priced)
    if args.verbose: print(list(zip(ratio, result)))
    else: print("trade by benefit:", (result[2:5]))




def get_gann(price):
# support and resistence
# sample: 19775.385009982252, 19810.556879991123, 19845.76, 19880.99437000887, 19916.259990017745
    root = price ** 0.5
    result = []
    for i in range(0, 405, 45): result.append((root - (i/360)) ** 2)
    result = (result[::-1])
    for i in range(45, 405, 45): result.append((root + (i/360)) ** 2)
    if args.verbose: print(list(zip(range(-360, 405, 45), result)))
        #print(result)
    else: print("trade by gann:", result[7:10])

def get_elliot(price):
# wave 1 and 2
# sample: 90, 92, 91, 96, 94, 100, 97.5, 98.5, 95
    result = []
    result.append(price)
    import random

    ratio = random.uniform(0.005, 0.08)
    ratio = ratio*random.choice([-1, 1])
    change = price*ratio
    dest = (price+change)   
    #print(ratio)
    if ratio > 0:
        wave = price+change*random.choice([-0.5, -0.618])
        result.append(wave)
        wave = price+change*random.choice([0.618, 1, 2.618])
        result.append(wave)
        wave = price+price*0.318
        result.append(wave) #4
        wave = price+change*random.choice([0.5, 0.618])
        result.append(wave)  #5
        wave = wave-change*random.choice([0.5, 0.618])
        result.append(wave)  #a
        wave =wave+change*random.choice([0.382, 0.5, 0.618])
        result.append(wave)  #b
        wave = wave-change*random.choice([0.5, 0.618, 1, 1.382, 1.618])
        result.append(wave)  #c
    else:
        wave = price+change*random.choice([-0.5, -0.618])
        result.append(wave)
        wave = price+change*random.choice([0.618, 1, 2.618])
        result.append(wave)
        wave = price+price*0.318
        result.append(wave) #4
        wave = price-change*random.choice([0.5, 0.618])
        result.append(wave)  #5
        wave = wave+change*random.choice([0.5, 0.618])
        result.append(wave)  #a
        wave =wave+change*random.choice([0.382, 0.5, 0.618])
        result.append(wave)  #b
        wave = wave+change*random.choice([0.5, 0.618, 1, 1.382, 1.618])
        result.append(wave)  #c
    if args.verbose: print(list(zip(["1","2","3","4","5","a","b","c"], result)))

        #print("from", price, "to", dest, result)
    else: print("trade by elliot:", result)


def get_stock(name):
    import efinance as ef
    s = ef.stock.get_latest_quote(name, suppress_error=True).to_string(index=False)
    s_list = s.split()
    #print(s_list)
    indices = [20, -1, 24, 31, 22]
    new_list = [s_list[index] for index in indices]
    #new_list[-1] = '+'+new_list[-1]+'%' if float(new_list[-1]) > 0 else new_list[-1]+'%'
    print(new_list[0], "latest price:", new_list[1:3])

def get_minutes(name):
    import efinance as ef
    s = ef.stock.get_quote_history(name, klt=1)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices])
    s_list = dfs.values.tolist()
   
    print(s_list)

def get_fdays(name):
    import efinance as ef
    s = ef.stock.get_quote_history(name, klt=101)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(5)
    s_list = dfs.values.tolist()
   
    print("5days close price", s_list)

def get_tdays(name):
    import efinance as ef
    s = ef.stock.get_quote_history(name, klt=101)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(10)
    s_list = dfs.values.tolist()
   
    print("10days close price", s_list)

def get_mdays(name):
    import efinance as ef

    s = ef.stock.get_quote_history(name, klt=101)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(30)
    s_list = dfs.values.tolist()
   
    print("30days close price", s_list)

def payus(qty, prc):
    import math

    pos = abs(qty)
    a = pos * 0.0049 if pos * 0.0049 >= 0.99 else 0.99
    a = a if a <= pos * prc * 0.5 * 0.01 else pos * prc * 0.5 * 0.01
    b = pos * 0.005 if pos * 0.005 >= 1 else 1
    b = b if b <= pos * prc * 0.5 * 0.01 else pos * prc * 0.5 * 0.01
    c = 0.003 * pos
    d = 0
    e = 0
    if qty < 0:
        d = 0.0000278 * prc * pos; d = 0.01 if d <= 0.01 else d; e = 0.000166 * pos; e = 8.3 if d >= 8.3 else d; e = 0.01 if d <= 0.01 else d
    fee = a + b + c + d + e
    #print("US", a, b, c, d, e)

    fee = math.ceil(fee * 100) / 100
    return fee


def payhk(qty, prc):
    import math

    pos = abs(qty *prc)

    a = pos * 0.03 * 0.01 if pos * 0.03 * 0.01 >= 3 else 3
    b = 15
    c = 0.002 * 0.01 * pos
    c = c if c >= 2 else 2
    c = c if c <= 100 else 100
    d = math.ceil(0.1 * 0.01 * pos)
    e = 0.00565 * 0.01 * pos if 0.00565 * 0.01 * pos >= 0.01 else 0.01
    f = 0.0027 * 0.01 * pos if 0.0027 * 0.01 * pos >= 0.01 else 0.01
    g = 0.00015 * 0.01 * pos
    fee = a + b + c + d + e + f + g
    #print("HK", a, b, c, d, e, f, g)
    fee = math.ceil(fee * 100) / 100
    return fee

def payhketf(qty, prc):
    import math

    pos = abs(qty * prc)

    a = pos * 0.03 * 0.01 if pos * 0.03 * 0.01 >= 3 else 3
    b = 15
    c = 0.002 * 0.01 * pos
    c = c if c >= 2 else 2
    c = c if c <= 100 else 100
    d = 0#math.ceil(0.1 * 0.01 * pos)
    e = 0.00565 * 0.01 * pos if 0.00565 * 0.01 * pos >= 0.01 else 0.01
    f = 0.0027 * 0.01 * pos if 0.0027 * 0.01 * pos >= 0.01 else 0.01
    g = 0.00015 * 0.01 * pos
    fee = a + b + c + d + e + f + g
    #print("HK", a, b, c, d, e, f, g)
    fee = math.ceil(fee * 100) / 100
    return fee

def paymkt(mkt, qty, prc):
    if mkt == 1: return payus(qty, prc)
    elif mkt == 2: return payhk(qty, prc)
    elif mkt == 3: return payhketf(qty, prc)
    else: return 0

def get_fee(price, qty):
    #qty = [100, 1000, 10000, 100000]
    qty = int(qty)
    result = [paymkt(1, qty, price), paymkt(2, qty, price), paymkt(3, qty, price)]
    print("trade", qty, "fee:", result)

    if args.verbose: 
        print("trade 10to100000 fee for price", price)
        print(10, list(zip(["US", "HK", "HKETF"], [paymkt(1, 10, price), paymkt(2, 10, price), paymkt(3, 10, price)])))
        print(100, list(zip(["US", "HK", "HKETF"], [paymkt(1, 100, price), paymkt(2, 100, price), paymkt(3, 100, price)])))
        print(1000, list(zip(["US", "HK", "HKETF"], [paymkt(1, 1000, price), paymkt(2, 1000, price), paymkt(3, 1000, price)])))
        print(10000, list(zip(["US", "HK", "HKETF"], [paymkt(1, 10000, price), paymkt(2, 10000, price), paymkt(3, 10000, price)])))
        print(100000, list(zip(["US", "HK", "HKETF"], [paymkt(1, 100000, price), paymkt(2, 100000, price), paymkt(3, 100000, price)])))


def get_qdays(name):
    import efinance as ef

    s = ef.stock.get_quote_history(name, klt=101)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(30)
    s_list = dfs.values.tolist()
   
    print("90days close price", s_list)

def get_month(name):
    import efinance as ef

    s = ef.stock.get_quote_history(name, klt=103)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(30)
    s_list = dfs.values.tolist()
   
    print("month close price", s_list)

def get_halfyear(name):
    import efinance as ef

    s = ef.stock.get_quote_history(name, klt=105)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(30)
    s_list = dfs.values.tolist()
   
    print("half year close price", s_list)

def get_year(name):
    import efinance as ef

    s = ef.stock.get_quote_history(name, klt=106)
    #indices = [2, 3, 4, 5, 6, 7, 11]
    indices = [2, 6]

    dfs = (s.iloc[:, indices]).tail(30)
    s_list = dfs.values.tolist()
   
    print("year close price", s_list)

def get_to(name, days, verbose):
    day=days.split('to')
    #if verbose: print("split the time", day)
    import efinance as ef
    st = day[0].replace('-', '')
    et = day[1].replace('-', '')
    s_list = []
    if len(st) == 8: 
        s = ef.stock.get_quote_history(name, st, et, klt=101, suppress_error=True)
    #indices = [2, 3, 4, 5, 6, 7, 11]
        indices = [2, 6]

        dfs = (s.iloc[:, indices])
        s_list = dfs.values.tolist()
    elif len(st) == 6: 
        st = st + "01"
        et = et + "01"
        s = ef.stock.get_quote_history(name, st, et, klt=103, suppress_error=True)
    #indices = [2, 3, 4, 5, 6, 7, 11]
        indices = [2, 6]

        dfs = (s.iloc[:, indices])
        s_list = dfs.values.tolist()
    elif len(st) == 13: 
        #print(st[-5:])
        print("UTC-8")
        s = ef.stock.get_quote_history(name, st, et, klt=1, suppress_error=True)
    #indices = [2, 3, 4, 5, 6, 7, 11]
        indices = [2, 6]

        dfs = (s.iloc[:, indices])
        s_list = dfs.values.tolist()

    print(days.replace("to", " "), "close price", s_list)
    
def get_avg(name, days, verbose):
    #if verbose: print("split the time", day)
    import efinance as ef
    day=days[:-3]

    if "day" in day: 

        s = ef.stock.get_quote_history(name, klt=101)
        indices = [2, 3, 4, 5, 6, 7, 8]
    #indices = [2, 6]
        d = int(day.split("day")[0])
        dfs = (s.iloc[:, indices]).tail(d)
        #print(dfs.columns)
        dfs.columns.values[[0, 1, 2, 3, 4, 5, 6]] = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount']
        s_list = dfs.values.tolist()
        if verbose: print(day, "ohlc and volume", s_list)
        print(day, "close avg", dfs['close'].mean())

        print(day, "vwmp avg", (dfs['amount']/dfs['volume']).mean())

    if "to" in day: 

        d=day.split('to')
        #if verbose: print("split the time", day)
        st = d[0].replace('-', '')
        et = d[1].replace('-', '')
        s_list = []
        s = ef.stock.get_quote_history(name, st, et, klt=101, suppress_error=True)
        indices = [2, 3, 4, 5, 6, 7, 8]

        dfs = (s.iloc[:, indices])
        dfs.columns.values[[0, 1, 2, 3, 4, 5, 6]] = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount']
        s_list = dfs.values.tolist()
        if verbose: print(day, "ohlc and volume", s_list)
        print(day, "close avg", dfs['close'].mean())
        print(day, "vwmp avg", (dfs['amount']/dfs['volume']).mean())

def get_band(name, days, verbose):
    #if verbose: print("split the time", day)
    import efinance as ef
    day=days[:-4]

    import pandas as pd
    if "day" in day: 

        s = ef.stock.get_quote_history(name, klt=101)
        indices = [2, 3, 4, 5, 6, 7, 8]
        d = int(day.split("day")[0])
        dfs = (s.iloc[:, indices]).tail(d)
        #print(dfs.columns)
        dfs.columns.values[[0, 1, 2, 3, 4, 5, 6]] = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount']
        s_list = dfs.values.tolist()
        if verbose: print(day, "ohlc and volume", s_list)

        tr1 = dfs['high'] - dfs['low']
        tr2 = dfs['high'] - dfs['close'].shift()
        tr3 = dfs['low'] -  dfs['close'].shift()
        #dfs['TR3'] = tr3
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
        kc_lookback, multiplier, atr_lookback = 20, 2, 10
        atr = tr.ewm(alpha = 1/atr_lookback).mean()
        kc_middle = dfs['close'].ewm(kc_lookback).mean()
        kc_upper = dfs['close'].ewm(kc_lookback).mean() + multiplier * atr
        kc_lower = dfs['close'].ewm(kc_lookback).mean() - multiplier * atr
        
        print(day, "keltner band", list(list(zip(dfs['date'], kc_lower, kc_middle, kc_upper))[-1]))

        lookback = day.split('day')[0]
        lookback = int(lookback)
        
        std = dfs['close'].rolling(lookback).std()
        sma = dfs['close'].rolling(lookback).mean()
        bb_upper = sma + std * 2
        bb_lower = sma - std * 2
        bb_middle = sma        
        print(day, "bolling band", list(list(zip(dfs['date'], bb_lower, bb_middle, bb_upper))[-1]))
    

    if "to" in day: 
        s = ef.stock.get_quote_history(name, klt=101)
        indices = [2, 3, 4, 5, 6, 7, 8]
        dfs = (s.iloc[:, indices])
        dfs.columns.values[[0, 1, 2, 3, 4, 5, 6]] = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount']

        d=day.split('to')
        #st = d[0].replace('-', '')
        #et = d[1].replace('-', '')
        if verbose: print("split the time", day)

        #dfs['date'] = pd.to_datetime(dfs['date'], format='%Y-%m-%d')
        # Filter data between two dates
        fdf = dfs.loc[(dfs['date'] >= d[0]) & (dfs['date'] <= d[1])]
        l = (fdf.shape[0])
        s_list = fdf.values.tolist()
        if verbose: print(day, "ohlc and volume", s_list)

        ddd = fdf.date.tolist()
        #print(ddd)

       
        for i in ddd: 
            dd = dfs[(dfs['date'] <= i)].tail(l)
            #if verbose: print("band by", dd)
            
            tr1 = dd['high'] - dd['low']
            tr2 = dd['high'] - dd['close'].shift()
            tr3 = dd['low'] -  dd['close'].shift()
            frames = [tr1, tr2, tr3]
            tr = pd.concat(frames, axis = 1, join = 'inner').max(axis = 1)
            kc_lookback, multiplier, atr_lookback = 20, 2, 10
            atr = tr.ewm(alpha = 1/atr_lookback).mean()
            kc_middle = dd['close'].ewm(kc_lookback).mean()
            kc_upper = dd['close'].ewm(kc_lookback).mean() + multiplier * atr
            kc_lower = dd['close'].ewm(kc_lookback).mean() - multiplier * atr
        
            print(day, "keltner band", list(list(zip(dd['date'], kc_lower, kc_middle, kc_upper))[-1]))
        for i in ddd: 
            dd = dfs[(dfs['date'] <= i)].tail(l)
            #if verbose: print("band by", dd)
        #lookback = day.split('day')[0]
            lookback = int(l)
        
            std = dd['close'].rolling(lookback).std()
            sma = dd['close'].rolling(lookback).mean()
        #print(std, sma)
            bb_upper = sma + std * 2
            bb_lower = sma - std * 2
            bb_middle = sma        
            print(day, "bolling band", list(list(zip(dd['date'], bb_lower, bb_middle, bb_upper))[-1]))

        
def get_vol(name, days, verbose):
    #if verbose: print("split the time", day)
    import efinance as ef
    day=days[:-3]
    # GBK encoded bytes
    gbk_encoded = b'\xc3\xc0\xb9\xc9'
    det2 = gbk_encoded.decode('gbk')

    gbk_encoded = b'\xb8\xdb\xb9\xc9'
    det1 = gbk_encoded.decode('gbk')
    import pandas as pd

    r2 = ef.stock.get_realtime_quotes([det2])
        #print(r.columns)
    r1 = ef.stock.get_realtime_quotes([det1])

    rr = pd.concat([r2, r1], ignore_index = True)
    #print(rr.columns)
    ss=rr.iloc[:,[0, 3, 15, 11, 12]]
    #print(ss)
    ss.columns.values[[0, 1, 2, 3, 4]] = ['code', 'price', 'total', 'volume', 'amount']
    ff = ss.loc[(ss['code'] == name)]
    ll = (ff.values.tolist()[0])
    if verbose: 
        div = ll[3] / (ll[2]/ll[1]) * 100
        print(name, "volume/total:", ll[3], "/", ll[2]/ll[1], "=", div, "%")
    #print("total / volume", ff['total']/ff['price'], ff['volume'])

    if "day" in day: 
        s = ef.stock.get_quote_history(name, klt=101)
        indices = [2, 4, 7, 8, -2]
        d = int(day.split("day")[0])
        dfs = (s.iloc[:, indices]).tail(d)
        dfs.columns.values[[0, 1, 2, 3, 4]] = ['date', 'close', 'volume', 'amount', 'change']
        
        s_list = dfs.values.tolist()
        if verbose: print(day, "close, volume, amount change", s_list)

        svol = dfs['volume'].sum() 
        div = svol / (ll[2]/ll[1]) * 100
        print(day, "volume/total:", svol, "/", ll[2]/ll[1], "=", div, "%")

        ddd = dfs.date.tolist()
        #print(ddd)
        l = 20 # PSY
        if len(ddd) >= 20:
            for i in ddd: 
               dd = dfs[(dfs['date'] <= i)].tail(l)
               psy = dd[(dd['change'] > 0)].shape[0] / l * 100
               print(day, "psy", [i, psy])
        else:
               if verbose: print("Erroe: less than 20 days has no psy")


    if "to" in day: 
        
        s = ef.stock.get_quote_history(name, klt=101)
        #print(s.columns)
        #indices = [2, 3, 4, 5, 6, 7, 8, -2]
        indices = [2, 4, 7, 8, -2]

        dfs = (s.iloc[:, indices])
        dfs.columns.values[[0, 1, 2, 3, 4]] = ['date', 'close', 'volume', 'amount', 'change']

        d=day.split('to')
        #st = d[0].replace('-', '')
        #et = d[1].replace('-', '')
        if verbose: print("split the time", day)

        #dfs['date'] = pd.to_datetime(dfs['date'], format='%Y-%m-%d')
        # Filter data between two dates
        fdf = dfs.loc[(dfs['date'] >= d[0]) & (dfs['date'] <= d[1])]
        #l = (fdf.shape[0])
        s_list = fdf.values.tolist()
        if verbose: print(day, "close, volume, amount change", s_list)

        svol = dfs['volume'].sum() 
        div = svol / (ll[2]/ll[1]) * 100
        print(day, "volume/total:", svol, "/", ll[2]/ll[1], "=", div, "%")

        ddd = fdf.date.tolist()
        #print(ddd)
        l = 20 # PSY
        for i in ddd: 
            dd = dfs[(dfs['date'] <= i)].tail(l)
            psy = dd[(dd['change'] > 0)].shape[0] / l * 100
            print(day, "psy", [i, psy])


def get_cost(s):
    t = 0
    tq = 0
    for i in s:
        q, p = i.split('@')
        get_fee(float(p), int(q))
        t = t + int(q) * float(p)
        tq = tq + int(q)
    print("no fee cost:", t)
    print("no fee avg:", t/tq)

def get_excel(name):
    import efinance as ef
    s = ef.stock.get_quote_history(name, klt=101)
    #print(s.tail(1))
    indices = [2, 3, 4, 5, 6, 7, 8, 12, -3, -1]
    dfs = (s.iloc[:, indices])
    dfs.columns.values[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] = ['date', 'open', 'close', 'high', 'low', 'volume', 'amount', 'change', 'change_rate', 'turnover_rate']
    #dfs = (s.iloc[:, indices])
    
    print(dfs.tail(5))
    return dfs.to_csv(f"{name}.csv")

import sys

if args.price == None: sys.exit("error: no price")
else: print(f"given price {args.price}")
#print(f"Code: {args.code}")

if args.code == "gann": get_gann(args.price)
elif args.code == "elliot": get_elliot(args.price)
elif args.code == "cost": sell(args.price) 
elif args.code == "gold": gold(args.price)
elif args.code == "benefit": benefit(args.price)

else: 
    if args.verbose: print("connecting ef to get the latest price")
    #if args.parameter == "latest": 
    try: get_stock(args.code)
    except Exception as e: sys.exit("error: no", args.code)
    if args.parameter == "minutes": get_minutes(args.code)
    
    if args.parameter == "5days": get_fdays(args.code)
    if args.parameter == "10days": get_tdays(args.code)
    if args.parameter == "30days": get_mdays(args.code)

    if args.parameter == "quarter": get_qdays(args.code)
    if args.parameter == "month": get_month(args.code)
    if args.parameter == "halfyear": get_halfyear(args.code)
    if args.parameter == "year": get_year(args.code)


    if "to" in args.parameter and "avg" not in args.parameter and "band" not in args.parameter and "vol" not in args.parameter: get_to(args.code, args.parameter, args.verbose)
    if "avg" in args.parameter: get_avg(args.code, args.parameter, args.verbose)
    if "band" in args.parameter: get_band(args.code, args.parameter, args.verbose)
    if "vol" in args.parameter: get_vol(args.code, args.parameter, args.verbose)

if args.fee:
    if "@" not in args.fee: 
        if args.fee == "0": print("error: no fee")
        else: get_fee(args.price, args.fee)
    else: 
        s = []
        if ',' not in args.fee: s = [args.fee]
        else: s = args.fee.split(',')
        get_cost(s)
        

if args.safe: 
    #print("python tradetrend.py")

    get_excel(args.code)
    print("trade... see the trend", f"{args.code}.csv")
    