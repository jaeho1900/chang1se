import pandas as pd
import datetime
import re

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.shape
df.columns

len(df[~df.건물.str.contains('(KR|수퍼)')])
new_df = df[~df.건물.str.contains('(KR|수퍼)')]

new_df.tail()


