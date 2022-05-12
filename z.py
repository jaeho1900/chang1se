import pandas as pd
import datetime

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.columns

df['고객군'].nunique()
df['건물군'].nunique()
df['건물'].nunique()

grouped = df.groupby('고객군')

i = 0
for name, data in grouped:
    i += 1
    print(i, name, data['건물군'].nunique(), data['건물군'].unique())

df2 = (
    pd.DataFrame({
        'X' : ['X1', 'X1', 'X1', 'X1'],
        'Y' : ['Y2', 'Y1', 'Y1', 'Y1'],
        'Z' : ['Z3', 'Z1', 'Z1', 'Z2']
    })
)
g = df2.groupby('X')
# pd.pivot_table(g, values='X', rows='Y', cols='Z', margins=False, aggfunc='count')
df2.pivot_table(values='X', index='Y', columns='Z', aggfunc=lambda x: len(x.unique()))
df2.pivot_table(values='X', index='Y', columns='Z', aggfunc=pd.Series.nunique)