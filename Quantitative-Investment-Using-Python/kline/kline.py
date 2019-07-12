"""
https://tushare.pro/document/41?doc_id=4
https://github.com/mrjbq7/ta-lib
https://stackoverflow.com/questions/9944436/converting-ohlc-stock-data-into-a-different-timeframe-with-python-and-pandas
"""

import tushare as ts
import pandas as pd
import datetime as dt
import talib as ta


def transfer_kline(df, period):
    """
    :param df: [date, open, high, low, close, vol]
    :param period: D
    :return: df
    """
    ohlcv_dict = {
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'vol': 'sum'
    }
    df.reset_index(drop=True, inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index("date", inplace=True)
    return df.resample(period).apply(ohlcv_dict)


if __name__ == '__main__':
    pro = ts.pro_api()
    now = dt.datetime.now().timestamp()
    end_date = dt.datetime.fromtimestamp(now).strftime('%Y%m%d%H%M')
    print(f'end date: {end_date}')
    df = pro.coinbar(exchange='okex', symbol='btcusdt', freq='60min', start_date='20190701', end_date=end_date)
    # df.drop(df.index[[0, -1]], inplace=True)
    # print(df)

    df_4h = transfer_kline(df, '4H')

    df_4h['ema5'] = ta.EMA(df_4h['close'], timeperiod=5).tolist()
    df_4h['ema50'] = ta.EMA(df_4h['close'], timeperiod=50).tolist()

    _max = ta.MAX(df_4h['high'], timeperiod=20)
    _min = ta.MIN(df_4h['low'], timeperiod=20)
    df_4h['max'] = _max.tolist()
    df_4h['min'] = _min.tolist()
    df_4h['mid'] = (df_4h['max'] + df_4h['min']) / 2

    print(df_4h)

    print(df_4h[df_4h['mid'] > 0])
