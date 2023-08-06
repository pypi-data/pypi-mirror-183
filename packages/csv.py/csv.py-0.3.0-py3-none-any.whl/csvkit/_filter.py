import pandas as pd
import math
from typing import List

def column_equal(*,
        df :pd.DataFrame,
        column_name: str,
        value
) -> pd.DataFrame:
    if column_name in df.columns:
        return df.loc[df[column_name] == value]
    else:
        return pd.DataFrame(columns=df.columns)

def filter_row(
        *,
        df: pd.DataFrame,
        condition: callable,
):
    return df[df.apply(condition,axis=1)]


def count_row(
    *,
    df: pd.DataFrame,
    condition: callable,
):
    return len(df[df.apply(condition,axis=1)])


def count_nan(
    *,
    df: pd.DataFrame,
    column: str
):
    cond = lambda x : math.isnan(x[column])
    return count_row(df=df,condition=cond)


def drop_nan(
    *,
    df: pd.DataFrame,
    column: str,
):
    cond = lambda x : not math.isnan(x[column])
    return filter_row(df=df,condition=cond)


def drop_nan_multicol(
    *,
    df:pd.DataFrame,
    columns: List[str]
):
    cond = lambda x : all([not math.isnan(x[col]) for col in columns])
    return filter_row(df=df,condition=cond)