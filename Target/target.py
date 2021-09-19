import pyupbit
import time
import datetime

df = pyupbit.get_ohlcv(ticker)
yesterday = df.iloc[-2]
today = df.iloc[-1]
yesterday_range = yesterday['high'] - yesterday['low']
target = today['open'] + yesterday_range * 0.5
print("목표가:", target)