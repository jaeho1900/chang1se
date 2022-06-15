"""
_Pandas.py
"""


#######################################
# 데이터 입출력
#######################################

# # csv 읽기 ----------
df_csv = pd.read_csv("./stats.csv",
                     # index_col=0,          # 행 인덱스가 되는 열 지정(None..)
                     # header=0,             # 열이름으로 사용할 행 지정(None..)
                     # usecols=[0,3,6,8],    # 불러올 columns
                     # nrows=6,              # 불러올 rows
                     # skiprows=[1,3],       # 처음 몇 줄을 skip할지 설정
                     # skipfooter=5,         # 마지막 몇 줄을 skip할지 설정
                     # encoding='CP949',     # 한글인코딩: 조합형유니코드UTF8, 완성형웹EUC-KR, 완성형윈도우CP949
                     # sep=",",              # txt파일은 "\t"
                     )

# # excel 읽기 ----------
df_xl = pd.read_excel('./stats.xlsx',
                      # sheet_name='prod',
                      # index_col="A",       # 행 인덱스가 되는 열 지정(숫자, 컬럼명, None..)
                      # usecols='B:D, H, j',
                      )

# # html 의 <table>태그로 작성된 표 읽기 ----------
tables = pd.read_html('./trainingdata/html/first.html', encoding='utf-8')
tables[0]  # 첫번째 표(복수의 표는 데이터프레임 리스트로 읽어옴)

# # 웹 스크래핑 ----------
# 스크래핑한 내용을 리스트나 딕셔너리로 정리한 후, 데이터프레임으로 변환
from bs4 import BeautifulSoup
import requests
import re

url = r"https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
rows = soup.select('div > ul > li')
etfs = {}
for row in rows:
    try:
        etf_name = re.findall(r'^(.*) \(NYSE', row.text)
        etf_market = re.findall(r'\((.*)\|', row.text)
        etf_ticker = re.findall(r'NYSE Arca\|(.*)\)', row.text)
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            # 리스트를 원소로 갖는 딕셔너리를 생성
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
    except AttributeError as err:
        pass
# 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)

# # csv 저장 ----------
df.to_csv("./sample.csv",
          # columns = ['날짜', '국적', '계'],  # 저장할 열 지정
          # index = False,                     # 행 인덱스 제거
          # header = False,                    # 열이름 제거
          # encoding = 'utf-8',
          )

# # excel 저장 ----------
df.to_excel("./sample.xlsx")

# # 복수의 excel sheet에 저장
with pd.ExcelWriter('./sample_multi_sheet.xlsx') as writer:
    df1.to_excel(writer, sheet_name='1sheet')
    df2.to_excel(writer, sheet_name='2sheet')

# # 기존 excel 파일에 저장
import openpyxl
book = openpyxl.load_workbook('./present.xlsx')
writer = pd.ExcelWriter('./present.xlsx', engine='openpyxl')
writer.book = book
df1.to_excel(writer, sheet_name='1sheet')
df2.to_excel(writer, sheet_name='2sheet')
writer.save()
writer.close()

# # excel: protected files(1)
import win32com.client
import pandas as pd
xl = win32com.client.Dispatch("Excel.Application")
# xl.Visible = False
filename = './excel_pass.xlsx'
password = '1'
wb = xl.Workbooks.Open(os.path.abspath(filename), Password=password)
ws = wb.Sheets(1)
content = ws.Range('A1:G313').Value
# content = xlws.Range(xlws.Cells(1,1), xlws.Cells(313,7)).Value
df = pd.DataFrame(list(content))
xl.Quit()

# # excel: protected files(2)
import xlwings as xw
import pandas as pd
xl = xw.App(visible=False)  # 엑셀 인스턴스 객체 생성
filename = './excel_pass.xlsx'
password = '1'
wb = xw.Book(os.path.abspath(filename), password=password)
ws = wb.sheets['addSheet']
df = ws['A1:G313'].options(pd.DataFrame, index=False, header=True).value
xl.kill()


#######################################
# 데이터프레임
#######################################

# # 인덱스 ----------

# # 인덱스 설정 및 변경
df.index = ['상록수', '양귀비', '진서영']
df.columns = ['나이', '성별', '학교명', '생년월일']
df.rename(index={'상록수': '학생1', '양귀비': '학생2', '진서영': '학생3'}, inplace=True)
df.rename(columns={'나이': '연령'}, inplace=True)

# # 특정 열을 행 인덱스로 설정
ndf1 = df.set_index(['성별'])
ndf2 = df.set_index(['성별', '연령'])

# # 정수인덱스로 초기화하면서, 기존 행 인덱스는 열로 이동
df.reset_index()
df.reset_index(drop=True)                # 기존 행 인덱스 제거
df.reset_index().rename(columns={'index': '구분'})

# # 정렬 및 삭제 ----------

# # 행 인덱스 기준으로 정렬
df.sort_index(ascending=True)            # 오름차순(True)

# # 특정 열 기준으로 정렬
df.sort_values(by=['성별', '학교명'],    # 기준열
               ascending=True,           # 오름차순(True)
               # inplace=True,           # 자체 저장
               # ignore_index=True,      # 기존 인덱스 무시
               na_position='last')       # 결측값 위치 'first'

# # 행 열 삭제
df.drop(['학생1', '학생3'], inplace=False)  # 행삭제(axis=0)
df.drop('연령', axis=1, inplace=False)      # 열삭제

# # 구조 확인 ----------

df.info()
df.dtypes                   # 자료형
df.describe(include='all')  # 통계(평균,편차,최대,최소,중간값), include옵션은 문자열데이터의 고유값개수,최빈값,빈도수
df.shape                    # 크기(행, 열)
len(df)                     # NaN 포함 개수
df.count()                  # NaN 이 아닌 개수
df['성별'].unique()                                         # 고유값 구성원
df['성별'].nunique()                                        # 고유값 개수
df['성별'].value_counts()                                   # 고유값별 자료수(NaN 생략)
df['성별'].value_counts(dropna=False)                       # 고유값별 자료수(NaN 포함)
df['연령'].value_counts(bins=[0, 12, 15, 20], sort=False)   # 구간별 자료수


#######################################
# 시각화
#######################################

# # 기본 그래프 ----------
# # 고급 그래프 ----------
# # 지도 ----------


#######################################
# 품질향상
#######################################

# # 결측값(Not a Number) ----------

# # 결측값 갯수 확인
df.info()
df.isnull().sum()

# # 열(변수) 삭제
df = df.dropna(thresh=500, axis=1)  # NaN 이 500개 이상인 열

# # 행(관측치) 삭제
df = df.dropna(subset='age', how='any', axis=0)

# # 평균값 채우기
mean_age = df.age.mean(axis=0)
df = df.age.fillna(mean_age)

# # 최빈값 채우기
most_freq = df.embark_town.value_counts(dropna=True).idxmax()
df = df.embark_town.fillna(most_freq)

# # 이웃값 채우기('ffill', 'bfill')
df.embarked.fillna(method='ffill', inplace=True)

# # 그룹별 채우기
df.groupby('지역').apply(lambda g: g.fillna(g.mean()))

# # 컬럼별 채우기
df.fillna({'인구': '통계오류', '기온': df2['기온'].mean()})

# # 보간 채우기(linear 선형보간, time 시간보간: 시간형 인덱스이어야 함)
df.interpolate(method='linear')

# # if조건 채우기
df['New'] = np.where(pd.notnull(df['기온']) is True, df['기온'], df['기온'].mean())

# # 중복값 ----------

# # 중복값 찾기
df['c2'].duplicated()
df.duplicated()

# # 중복 행 제거
df.drop_duplicates()

# # 조건 열을 기준으로 중복 행 제거
df.drop_duplicates(subset=['c2', 'c3'])

# # 표준화(포멧) ----------

# # 자료형 변환
df['m'].replace('?', np.nan, inplace=True)  # 문자형원소를 NaN으로 변경 선행 후
df['m'] = df['m2'].astype('float')          # 실수형으로 변환
df['y'] = df['year'].astype('category')     # 범주형으로 변환

# # 범주화 ----------

# # 구간 분할
# 연속형 데이터를 일정 구간(수준)으로 나눠서 구간별 차이를 분석하는 방법

from sklearn.datasets import load_iris
iris = load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# np.histogram 함수로 bin 경계값 리스트 구하기
count, bin_dividers = np.histogram(iris_df['sepal length (cm)'], bins=3)
print(bin_dividers)

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
bin_names = ['소형', '중형', '대형']
iris_df['sepal_bin'] = pd.cut(x=iris_df['sepal length (cm)'],  # 데이터 배열
                              bins=bin_dividers,               # 경계 값 리스트
                              labels=bin_names,                # bin 이름
                              include_lowest=True)             # 첫(낮은) 경계값 포함

# # 더미 변수
# 범주형 3개영역을 각 더비변수 열로 생성(속하면1, 속하지 않으면0)
sepal_dummies = pd.get_dummies(iris_df['sepal_bin'])
print(sepal_dummies.head(15))

# # 정규화(상대적크기차이제거) ----------

# 열데이터에서 열최솟값을 뺀 값을 분자로 하고, 열최댓값-열최솟값을 분모로 산출(0~1)
min_x = iris_df['sepal length (cm)'] - iris_df['sepal length (cm)'].min()
min_max = iris_df['sepal length (cm)'].max() - iris_df['sepal length (cm)'].min()
iris_df['sepal_normalization'] = min_x / min_max
print(iris_df['sepal_normalization'].describe())


#######################################
# 시계열
#######################################

# # 시계열 객체 변환 ----------

# # 문자열을 Timestamp 로 변환
df['NewDate'] = pd.to_datetime(df['Date'])

# # Timestamp 를 Period 로 변환(D, B, W, M, MS, Q, QS, A, AS, H, T, S)
pr_year = df['NewDate'].to_period(freq='A')
pr_month = df['NewDate'].to_period(freq='M')
pr_day = df['NewDate'].to_period(freq='D')

# # 시계열 데이터 만들기 ----------

# # Timestamp 배열
ts_ms = pd.date_range(start='2019-01-01',   # 날짜 범위의 시작
                      end=None,             # 날짜 범위의 끝
                      periods=4,            # 생성할 Timestamp의 개수
                      freq='3MS',           # 시간 간격 (MS: 월의 시작일)
                      tz='Asia/Seoul')      # 시간대(timezone)

# # Period 배열
pr_h = pd.period_range(start='2019-01-01',  # 날짜 범위의 시작
                       end=None,            # 날짜 범위의 끝
                       periods=3,           # 생성할 Period 개수
                       freq='H')            # 기간의 길이 (H: 시간)

# # 시계열 데이터 활용(dt 속성) ----------

# # 날짜 데이터 분리
df['NewDate'].dt.year
df['NewDate'].dt.month
df['NewDate'].dt.day

# # Period 에서 '년, 년-월' 분리
df['NewDate'].dt.to_period(freq='A')
df['NewDate'].dt.to_period(freq='M')

# # 시계열 인덱스 ----------

df.set_index('NewDate', inplace=True)
# 날짜나 기간으로 슬라이싱 용이
df['2021']
df['2022-01-01':'2023-12-31']
df.loc['2022-03']
df.loc['2023-03':]
df.loc['2021-01', 'Date':'Time']


#######################################
# 데이터프레임 응용
#######################################

# # 함수 매핑 ----------

import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(4, 3), columns=['a', 'b', 'c'])
df.info()

# # 시리즈 -> 개별데이터 -> 시리즈
df['a'].map(lambda x: '%.2f' % x if (x > 5) else x)

# # 데이터프레임 -> 개별데이터 -> 데이터프레임
df.applymap(lambda x: '%.2f' % x if (x > 5) else x)

# # 시리즈 -> 시리즈객체(행, 열) -> 시리즈
df['a'].apply(lambda x: '%.2f' % x if (x > 5) else x)

# # 데이터프레임 -> 시리즈객체(행, 열) -> 시리즈, 데이터프레임(통합시리즈)
df.apply(lambda x: x.max() - x.min(), axis=1)
df.apply(lambda x: x.max() - x.min())
df.apply(lambda k: k * 2)

# # 데이터프레임 -> 데이터프레임객체 -> 단일값, 시리즈, 데이터프레임
df.pipe(lambda x: x.sum().sum())
# 체인기능
df.pipe(lambda x: x * 2).pipe(lambda x: x.max()).pipe(lambda x: x.sum())

# # 열 분리 ----------

np.random.seed(0)
df = pd.DataFrame(np.random.randn(10, 3),
                  index=pd.date_range('1/1/2018', periods=10),
                  columns=['A', 'B', 'C']).cumsum()
# 1단계: 문자열로 변환
df['yymmdd'] = df.index.astype('str')
# 2단계: 문자열을 분해하여 "리스트로 저장"
dates = df['yymmdd'].str.split('-')
# 3단계: 인덱스 기준으로 리스트를 꺼내어 새로운 열에 저장
df['year'] = dates.str.get(0)
df['month'] = dates.str.get(1)
df['day'] = dates.str.get(2)
print(df)

# # 필터링 ----------

import seaborn as sns
titanic = sns.load_dataset('titanic')

# # 단일 또는 복합 조건식
mask = (titanic.age >= 60) & (titanic.sex == 'female')
titanic.loc[mask, ['age', 'sex', 'alone']]

# 단일 조건식의 인자를 리스트로 전달
mask = titanic.age.isin([30, 40, 50])
titanic.loc[mask, ['age', 'sex', 'alone']]

# # 데이터프레임 합치기 ----------

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                   index=[2, 3, 4, 5])

# # 연결
pd.concat([df1, df2])                     # 열기준(axis=0), 합집합(join='outer')
pd.concat([df1, df2], ignore_index=True)  # 새로운 정수형 인덱스 설정
pd.concat([df1, df2], axis=1, join='inner')

# # key 로 병합
# 열을 키로 지정(공통on, left_on, right_on), 인덱스를 키로 지정(left_index, right_index)
# 결합 방법(inner, outer, left, right)
pd.merge(df1, df2)                                 # 공통되는 모든열기준(on=None), 교집합(how='inner')
pd.merge(df1, df2, on='a', how='outer')            # 공통되는 열(a) 기준의 합집합
pd.merge(df1, df2, left_on='a', right_index=True)  # 왼쪽df a열과 오른쪽df 인덱스를 키로 지정
pd.merge(df1, df2, on=['a', 'b'], suffixes=['_left', '_right'])   # 열명이 중복되는 경우에 접미사 지정

# # 그룹 연산 ----------

import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]


def min_max(x):
    return x.max() - x.min()


# # 그룹객체 생성
grouped1 = df.groupby(['class'])
grouped2 = df.groupby(['class', 'sex'])
for key, group in grouped1:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('\n')
# 개별 그룹 선택
grouped1.get_group('Third')
grouped2.get_group(('Third', 'female'))  # 튜플인수

# # 그룹객체 연산
grouped1.mean()
grouped2.mean()
grouped2['fare'].std()
# 사용자정의 함수 적용
grouped1.agg(min_max)
# 여러 함수를 각 열에 동일하게 적용할 때는 리스트 인수 전달
grouped1.agg(['min', 'max', min_max])
# 각 열마다 다른 함수를 적용할 때는 딕셔너리 인수 전달
grouped1.agg({'fare': ['min', 'max'], 'age': 'mean'})
# 원본 데이터프레임의 형태로 결과 반환(연산이 가능한 열만)
grouped1.transform(min_max)
# 그룹핑된 개별 원소에 함수를 일대일로 매핑
grouped1.age.apply(min_max)
grouped1.age.apply(lambda x: x.min())
grouped1.apply(lambda x: x.describe())
grouped1.apply(lambda x: len(x) >= 200)
# 그룹객체 필터링: 조건만족하는 그룹만 남김
grouped1.filter(lambda x: len(x) >= 200)

# # 멀티 인덱스 ----------

gdf = grouped2.mean()
print(gdf)

print(gdf.loc['First'])
print(gdf.loc[('First', 'male')])   # 튜플인수
print(gdf.xs('male', level='sex'))  # xs 인덱서

# # 피벗 ----------

print(df.head())
pdf = pd.pivot_table(df,
                     index=['class', 'sex'],
                     columns='survived',
                     values=['age', 'fare'],
                     aggfunc=['mean', 'max'])
print(pdf.head())
print(pdf.index)
print(pdf.columns)

# xs 인덱서 사용(행선택 axis=0)
print(pdf.xs('First'))
print(pdf.xs(('First', 'female')))
print(pdf.xs('male', level='sex'))
print(pdf.xs(('Second', 'male'), level=[0, 'sex']))

# xs 인덱서 사용(열선택 axis=1)
print(pdf.xs('mean', axis=1))
print(pdf.xs(('mean', 'age'), axis=1))
print(pdf.xs(1, level='survived', axis=1))
print(pdf.xs(('max', 'fare', 0), level=[0, 1, 2], axis=1))


#######################################
# 머신러닝
#######################################

# # 머신러닝 프로세스
# 데이터 정리 - 데이터분리(훈련,검증) - 알고리즘준비 - 모형학습(훈련) - 예측(검증) - 모형평가 - 모형활용
# 소득이 증가(독립변수x)하면 소비가 증가(종속변수y)한다:  x가 주어지면 y를 예측할 수 있다
# 모형이 예측을 위해 사용하는 변수(x): 독립변수, 설명변수
# 모형이 예측하고자하는 변수(y): 종속변수, 예측변수

# ========================
# 예측(지도학습, 회귀분석)
# ========================

# # 단순회귀분석 ----------
# y = ax + b 에서 a와 b를 찾기 위한 여정

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./trainingdata/machine/auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']
print(df.head())
print(df.info())
print(df.describe())

# # 전처리
# horsepower 열의 자료형 변경 (문자열 ->숫자)
print(df['horsepower'].unique())                         # horsepower 열의 고유값 확인
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환
print(df.describe())                                     # 데이터 통계 요약정보 확인

# # 종속변수(mpg)와 독립변수후보군(cylinders, horsepower, weight) 선정
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())
# 종속변수 mpg 와 다른 변수간 선형 관계 확인
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
# seaborn으로 그리기
sns.regplot(x='weight', y='mpg', data=ndf)    # 분포된 형태가 선형보다는 비선형에 가까움
sns.jointplot(x='weight', y='mpg', data=ndf)
sns.pairplot(ndf)
# 후보군확정: 선형관계와 무관한 cylinders 제외

# # 훈련 및 검증 데이터셋 분리
X = ndf[['weight']]  # 독립 변수 X
y = ndf['mpg']       # 종속 변수 Y
# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,                # 독립 변수
                                                    y,                # 종속 변수
                                                    test_size=0.3,    # 검증 30%
                                                    random_state=10)  # 랜덤 추출 값
print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)

# # 단순회귀분석 모형 적용
from sklearn.linear_model import LinearRegression
# 모형 객체 생성
lr = LinearRegression()
# 훈련데이터셋으로 모형 학습
lr.fit(X_train, y_train)
# 검증데이터셋으로 결정계수(R-제곱) 산출: 결정계수값이 클수록 모형예측능력 우수
r_square = lr.score(X_test, y_test)
print(r_square)
# 기울기 산출
print('기울기 a: ', lr.coef_)
# y절편 산출
print('y절편 b', lr.intercept_)

# # 모형 평가(예측값 y_hat, 실제값 y 비교)
y_hat = lr.predict(X)
# 비교 그래프 출력
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()

# # 다항회귀분석 ----------
# 2차 이상의 함수를 이용(2차 함수는 y= ax2 + bx + c 에서 a, b, c를 찾는 과정)

# # 다항회귀분석 모형 적용
from sklearn.linear_model import LinearRegression      # 선형회귀분석
from sklearn.preprocessing import PolynomialFeatures   # 다항식 변환
# 모형 객체 생성
poly = PolynomialFeatures(degree=2)          # 2차항 적용
X_train_poly = poly.fit_transform(X_train)   # X_train 데이터를 2차항으로 변형
print('원 데이터: ', X_train.shape)
print('2차항 변환 데이터: ', X_train_poly.shape)
# 모형 학습
pr = LinearRegression()
pr.fit(X_train_poly, y_train)
# 결정계수(R-제곱) 산출
X_test_poly = poly.fit_transform(X_test)     # X_test 데이터를 2차항으로 변형
r_square = pr.score(X_test_poly, y_test)
print(r_square)

# # 모형 평가
# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat_test = pr.predict(X_test_poly)
# 비교 그래프 출력
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(X_train, y_train, 'o', label='Train Data')          # 데이터 분포
ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value')  # 모형이 학습한 회귀선
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()
# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 그래프 출력
X_ploy = poly.fit_transform(X)
y_hat = pr.predict(X_ploy)
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()
# 그래프로 판단할 때 단순회귀분석보단 더 적합한 모형으로 볼 수 있음

# # 다중회귀분석 ----------
# 소득이 증가 뿐만아니라 거주지, 자녀수 등 소비에 영향을 주는 다양한 독립변수를 고려함
# y = b + a1x1 + a2x2 + ... + anxn 에서 a1, a2, ... an, b 를 찾는 과정

# # 변수 선정
X = ndf[['cylinders', 'horsepower', 'weight']]  # 독립 변수 X1, X2, X3
y = ndf['mpg']                                  # 종속 변수 Y

# # 데이터셋 분리(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)

# # 다중회귀분석 모형 적용
from sklearn.linear_model import LinearRegression
# 모형 객체 생성
lr = LinearRegression()
# 모형 학습
lr.fit(X_train, y_train)
# 결정계수(R-제곱) 산출
r_square = lr.score(X_test, y_test)
print(r_square)
# 회귀식의 기울기
print('X 변수의 계수 a: ', lr.coef_)
# 회귀식의 y절편
print('상수항 b', lr.intercept_)

# # 모형 평가
# 예측회귀선 그래프로출력
y_hat = lr.predict(X_test)
# 비교 그래프 출력
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y_test, label="y_test")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()

# ========================
# 분류(지도학습)
# ========================
# 범주형 y 값을 예측하는 모형

# # KNN ----------
# 적절한 k 값을 찾고, 이웃하는 원소들 중 다수를 차지하는 분류값을 따름

# # 전처리: 탑승객의 생존여부를 예측하는 모형 만들기
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
print(df.info())

# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)
# age 열에 나이 데이터가 없는 모든 행을 삭제(891개 중 177개의 NaN 값)
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))
# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(rdf.describe(include='all'))  # embarked 열의 최빈값(top) 재확인
rdf['embarked'].fillna(most_freq, inplace=True)
print(rdf.info())

# # 변수 선정
# 예측변수(survived)와 설명변수 후보6개(pclass, sex, age, sibsp, parch, embarked) 로 데이터를 구성
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())
# 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head())

X = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]  # 독립 변수 X
y = ndf['survived']                                                                           # 종속 변수 Y

# 설명변수 데이터를 정규화(normalization)
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# # 데이터셋 분리(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련데이터: ', X_train.shape)
print('검증데이터: ', X_test.shape)

# # KNN 분류 모형 적용
from sklearn.neighbors import KNeighborsClassifier
# 모형 객체 생성 (k=5로 설정)
knn = KNeighborsClassifier(n_neighbors=5)
# 모형 학습
knn.fit(X_train, y_train)
# test data를 가지고 y_hat을 예측(분류)
y_hat = knn.predict(X_test)
# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# # 모형 평가
from sklearn import metrics
# Confusion Matrix 출력
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)
# [[TN, FP], [FN, TP]] 형태로 결과 반환
# 미생존바른예측 110(True Negative), 미생존을생존오류 15(False Positive), 생존을미생존오류 26, 생존정확예측 64

# 모형성능 평가지표 출력
knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)
# precision(정확도): True로 예측하여 실제 True인 비율, 높을수록 오류가 적음
# recall(재현율): 실제 True를 True로 예측한 비율, 높을수록 오류가 적음
# f1-score(예측정확도): 정확도와 재현율의 조화평균을 계산한 값, 높을수록 예측력이 좋음
# support(개체수)

# KNN모형평가: 미생존자(0) 예측정확도가 0.84, 생존자(1) 예측정확도가 0.76으로 예측 능력의 차이가 있음

# # SVM 분류 모형 ----------

# 데이터프레임의 속성(열)별로 벡터를 구성하여 2개열은 2차원, 3개열은 3차원...의 공간좌표를 구성하고
# 같은 분류값을 가지는 데이터끼리 같은 공간에 배치하여, 새로운 데이터의 공간위치로 분류 영역을 예측

# # 모형 적용
from sklearn import svm
# 모형 객체 생성 (kernel='rbf' 적용)
svm_model = svm.SVC(kernel='rbf')  # 커넬옵션: linearm polynimial, sigmoid 등
# 모형 학습
svm_model.fit(X_train, y_train)
# test data를 가지고 y_hat을 예측(분류)
y_hat = svm_model.predict(X_test)
# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# # 모형 평가
from sklearn import metrics
# Confusion Matrix 출력
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)
# 미생존정확예측 120(True Negative), 미생존을생존오류 5(False Positive), 생존을미생존오류 35, 생존정확예측 55

# 모형성능 평가지표 출력
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)

# SVM모형평가: 미생존자(0) 예측정확도가 0.86, 생존자(1) 예측정확도가 0.73으로 KMM모형과 유사함

# # Decisin Tree 분류 모형 ----------

# 속성별 분기점마다 최적의 선택이 이루어지도록 구성

from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np

# # 전처리: Breast Cancer 데이터셋
df = pd.read_csv('./trainingdata/machine/breast-cancer-wisconsin.csv', header=None)
df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']
print(df.head())
print(df.describe())
print(df.info())
# 유일한 문자형이며 결손값이 있는 bare_nuclei 열 전처리
print(df['bare_nuclei'].unique())
df['bare_nuclei'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int')       # 문자열을 정수형으로 변환
print(df.describe())                                      # 데이터 통계 요약정보 확인

# # 변수 선정
X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']]  # 설명 변수 X
y = df['class']                                                     # 예측 변수 Y
# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# # 데이터셋 분리(7:3 비율)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련데이터: ', X_train.shape)
print('검증데이터: ', X_test.shape)

# # Decision Tree 분류 모형 적용
from sklearn import tree
# 모형 객체 생성 (criterion='entropy', 트리레벨은 '5'로 지정)
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)
# 모형 학습
tree_model.fit(X_train, y_train)
# test data를 가지고 y_hat을 예측(분류)
y_hat = tree_model.predict(X_test)      # 2: benign(양성), 4: malignant(악성)
# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# # 모형 평가
# Confusion Matrix 출력
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix)

# 모형성능 평가지표 출력
tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)
# 양성예측정확도는 0.98, 악성예측정확도는 0.96으로 평균 0.97의 정확도를 가짐

# ========================
# 군집(비지도학습)
# ========================

# 비지도학습으로 예측변수도 학습과정도 없으며, 필요한 변수를 모두 설명변수로 활용

# # K-Means 모형 ----------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./trainingdata/machine/customer.csv')
print(df.head())
print(df.info())
print(df.describe())

# # 변수 선정
X = df.iloc[:, :]
print(X[:5])

# 설명 변수 데이터를 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)
print(X[:5])

# # k-means 군집 모형 적용
from sklearn import cluster
# 모형 객체 생성: 8개의 속성을 이용하여 5개의 클러스터로 관측값을 분류
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)
# 모형 학습
kmeans.fit(X)
# 예측(군집): 모형의 예측값은 매번 달라짐
cluster_label = kmeans.labels_
print(cluster_label)

# # 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())

# 그래프로 표현: 시각화(8개의 변수를 하나씩 그려보아야 함)
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
        colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
        colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

# 지나치게 큰 값으로 구성된 클러스터(0, 4)를 제외: 값이 몰려 있는 구간을 자세하게 분석
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]

ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
         colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
         colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

# # DBSCAN ----------
# 데이터가 위치한 공간 밀집도를 기준으로 클러스터를 구분

import pandas as pd
import folium

# # 전처리: 서울시내 중학교 진학률 데이터셋
df = pd.read_excel('./trainingdata/machine/middle_shcool_report.xlsx', engine='openpyxl', header=0, index_col=0)
print(df.columns.values)
print(df.head())
print(df.info())
print(df.describe())

# 지도에 위치 표시
mschool_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain', zoom_start=12)

# 중학교 위치정보를 CircleMarker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
    folium.CircleMarker([lat, lng],
                        radius=5,              # 원의 반지름
                        color='brown',         # 원의 둘레 색상
                        fill=True,
                        fill_color='coral',    # 원을 채우는 색
                        fill_opacity=0.7,      # 투명도
                        popup=name
                        ).add_to(mschool_map)

# 지도를 html 파일로 저장
mschool_map.save('./seoul_mschool_location.html')

# 문자열데이터를 더미변수로 전환(원핫인코딩)
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()     # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder()   # one hot encoder 생성

onehot_location = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day
print(df.head())

# # 변수 선정
from sklearn import cluster
# 분석에 사용할 속성을 선택 (과학고, 외고국제고, 자사고 진학률)
columns_list = [9, 10, 13]
X = df.iloc[:, columns_list]
print(X[:5])

# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# # DBSCAN 군집 모형 적용
# 모형 객체 생성
dbm = cluster.DBSCAN(eps=0.2, min_samples=5)
# 모형 학습
dbm.fit(X)
# 예측(군집): -1은 Noise를 나타내고 클러스터는 0,1,2,3으로 모두 4개가 됨
cluster_label = dbm.labels_
print(cluster_label)

# # 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())

# 클러스터 값으로 그룹화하고, 그룹별로 내용 출력 (첫 5행만 출력)
grouped_cols = [0, 1, 3] + columns_list
grouped = df.groupby('Cluster')
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped_cols].head())
    print('\n')
# 클러스터(key) -1은 Noise로 255개
# 클러스터(key) 0은 102개로 외고와 자사고 합격률은 높지만 과학고 합격자는 없음
# 클러스터(key) 1은 45개로 자사고 합격자만 존재
# 클러스터(key) 2는 8개로 자사고 합격률 매우 높으며, 외고와 과학고 합격자도 존재
# 클러스터(key) 3은 5개로 자사고 합격자가 있으며, 과학고 합격자는 없고 외고합격률이 매우 낮음

# 그래프로 표현 - 시각화
colors = {-1: 'gray', 0: 'coral', 1: 'blue', 2: 'green', 3: 'red', 4: 'purple',
          5: 'orange', 6: 'brown', 7: 'brick', 8: 'yellow', 9: 'magenta', 10: 'cyan', 11: 'tan'}
cluster_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                         zoom_start=12)
for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도
                        popup=name
                        ).add_to(cluster_map)

# 지도를 html 파일로 저장하기
cluster_map.save('./seoul_mschool_cluster.html')

# # 변수 추가: X2 데이터셋에 대하여 위의 과정을 반복(과학고, 외고국제고, 자사고 진학률 + 재단유형(국,공,사립))
columns_list2 = [9, 10, 13, 22]
X2 = df.iloc[:, columns_list2]
print(X2[:5])

X2 = preprocessing.StandardScaler().fit(X2).transform(X2)
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm2.fit(X2)
df['Cluster2'] = dbm2.labels_

grouped2_cols = [0, 1, 3] + columns_list2
grouped2 = df.groupby('Cluster2')
for key, group in grouped2:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped2_cols].head())
    print('\n')

cluster2_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                          zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도
                        popup=name
                        ).add_to(cluster2_map)

# 지도를 html 파일로 저장하기(11개의 클러스터 생성)
cluster2_map.save('./seoul_mschool_cluster2.html')

# # 변수 추가: X3 데이터셋에 대하여 위의 과정을 반복(과학고, 외고_국제고)
columns_list3 = [9, 10]
X3 = df.iloc[:, columns_list3]
print(X3[:5])

X3 = preprocessing.StandardScaler().fit(X3).transform(X3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(X3)
df['Cluster3'] = dbm3.labels_

grouped3_cols = [0, 1, 3] + columns_list3
grouped3 = df.groupby('Cluster3')
for key, group in grouped3:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped3_cols].head())
    print('\n')

cluster3_map = folium.Map(location=[37.55, 126.98], tiles='Stamen Terrain',
                          zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):
    folium.CircleMarker([lat, lng],
                        radius=5,                   # 원의 반지름
                        color=colors[clus],         # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus],    # 원을 채우는 색
                        fill_opacity=0.7,           # 투명도
                        popup=name
                        ).add_to(cluster3_map)

# 지도를 html 파일로 저장하기(클러스터 7개 생성)
cluster3_map.save('./seoul_mschool_cluster3.html')
