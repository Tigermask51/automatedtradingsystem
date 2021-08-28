import pyupbit

aa = pyupbit.get_ohlcv("KRW-BTC", "day")
print(aa)

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return(target)
