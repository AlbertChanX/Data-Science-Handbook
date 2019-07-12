"""
brew install ta-lib
pip install TA-Lib
"""

import talib as ta


def ema(df, t1):
    t = ta.EMA(df, timeperiod=t1)
    print(t)
