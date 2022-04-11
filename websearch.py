from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r'D:/2022/_Py/_common/chromedriver.exe', chrome_options=options)
# url = r"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22+-%EC%8A%A4%EC%B9%B4%EC%9D%B4%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B&oquery=%22%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22&tqi=hCYrfwprvhGssPSG7X4ssssst4N-298993&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de=2022.03.31&ds=2021.04.01&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0"
url = r"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22%EB%B8%94%EB%A3%A8%EC%8A%A4%EC%BA%94%22&oquery=%EB%B8%94%EB%A3%A8%EC%8A%A4%EC%BA%94&tqi=hC0hLsp0J14sse1RDMZssssssXw-072133&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de=2022.03.31&ds=2021.04.01&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0"
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = bs(html, 'lxml')

data_lst = []
for i in range(1, 11):
    try:
        n_agency = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/div[1]/div[2]/a[1]')
        n_date = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/div[1]/div[2]/span[2]')
        n_title = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/a')

    except NoSuchElementException:
        n_agency = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/div[1]/div[2]/a[1]')
        n_date = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/div[1]/div[2]/span')
        n_title = driver.find_element_by_xpath(f'//*[@id="sp_nws{i}"]/div/div/a')
    data_lst.append([n_agency.text, n_date.text, n_title.text, n_title.get_attribute('href')])

df = pd.DataFrame(data_lst, columns=['언론사명', '기사날짜', '제목', 'URL'])
with pd.ExcelWriter("C:/Users/Administrator/Desktop/블루스캔동향.xlsx") as writer:
    df.to_excel(writer)

time.sleep(1)
driver.close()
