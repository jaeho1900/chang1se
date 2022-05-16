import pandas as pd
import datetime
import re

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.shape
df.columns

df.건물.head(11)

len(df.건물.str.contains('수퍼').head(11))




# except store
df[df.건물 is not re.search('\d{3}', df.건물[0])]
df[df.건물 == re.search('^KR', df.건물)]


print(re.search('\d{3}', df.건물[0]))


occ = []
for i in len(df.건물):
    occ.append(df[df.건물 != re.search('\d{3}', df.건물[0])])





print(occ)




grouped = df.groupby('고객군')





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


# # 판다스 정규표현식

import pandas as pd  # re 라이브러리 불필요

df = pd.DataFrame({'name': ['Alice','Bob','Charlie','Dave','Ellen','Frank'],
                   'age': [24,42,18,68,24,30],
                   'state': ['NY','CA','CA','TX','CA','NY'],
                   'point': [64,24,70,70,88,57]}
                  )

# 치환
print(df.replace('(.*)li(.*)', r'\1LI\2', regex=True))

# str.extract: 특정 문자열을 추출
df.age.str.extract('([a-zA-Z]+)\.')

# str.contains: 지정한 문자열이 포함되어 있는지 확인(True 또는 False 반환)
df.state.str.contains('(CA)')
len(df[df.state.str.contains('(CA)')])



import pandas as pd

sampleData = pd.DataFrame()
sampleData['val1'] = ['M', 'F', 'M', 'M', 'F']

sampleData.loc[(sampleData.val1 == 'M'), 'val1']

str.contains - 포함하면 값을 반환


 import pandas as pd

sampleData = pd.DataFrame()
sampleData['val1'] = ['abc1.pdf', 'abc2.pdf', 'abc3.pdf', 'abc4.pdf', 'abc5.pdf']


위의 데이터에서 pdf 파일명 1~3만 추출하는 상황을 가정해보겠습니다.



sampleData.loc[sampleData['val1'].str.contains(r"abc[1-3]")]