import pandas as pd
import datetime
import re

# 원시데이터 확인
df = pd.read_excel('c:/Users/Administrator/Desktop/2022.xlsx')
                   # parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.columns
df.shape

# 결측치 확인
missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    try:
        print(col, ': ', missing_count[True])
    except:
        print(col, ': ', 0)

# 리테일 자료 제외
df.head()
df.경보명.str.contains('(GS수퍼|EMS)').sum()
ndf = df[~df.경보명.str.contains('(GS수퍼|EMS)')]

# 발생일시 분리
ndf = ndf[['경보명', '발생일시', '처리내용']]
ndf.dtypes
ndf['발생일시'] = ndf['발생일시'].apply(pd.to_datetime)
ndf.set_index('발생일시', inplace=True)
ndf.shape

# 도수분포표
ndf.경보명.value_counts().head(20)
ndf[ndf.경보명 == 'LS타워_항온항습기1_누수감지기_동작']

# 요일별 발생건수
ndf.index.weekday.value_counts().sort_index(inplace=False).plot(
    kind='bar', xlabel=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

# 일별 발생건수
import calplot
calplot.calplot(ndf.resample('H')['경보명'].count())



k = df.groupby(by=['경보명', '시간']).count()

df['시간'] = df['발생시간'].dt.to_period(freq='H')

df[df.경보명 == 'LS타워_항온항습기1_누수감지기_동작']