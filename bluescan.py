"""
블루스캔
220421
"""


# # 스크롤 ----------

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import urllib

keyword_input = '블루에셋'
keyword_except = '스카이블루에셋'
start_date = '2021.01.01'
end_date = '2021.12.31'

sd = start_date.replace('.', '')
ed = end_date.replace('.', '')
keyword = urllib.parse.quote(keyword_input)
keyword2 = urllib.parse.quote(keyword_except)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r'D:/2022/_Py/_common/chromedriver.exe', chrome_options=options)
url = rf"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22{keyword}%22+-%22{keyword2}%22&oquery=%22{keyword}%22&tqi=hDQsCdp0Jywssl88giGsssssshN-194891&nso=so%3Ar%2Cp%3Afrom{sd}to{ed}%2Ca%3Aall&de={end_date}&ds={start_date}&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0"
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = bs(html, 'html.parser')
agency = []
date = []
title = []
link = []
for i in driver.find_elements_by_css_selector('.info.press'):
    agency.append(i.text)
for i in driver.find_elements_by_css_selector('span.info'):
    if len(i.text) == 11:
        date.append(i.text)
for i in driver.find_elements_by_css_selector('div.news_wrap.api_ani_send > div > a'):
    title.append(i.text)
for i in driver.find_elements_by_css_selector('div.news_wrap.api_ani_send > div > a'):
    link.append(i.get_attribute('href'))

# 페이지 반복 ----------

while driver.find_element_by_css_selector('a.btn_next').get_attribute('aria-disabled') == 'false':
    # 클릭 후 스크랩핑
    driver.find_element_by_css_selector('a.btn_next').click()
    time.sleep(3)
    html = driver.page_source
    soup = bs(html, 'html.parser')
    for i in driver.find_elements_by_css_selector('.info.press'):
        agency.append(i.text)
    for i in driver.find_elements_by_css_selector('span.info'):
        if len(i.text) == 11: date.append(i.text)
    for i in driver.find_elements_by_css_selector('div.news_wrap.api_ani_send > div > a'):
        title.append(i.text)
    for i in driver.find_elements_by_css_selector('div.news_wrap.api_ani_send > div > a'):
        link.append(i.get_attribute('href'))

# 최종 작업 ----------

df = pd.DataFrame({'언론사명': agency, '기사날짜': date, '제목': title, 'URL': link})
df.sort_values(by='기사날짜', ascending=True, inplace=True, ignore_index=True)
df.index = df.index + 1
with pd.ExcelWriter("C:/Users/Administrator/Desktop/{}.xlsx".format(keyword_input)) as writer:
    df.to_excel(writer)
time.sleep(1)
driver.close()


# # 판다스 ----------

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
ax1.set_xlim(new_df['날짜'].min()-pd.Timedelta(days=5), new_df['날짜'].max()+pd.Timedelta(days=5))
ax1.set_ylim(0, 100)
ax1.grid(True)
ax1.set_title('블루에셋 검색추이')

ax2.plot(new_df['날짜'], new_df['블루스캔'], color='magenta')
ax2.set_xlim(new_df['날짜'].min()-pd.Timedelta(days=5), new_df['날짜'].max()+pd.Timedelta(days=5))
ax2.set_ylim(0, 100)
ax2.grid(True)
ax2.set_title('블루스캔 검색추이')

ax3.bar(new_df['날짜'], new_df['에셋기사건수'], color='blue')
ax3.set_ylabel('기사건수(개)')
ax3.set_xlim(new_df['날짜'].min()-pd.Timedelta(days=5), new_df['날짜'].max()+pd.Timedelta(days=5))
ax3.set_ylim(0, 5)
ax3.grid(True)
ax3.set_title('블루에셋 기사건수')

ax4.bar(new_df['날짜'], new_df['스캔기사건수'], color='magenta')
ax4.set_xlim(new_df['날짜'].min()-pd.Timedelta(days=5), new_df['날짜'].max()+pd.Timedelta(days=5))
ax4.set_ylim(0, 5)
ax4.grid(True)
ax4.set_title('블루스캔 기사건수')

plt.suptitle("'검색 트랜드'와 '기사 건수'간 상관성", fontsize=20)
plt.show()
