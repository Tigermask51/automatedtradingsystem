import pyupbit

f = open("upbit.txt")
lines = f.readlines()
access = lines(0).strip()  # access key
secret = lines(1).strip()  # secret key
f.close()

upbit = pyupbit.Upbit(access, secret) # class instance
balance = upbit.get_balance("KRW")
print(balance)