"""
네이버 검색어 스크랩
220422
"""


# # 스크롤 ----------

import requests
from bs4 import BeautifulSoup as bs
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22%EB%B8%94%EB%A3%A8%EC%8A%A4%EC%BA%94%22&oquery=%22%EB%B8%94%EB%A3%A8%EC%8A%A4%EC%BA%94%22&tqi=hE5g9sp0YiRss4K5%2FDRssssstPs-396289&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de=2022.03.31&ds=2021.04.01&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0'
res = requests.get(url, verify=False).text
soup = bs(res, 'html.parser')






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

# 검색없는 단어 테스트용
# url ='https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22111%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22&oquery=%22%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22&tqi=hEiU1dp0YidssUKfUKVssssstaV-304742&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de=2022.03.31&ds=2021.04.01&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0'

driver.get(url)
time.sleep(3)
html = driver.page_source
soup = bs(html, 'html.parser')

# 변수정의 ----------
t_press = []
t_date = []
t_title = []
t_link = []
t_relatenews = []

# 뉴스페이지스크랩 ----------
def newspage_scrap():
    # 메인뉴스
    for i in soup.select('div.info_group a.info.press'):
        t_press.append(i.text)
    for i in soup.select('div.info_group span.info'):
        if i.text[0:2] == '20':
            t_date.append(i.text)
    for i in soup.select('div.news_area > a'):
        t_title.append(i.text)
    for i in soup.select('div.news_area > a'):
        t_link.append(i.get('href'))

    # 서브뉴스
    for i in soup.select('cite.sub_txt.press'):
        t_press.append(i.text)
    for i in soup.select('span.sub_txt'):
        if i.text[0:2] == '20':
            t_date.append(i.text)
    for i in soup.select('span.sub_wrap > a'):
        t_title.append(i.text)
    for i in soup.select('span.sub_wrap > a'):
        t_link.append(i.get('href'))

    # 관련뉴스
    for i in soup.select('a.news_more'):
        t_relatenews.append('https://search.naver.com/search.naver' + i.get('href'))

# 페이지 반복 ----------
if driver.find_element_by_css_selector('a.btn_next') == "":
    print("해당 단어의 검색 뉴스가 없습니다.")
else:
    newspage_scrap()
    while driver.find_element_by_css_selector('a.btn_next').get_attribute('aria-disabled') == 'false':
        driver.find_element_by_css_selector('a.btn_next').click()
        time.sleep(3)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        newspage_scrap()

# 연관뉴스 반복 ----------
if len(t_relatenews) > 0:
    for iurl in t_relatenews:
        url = iurl
        res = requests.get(url, verify=False).text
        soup = bs(res, 'html.parser')
        ??? "와일문 반복"


# 데이터프레임 저장 ----------
df = pd.DataFrame({'언론사명': t_press, '기사날짜': t_date, '제목': t_title, 'URL': t_link})
df.sort_values(by='기사날짜', ascending=True, inplace=True, ignore_index=True)
??? "중복제거"
df.index = df.index + 1
with pd.ExcelWriter("C:/Users/Administrator/Desktop/{}.xlsx".format(keyword_input)) as writer:
    df.to_excel(writer)
time.sleep(1)
driver.close()

