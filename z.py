import pandas as pd
import datetime
import re

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.shape
df.columns
df.head()
df['고객군'].nunique()
df['건물군'].nunique()
df['건물'].nunique()

df[df.건물 != re.search(pattern, string)]
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
# ################
# 파이썬 re모듈
# ################

# # 1. re 모듈의 메소드

# 종류       기능                    찾는경우                없는경우
# match      문자열 첫글자부터 검색   match object 1개       None
# search     문자열 전체를 검색       match object 1개       None
# findall    문자열 전체를 검색       문자열 리스트          빈 리스트
# finditer   문자열 전체를 검색       match object iterator  None
# fullmatch  패턴과 문자열이 완벽일치 match object 1개       None
# sub        일종의 replace
# compile    정규식을 반복 사용

# # 2. match object의 메소드

# 종류   기능                           예시
# start  매칭된 문자열의 시작 위치       5
# end    매칭된 문자열의 끝 위치         11
# span   매칭된 문자열의(시작, 끝)튜플   (5, 11)
# group  매칭된 문자열을 반환            people
# groups(), group(int)  소괄호()가 존재하는 패턴에서만 활용

# # 3. 정규표현식
# [A-Z] 대괄호안 문자 중 1개 나타남  ([A-Z]+ 1개이상 나타남)
# (a+b) 그룹으로 묶은 하위표현식
# | |로 분리된 문자,하위표현식 나타남
# . 문자,글자,숫자,기호,공백 등 1개 나타남#
# * 바로앞 문자,하위표현식,대괄호 0번이상 나타남
# + 바로앞 문자,하위표현식,대괄호 1번이상 나타남
# {m,n} 바로앞 문자,하위표현식,대괄호 m번이상 n번이하 나타남#
# [^a-z] 대괄호안 문자제외한 문자 나타남
# ?! 바로뒤 문자,하위표현식을 제외함#
# ^ 바로뒤 문자,하위표현식이 첫문자가 됨
# $ 바로앞 문자,하위표현식이 끝문자가 됨
# \ 특수문자앞에서 본래문자로 나타냄

# # 4. 예제

# 4-1. re 모듈의 메소드 예제 ----------

import re
str = 'love people around you, love your work, love yourself'

# compile(패턴, 플래그): 정규식을 반복 사용할 때 지정 필요
c = re.compile('a')
print(c.sub('zxc', 'abcdefg'))
print(c.search('vcxdfsa'))

# match: 문자열의 첫글자부터 검색(결과: 처음 1개의 match 객체만 반환)
result = re.match('ove', str)
print(result)

# search: 문자열의 전체를 검색(결과: 처음 1개의 match 객체만 반환)
result = re.search('ove', str)
print(result)

# findall: 문자열의 전체를 검색(결과: 전부 찾아서 리스트로 반환)
result = re.findall('love', str)
print(result)

# finditer: 문자열의 전체를 검색(결과: 전부 찾아서 iterator(순회객체)로 반환)
result = re.finditer('love', str)
for iter in result:
    print(iter)

# fullmatch: 패턴과 문자열이 완벽하게 일치할 때 반환
str2 = 'Hey Guys, read books'
result = re.fullmatch('Hey Guys, read books', str2)
print(result)

result = re.fullmatch('.*', str2)
print(result)

# sub(패턴, 교체할 문자열, 적용 문자열, 교체횟수)
str3 = '010-2343-9537'
result = re.sub(r'(?<=\d{3}-\d{4}-)\d{4}', '****', str3)
print(result)

re.sub("2343", "1234", str3)
re.sub(r"[^\d]", "", str3, 1)

# 4-2. match 객체의 메소드 예제 ----------

import re
str = 'love people around you, love your work, love yourself'
result = re.search('people', str)

# group(): 매칭된 문자열 반환
print(result.group())

# start(): 매칭된 문자열의 시작 위치 반환
print(result.start())

# end(): 매칭된 문자열의 끝 위치 반환
print(result.end())

# span(): 매칭된 문자열의 (시작, 끝) 위치 튜플 반환
print(result.span())

# groups(), group(int)
result = re.match(r'(\d{2})-(\d{3,4})-(\d{4})', '02-123-1234')
print(result.group())
print(result.groups())
print(result.group(0))
print(result.group(1))
print(result.group(2))

# 4-3. 전화번호 형식을 검사하는 정규표현식 ----------

# 매칭되는 문자열 한 개
str1 = '010-2343-3333'
result = re.match(r'\d{2,3}-\d{3,4}-(\d{4})$', str1)  # (숫자 2~3자리)-(숫자 3~4자리)-(숫자 4자리)(문자열 끝)
print(result.group(1))  # 3333

# 매칭되는 문자열 여러 개
str2 = '010-1234-7888, 010-7895-1234, 010-5468-5678, 010-7895-9999, 010-1234-2222'
result = re.finditer(r'\d{2,3}-\d{3,4}-(\d{4})(?=,|$)', str2)
# (숫자 2~3자리)-(숫자 3~4자리)-(숫자 4자리)(바로뒤문자가 , or 문자열 끝)
for idx, iter in enumerate(result, 1):
    print(f'{idx}. {iter.group(1)}')  # 1. 7888 2. 1234 3. 5678 4. 9999 5. 2222

re.findall("(?<=1234)(.*)(?=,)", str2)
# 시작점을 '?<='로 표현하고, 끝점은 '?='을 이용, .의 경우 모든 문자열을 의미하며 *는 반복을 의미

re.findall("(?<=1234)(.{9,23})(?=,)", str2)
# 9글자에서 23글자까지의 범위에서 패턴과 일치하는 값을 반환

# 4-4. 이메일 주소 표현식 : [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
