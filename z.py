import pandas as pd
import datetime
import re

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])

df.columns
df.발생일시.isnull().sum()

df2 = pd.Series(df.발생일시.dt.date.value_counts())
df2.index = pd.to_datetime(df2.index)
df2.index

import calplot
calplot.calplot(df2)

df.발생일시.dt.weekday.value_counts().sort_index(inplace=False).plot(kind='bar', xlabel=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

df.set_index(['발생일시'], inplace=False).resample('H').sum()

