import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import rc
rc('font', family = 'malgun gothic')

trend_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name = '개요',
            index_col = 0,
            parse_dates = ['날짜'],
            skiprows=6)

asset_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name = '블루에셋',
            usecols='B:E',
            parse_dates = ['기사날짜'])

blue_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name = '블루스캔',
            usecols='B:E',
            parse_dates = ['기사날짜'])


trend_df.plot(kind ='line')
asset_df.plot(kind ='bar')


asset_df.dtypes

