import pandas as pd
import datetime
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', family = 'malgun gothic')

trend_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            skiprows=6,
            parse_dates = ['날짜'])

asset_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name = '블루에셋',
            usecols='B:E',
            parse_dates = ['기사날짜'])

scan_df = pd.read_excel(
            'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name = '블루스캔',
            usecols='B:E',
            parse_dates = ['기사날짜'])

asset_count = asset_df['기사날짜'].value_counts(dropna = False)
scan_count = scan_df['기사날짜'].value_counts(dropna = False)
new_df = pd.merge(trend_df, asset_count, how='outer', left_on='날짜', right_index=True)
new_df = pd.merge(new_df, scan_count, how='outer', left_on='날짜', right_index=True)
new_df.columns = ['날짜', '블루스캔', '블루에셋', '에셋기사건수', '스캔기사건수']
new_df.fillna(0, inplace=True)

new_df.to_excel('c:/Users/Administrator/Desktop/에스원_동향.xlsx',
            sheet_name='취합')

# # 시각화 ------------------
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(new_df['날짜'], new_df['블루에셋'], color='blue')
ax1.set_ylabel('네이버 트랜드 추이(%)')
ax1.set_ylim(0, 100)
ax1.grid(True)
ax1.set_title('블루에셋 검색추이')

ax2.plot(new_df['날짜'], new_df['블루스캔'], color='magenta')
ax2.set_ylim(0, 100)
ax2.grid(True)
ax2.set_title('블루스캔 검색추이')

ax3.bar(new_df['날짜'], new_df['에셋기사건수'], color='blue')
ax3.set_ylabel('기사건수(개)')
ax3.set_ylim(0, 5)
ax3.grid(True)
ax3.set_title('블루에셋 기사건수')

# ax4.set_ylim(0, 5)
ax4.bar(new_df['날짜'], new_df['스캔기사건수'], color='magenta')
ax4.set_ylim(0, 5)
ax4.grid(True)
ax4.set_title('블루스캔 기사건수')

plt.suptitle("'검색 트랜드'와 '기사 건수'간 상관성", fontsize=20)
plt.show()
