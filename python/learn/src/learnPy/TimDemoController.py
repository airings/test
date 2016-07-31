'''
Created on Jul 28, 2016

@author: airings
'''
import time
from functools import partial
import datetime
from matplotlib import finance, mlab
import numpy as np
import pandas as pd
from pandas.core.series import Series

def load_data_yahoo(code, start_date, end_date ):
#     http://blog.csdn.net/matrix_laboratory/article/details/50687910
# http://blog.csdn.net/mengwuyoulin/article/details/51165851
    fh = finance.quotes_historical_yahoo_ohlc(code, start_date, end_date,adjusted=False)
#     print type(fh)
    return fh[0][4]


def load_data_excel(path,sheet):
#     file://localhost/path/to/workbook.xlsx
    df = pd.read_excel(path, sheet)
    return df

def recon_data(df):
    df['Diff'] = df['PX_LAST'] - df['YA_Close']
    metric = Series.to_frame(df['Diff'].describe(), name='Metric')
    t = (df, metric)
    return t

def pivot_table_data(rel):
    data = rel[0]
#     pd.pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name)

def sort_data(rel,col):
    data = rel[0]
    rel[0] = data.sort_values(by=col, ascending=False)
    return rel

def write_excel(rel):
    data = rel[0]
    metric = rel[1]
    fileName = "../file/output_read"
    wbw = pd.ExcelWriter(fileName+".xlsx")
    data.to_excel(wbw, 'Diff', startcol=0,index=False)
    metric.to_excel(wbw, 'Metric', startcol=0,index=True)
    wbw.save()
    
    fileName = '../file/finialExcel'
    wbw = pd.ExcelWriter(fileName+".xlsx", engine='xlsxwriter')
    data.to_excel(wbw, 'Diff', startcol=0,index=False)
    metric.to_excel(wbw, 'Diff', startcol=data.shape[1]+3,index=True)
    wbw.save()

def process(path, sheet, start_date, end_date):
    df = load_data_excel(path, sheet)
    f = partial(load_data_yahoo, start_date=start_date, end_date=end_date)
    df['YA_Close'] = df['Ticker'].map(lambda x: x.replace(' ','.')).map(f)
    
    t = recon_data(df)
    write_excel(t)
    return t

if __name__ == '__main__':
    path = "/Users/airings/Documents/workspace/learn/src/file/KOSPI 200 PRICES.xlsx"
    sheet = "Sheet1"
    t = process(path,sheet, start_date=(2016, 07, 25), end_date=(2016, 07, 25))
    print t[0].to_html()