from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import urllib

keyword_input = '블루스캔'
start_date = '2021.04.01'
end_date = '2022.03.31'

sd = start_date.replace('.','')
ed = end_date.replace('.','')
keyword = urllib.parse.quote(keyword_input)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r'D:/2022/_Py/_common/chromedriver.exe', chrome_options=options)
url = rf"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22{keyword}%22&oquery=%22%EB%B8%94%EB%A3%A8%EC%8A%A4%EC%BA%94%22&tqi=hDQsCdp0Jywssl88giGsssssshN-194891&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de={end_date}&ds={start_date}&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0"

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
    if len(i.text) == 11: date.append(i.text)
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
