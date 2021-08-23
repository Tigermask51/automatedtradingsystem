import pyupbit
import pprint

f = open("upkey.txt")
lines = f.readlines()
access_key = lines[0].strip()  # access key '\n'
secret_key = lines[1].strip()  # secret key '\n'
f.close()

upbit = pyupbit.Upbit(access_key, secret_key)
balance = upbit.get_balance("KRW")
print(balance)
