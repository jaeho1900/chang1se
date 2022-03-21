"""
가맹사업거래 정보공개서 수집 프로그램
2021.7.28
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib3
import csv
import re
import pandas as pd
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 전체 페이지 수 계산

url = 'https://franchise.ftc.go.kr/mnu/00013/program/ \
       userRqst/list.do?searchCondition=&searchKeyword=&column=& \
       selUpjong=&selIndus=&pageUnit=10&pageIndex=1'
hpage = urlopen(url)
bs = BeautifulSoup(hpage, 'lxml')
print(bs.prettify())

endi = bs.find('table').tbody.tr.td.get_text()

url = 'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/ \
       list.do?searchCondition=&searchKeyword=&column=brd&selUpjong= \
       &selIndus=&pageUnit={}&pageIndex=1'.format(endi)
hpage = urlopen(url)
bs = BeautifulSoup(hpage, 'lxml')

rowi = len(bs.findAll('a', {'class': 'authCtrl'}))

for i in tqdm(range(1, rowi, 2)):
    sleep(0.0001)
    klist.append(
        len(bs.findAll('a', {'onclick': re.compile('fn_view')}))
        .attrs.split('=')[1].split("'")[0])

klist = []
for i in bs.findAll(onclick=re.compile('fn_view')):
    klist.append(str(i).split('=')[4].split("'")[0])

str(bs.findAll(onclick=re.compile('fn_view'))[2]).split('=')[4].split("'")[0]

# #--------------------
# ## 임시 저장
# df = pd.DataFrame(klist)
# df.to_excel("output_klist.xlsx")

# ## 임시 저장 호출
# df = pd.read_excel('output_klist.xlsx', usecols='B', header=0)
# klist = list(df[0])
# len(klist)
# #--------------------

# 개별 페이지 정보 저장

# 컬럼명 파일 저장
title = ['상호', '영업표지', '대표자', '업종', '사업자등록일', '대표번호',
         '최종등록일', '주소', '년도1', '전체1', '가맹점수1', '직영점수1',
         '년도2', '전체2', '가맹점수2', '직영점수2']
with open('output_result.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(title)

for contenti in range(0, len(klist)):

    url = 'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/ \
           view.do?firMstSn={}'.format(klist[contenti])
    url = 'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/ \
           view.do?firMstSn=16342'
    hpage = urlopen(url)
    bs = BeautifulSoup(hpage, 'lxml')
    crawlist = ["list(bs.findAll('table')[0].tbody.tr.stripped_strings)[1]",
                "list(bs.findAll('table')[0].tbody.tr.stripped_strings)[3]",
                "list(bs.findAll('table')[0].tbody.tr.stripped_strings)[5]",
                "list(bs.findAll('table')[0].tbody.tr.stripped_strings)[6]",
                "list(bs.findAll('table')[0].tbody.findAll('tr')[2]. \
                      stripped_strings)[1]",
                "list(bs.findAll('table')[0].tbody.findAll('tr')[2] \
                      .stripped_strings)[2]",
                "list(bs.findAll('table')[0].tbody.findAll('tr')[4] \
                      .stripped_strings)[2]",
                "list(bs.findAll('table')[1].tbody.td.stripped_strings)[0]",
                "list(bs.findAll('table')[6].tr.stripped_strings)[1]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [1]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [2]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [3]",
                "list(bs.findAll('table')[6].tr.stripped_strings)[2]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [4]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [5]",
                "list(list(bs.findAll('table')[6].tbody.tr.stripped_strings)) \
                 [6]"]


list(bs.findAll('table')[0].tbody.tr.stripped_strings)[1]

list(bs.find('h6', text='가맹본부 일반 현황').descendants).find(text='영업표지').string
bs.find('h6', text='가맹점 및 직영점 현황 <span class="unit">단위 (개)</span>')

pagecontent = []
for rangei in range(1, 17):
    try:
        a = eval(crawlist[rangei-1])
    except BaseException:
        a = 0
    # 특수문자 제거
    # a = str(a).replace('\u2219', '').replace('\xa0', '')
    #     .replace('\u0101', '').replace('\xc9', '')
    pagecontent.append(a)

# 결과 저장
with open('output_result.csv', 'a', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(pagecontent)

# 진행 확인
print(contenti)

# END
