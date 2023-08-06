# -*- coding: utf-8 -*-
import pdb
import numpy as np
import pandas as pd


def create_stats(df, horizon, offset, no_code=False):
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    df.set_index("trade_date", inplace=True)
    df["nxt1_ret"] = np.log(1. + df["chgPct"])
    if not no_code:
        df = df.groupby("code").rolling(window=horizon + 1)['nxt1_ret'].sum() \
            .groupby(level=0).shift(-(horizon + offset + 1)).dropna().reset_index()
    else:
        df = df.rolling(window=horizon + 1)['nxt1_ret'].sum().shift(
            -(horizon + offset + 1)).dropna().reset_index()
    return df