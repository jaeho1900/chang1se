import pandas as pd
import datetime
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', family='malgun gothic')

df = pd.read_excel('c:\\Users\\Administrator\\Desktop\\2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.columns

df['건물'].nunique()
df['건물군'].unique()

df1 = pd.DataFrame(df, columns=df.columns)
df1.pivot(['건물군', '건물'], '발생일시', '상태')


df_pivot = pd.pivot_table(df,
            index='건물',               # 행 위치에 들어갈 열
            values='발생일시',                 # 데이터로 사용할 열
            aggfunc='count',  # 데이터 집계 함수 (디폴트는 'mean')
            fill_value=0,                          # NaN 채우기
            margins=True,                          # 행별,열별 합계
            margins_name='합계')
print()


n = 7
h = n // 2
print(h)
while h > 0:
    h //= 2
    print(h)
