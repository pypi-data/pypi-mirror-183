# -*- coding: utf-8 -*-
# @Time    : 2022-11-15 11:29
# @Author  : zbmain

def setting(max_row: int = 0, max_col: int = 0, max_col_w: int = 0, max_char_size: int = 0, float_precision: int = 0):
    """
    Pandas 常用设置
    @param max_row: 显示最大行数
    @param max_col: 显示最大列数
    @param max_col_w: 显示列长度
    @param max_char_size: 显示横向最多字符数
    @param float_precision: 显示浮点数最多位数
    @return: None
    """
    import pandas
    max_row and pandas.set_option('display.max_rows', max_row)
    max_col and pandas.set_option('display.max_columns', max_col)
    max_col_w and pandas.set_option('display.max_colwidth', max_col_w)
    max_char_size and pandas.set_option('display.width', max_char_size)
    float_precision and pandas.set_option('precision', float_precision)


def view_df(df, head_num: int = 5, tail_num: int = 5, comment: str = 'DataFrame'):
    print('%s row_size:%d' % (comment, df.shape[0]))
    import pandas as pd
    return None if -1 in (head_num, tail_num) else pd.concat([df.head(head_num), df.tail(tail_num)], axis=0)


def check_null(x, null_values: list = []):
    """
    检测空值

    @param x: 检测值
    @param null_values: list 检测值黑名单表,都作为None.
    """
    import pandas as pd
    return None if x and str(x).lower() in map(lambda z: z.lower(), null_values) or pd.isna(x) or pd.isnull(x) \
        else x


if __name__ == '__main__':
    import numpy as np

    print(check_null(np.nan))
