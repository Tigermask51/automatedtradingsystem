import pyupbit
import time
import datetime

from pyupbit.exchange_api import Upbit


# 객체 생성
f = open("upkey.txt")
lines = f.readlines()
access_key = lines[0].strip()  # access key '\n'
secret_key = lines[1].strip()  # secret key '\n'
f.close()

upbit = pyupbit.Upbit(access_key, secret_key)



# 목표가 설정
def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high']-yesterday['low']
    target = today['open'] + yesterday_range * 0.5
    return(target)

# 변수 설정
target = cal_target("KRW-BTC")
op_mode = False
hold = False

while True:
    now = datetime.datetime.now()

    # 09:00:00 목표가 갱신
    if now.hour == 9 and now.minute == 0 and 20 <= now.second <= 30:
        target = cal_target("KRW-BTC")
        op_mode = True

    price = pyupbit.get_current_price("KRW-BTC")
    print(now, price)
    time.sleep(1)

    # 매초마다 조건을 확인한 후 매수시도
    if op_mode is True and hold is False and price >= target:
    # 매수
        krw_balance = Upbit.get_balance("KRW")
        Upbit.buy_market_order("KRW-BTC", krw_balance)
        hold = True

    # 매도 시도
    while True:
        if now.hour == 8 and now.minute == 59 and (50 <=now.second <= 59):
            if op_mode is True and hold is True:
                btc_balance = Upbit.get_balance("KRW-BTC")
                Upbit.sell_market_order("KRW_BTC", btc_balance)
                hold = False

            op_mode = False
            time.sleep(10)

        # 상태 출력
        print(f"현재시간 : {now} 목표가 : {target} 현재가 : {price} 보유상태 : {hold}")

        time.sleep(1)


