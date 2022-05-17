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




# # 판다스 정규표현식: re 라이브러리 불필요)
import pandas as pd
df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'Dave', 'Ellen', 'Frank'],
                   'age': [24, 42, 18, 68, 24, 30],
                   'state': ['NY', 'CA', 'CA', 'TX', 'CA', 'NY'],
                   'point': [64, 24, 70, 70, 88, 57]})

# str.extract: 추출
df.name.str.extract('\d{2,3}')
df.loc[df.age.str.extract('^2')]

# str.contains: 포함여부(True 또는 False 반환)
df.state.str.contains('CA')
len(df[df.state.str.contains('CA')])

# 치환
df.replace('(.*)li(.*)', r'\1LI\2', regex=True)  # 그룹1과 매칭, 그룹2와 매칭
sr.str.replace('김', '황')

# []: [ ] 문자 클래스는 대괄호 안에 포함된 문자들 중 하나와 매치를 뜻함
# [0-9]: 숫자
# [a-zA-Z]: 알파벳 모두
# \d: 숫자와 매치, [0-9]와 동일한 표현식
# \D: 숫자 아닌 것과 매치, [^0-9]와 동일한 표현식
# \s: whitespace문자와 매치, [ \t\n\r\f\v]와 동일한 표현식. 맨 앞의 빈칸은 공백문자를 의미
# \S: whitespace문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식
# \w: 문자+숫자와 매치, [a-zA-Z0-9_]와 동일한 표현식
# \W: 문자+숫자가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식
