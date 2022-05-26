import pandas as pd
import datetime
import re


# # 데이터 로딩 ----------
df = pd.read_excel('c:/Users/Administrator/Desktop/2022.xlsx')
df.shape      # 총데이터수 18,907개

# 결측치 확인
missing_df = df.isnull()
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()
    try:
        print(col, ': ', missing_count[True])
    except BaseException:
        print(col, ': ', 0)

# # 데이터 정제

# 특정 기록자 제외
ndf = df[~df.확인자.str.contains('점검조|테스트', na=False)]
ndf = ndf[~ndf.처리자.str.contains('점검조|테스트', na=False)]
ndf.shape     # 잔여데이터 17,887개

# 통신단절 제외
ndf = ndf[~ndf.경보명.str.contains('통신단절|Disconnect|Timeout', na=False)]
ndf.shape     # 잔여데이터 17,026개

# 리테일 제외
ndf = ndf[~df.경보명.str.contains('(GS수퍼|EMS)')]
ndf.shape     # 잔여데이터 2,419개

# 동일자 발생알람 제외
ndf['n발생일자'] = ndf['발생일시'].str[0:10]
ndf = ndf.drop_duplicates(subset=['경보명', 'n발생일자'])
ndf.shape     # 잔여데이터 1,211개


# # 데이터 샘플링 ----------

ndf2 = ndf[['경보명', '발생일시', '확인일시', '처리내용']]
ndf2.head(2)
ndf2.dtypes
ndf2['발생일시'] = ndf2['발생일시'].apply(pd.to_datetime)
ndf2['확인일시'] = ndf2['확인일시'].apply(pd.to_datetime)
ndf2.set_index('발생일시', drop=False, inplace=True)
ndf2.shape

# 선형적 기간 집계
day_count = ndf2['경보명'].resample('D').count()
month_count = ndf2['경보명'].resample('M').count()

# 순환적 집계
week_count = ndf2.index.weekday.value_counts().sort_index()
hour_count = ndf2.index.hour.value_counts().sort_index()

# 시각화
import calplot
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="D:/2022/_Py/data/malgun.ttf").get_name()
rc('font', family=font_name)

calplot.calplot(day_count, cmap='YlGn')
day_count.plot(kind='area')
month_count.plot(kind='bar')
week_count.plot(kind='bar', xlabel='Mon(0) ~ Sun(6)')
hour_count.plot(kind='bar')

import seaborn as sns
ndf2['week'] = ndf2.index.day_name()
ndf2['hour'] = ndf2.index.hour
ndf_week_hour = ndf2.groupby(['week', 'hour']).size()
ndf_table = ndf_week_hour.rename_axis(['Weekday', 'Hour']).unstack('Weekday')
days=['Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
ndf_table_sort = ndf_table.reindex(columns=days)
sns.heatmap(ndf_table_sort)

# 일별 시계열 분해
from statsmodels.tsa.seasonal import seasonal_decompose
ts = ndf2['경보명'].resample('D').count()
result = seasonal_decompose(ts, model='Additive')
result.plot()
plt.show()

# k = ndf2.경보명.str.extract(r'(.+)_(.+)_(.+)').get(1).value_counts()
