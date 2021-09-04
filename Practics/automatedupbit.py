import pyupbit
import pprint
import pandas

from pyupbit.exchange_api import Upbit

f = open("upkey.txt")
lines = f.readlines()
access_key = lines[0].strip()  # access key '\n'
secret_key = lines[1].strip()  # secret key '\n'
f.close()

upbit = pyupbit.Upbit(access_key, secret_key)
print(Upbit.get_balances())