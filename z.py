import pandas as pd
import datetime
import re

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.shape
df.columns

df.건물.head(11)
len(df[df.건물.str.contains('([^수퍼])')])

i = 0
for name, data in grouped:
    i += 1
    print(i, name, data['건물군'].nunique(), data['건물군'].unique())

df2 = (pd.DataFrame({'X': ['X1', 'X1', 'X1', 'X1'],
       'Y': ['Y2', 'Y1', 'Y1', 'Y1'],
       'Z': ['Z3', 'Z1', 'Z1', 'Z2']}))
g = df2.groupby('X')
# pd.pivot_table(g, values='X', rows='Y', cols='Z', margins=False, aggfunc='count')
df2.pivot_table(values='X', index='Y', columns='Z', aggfunc=lambda x: len(x.unique()))
df2.pivot_table(values='X', index='Y', columns='Z', aggfunc=pd.Series.nunique)


# #
import pandas as pd
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
                   'age': [24, 42, 18, 68, 24, 30],
                   'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
                   'point': [64, 24, 70, 70, 88, 57]})

print(df)

# str.extract 추출: 캡쳐그룹생성및 str형변환 필요
df.name.str.extract(r'(.+li)')
df.name.str.extract(r'(.+)(li)(\w)*')  # (3개)그룹을 나누면 (3개)열로 분리됨
df.age.astype(str).str.extract(r'(2)?')

# str.contains 포함여부(regex 옵션지정 필요)
df.state.str.contains('CA', regex=True)
len(df[df.state.str.contains('CA', regex=True)])
df[df.state.str.contains('CA', regex=True)]

# 치환(regex 옵션지정 필요)
df.replace('(.*)li(.*)', r'\1 123 \2', regex=True)
df.state.str.replace('N.', '뉴욕', regex=False)



