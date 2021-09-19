import pyupbit
import time
import datetime

while True:
    now = datetime.datetime.now()
    price = pyupbit.get_current_price(ticker)
    print(now, price)
    time.sleep(1)
