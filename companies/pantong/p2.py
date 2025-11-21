import random
import pandas as pd
import numpy as np
from typing import List
from datetime import datetime, timedelta


def generate_data(symbol_list: List[str], datetime_start: str, datetime_end: str,
                  column_list: List[str]) -> pd.DataFrame:
    """
    given symbol_list,like ["A","B"，"C"]
    given datetime_start,like "20180103 09:00:00"
    given datetime_end,like "20180103 15:00:00"
    given column_list,like ["last_price", "ask1", "bid1"]

    generate random price in column list for every symbol
    from datetime start to datetime end sample every second

           last_price      ask1      bid1 symbol                time
    0        0.173368  0.666229  0.650586      A 2018-01-03 09:00:00
    1        0.434612  0.771833  0.891474      A 2018-01-03 09:00:01
    2        0.222062  0.891160  0.299797      A 2018-01-03 09:00:02
    3        0.947866  0.073749  0.169601      A 2018-01-03 09:00:03
    4        0.800996  0.548314  0.360005      A 2018-01-03 09:00:04
    5        0.529903  0.542695  0.876590      A 2018-01-03 09:00:05
    """
    result = []
    for symbol in symbol_list:
        fmt_str = '%Y%m%d %H:%M:%S'
        start_time = datetime.strptime(datetime_start, fmt_str)
        end_time = datetime.strptime(datetime_end, fmt_str)
        current = start_time
        while current <= end_time:
            time_str = current.strftime('%Y-%m-%d %H:%M:%S')
            data = {'symbol': symbol, 'time': time_str}
            for col in column_list:
                data[col] = random.random()
            result.append(data)
            current += timedelta(seconds=1)
    return pd.DataFrame(result)


def cal_min_bar(df: pd.DataFrame) -> pd.DataFrame:
    """
    resample the last price column in second to generate open high low close in minutes
    generate bar return (bar_ret) column which means close /open
    generate flag column: if high / close <1.5 flag=1 else flag = 0
    no for loop statement

    symbol                time      open      high       low     close    bar_ret  flag
         A 2018-01-03 09:01:00  0.256674  0.996918  0.010180  0.082958   0.323205     0
           2018-01-03 09:02:00  0.114607  0.984437  0.033200  0.409413   3.572324     0
           2018-01-03 09:03:00  0.261541  0.980200  0.002990  0.462317   1.767662     0
           2018-01-03 09:04:00  0.379665  0.949153  0.006085  0.594945   1.567028     0
    """
    df = df.copy()
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)
    ohlc = (
        df.groupby('symbol')['last_price']
        .resample('1min')
        .ohlc()
        .reset_index()
    )
    ohlc['bar_ret'] = ohlc['close'] / ohlc['open']
    ohlc['flag'] = ((ohlc['high'] / ohlc['close']) < 1.5).astype(int)
    return ohlc


def select_data(df: pd.DataFrame, n):
    """
    select every symbol top n bar_ret in subset with condition flag ==1,
    no for loop statement

         symbol                time      bar_ret
    19        A 2018-01-03 09:20:00  1165.155037
    112       A 2018-01-03 10:53:00   110.638160
    211       A 2018-01-03 12:32:00    32.071124
    653       B 2018-01-03 13:53:00  1059.186040
    377       B 2018-01-03 09:17:00   238.020314
    466       B 2018-01-03 10:46:00    66.322434
    855       C 2018-01-03 11:14:00    90.620752
    1071      C 2018-01-03 14:50:00    47.786062
    786       C 2018-01-03 10:05:00    29.567013
    """
    top_n = (
        df[df['flag'] == 1].copy()
        .groupby('symbol', group_keys=False)
        .apply(lambda x: x.nlargest(n, 'bar_ret').assign(symbol=x.name), include_groups=False)
        .reset_index(drop=True)
    )
    return top_n[['symbol', 'time', 'bar_ret']]


if __name__ == "__main__":
    symbol_list = list("ABC")
    start = "20180103 09:00:00"
    end = "20180103 15:00:00"
    column_list = ["last_price", "ask1", "bid1"]
    price_data = generate_data(symbol_list, start, end, column_list)
    print(price_data)

    bar_data = cal_min_bar(price_data[["time", "symbol", "last_price"]])
    print(bar_data.head())

    focus_data = select_data(bar_data, 3)
    print(focus_data)
