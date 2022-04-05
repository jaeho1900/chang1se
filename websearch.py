from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22+-%EC%8A%A4%EC%B9%B4%EC%9D%B4%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B&oquery=%22%EB%B8%94%EB%A3%A8%EC%97%90%EC%85%8B%22&tqi=hCYrfwprvhGssPSG7X4ssssst4N-298993&nso=so%3Ar%2Cp%3Afrom20210401to20220331%2Ca%3Aall&de=2022.03.31&ds=2021.04.01&mynews=0&office_section_code=0&office_type=0&pd=3&photo=0&sort=0"
html = urlopen(url).read()
print(html)

soup = bs(html, 'lxml')
print(soup)


print(soup.select('a').text)
print(soup.select('a').stripped_strings)



soup.select_one('p')                     # 태그명
soup.select_one('#footer')               # #id
soup.select_one('.gift')                 # .class
soup.select_one('tr.gift')
soup.select_one('tr[class = "gift"]')
soup.select_one('img[src ^= "./"]')
soup.select_one('img[src *= "file"]')
soup.select_one('img[src $= "jpg"]')
soup.select_one('tbody > tr.gift')       # 직계 자손
soup.select_one('tbody  tr.gift')        # 모든 자손
soup.select_one('table > tbody > tr.gift')
soup.select_one('html #gift1.gift')
soup.select_one('html img[src*="file"]')
soup.select_one('#giftList td:nth-child(3)')   #n번째
soup.select('#gift1 > td')[2]
print(list(soup.select('#gift1 > td')[2]))
# 태그명             태그명과 일치하는 태그 선택
# #                 id="~~"인 태그 선택
# .                 class="~~"인 태그 선택
# [속성="속성text"]  속성="~~" 태그 선택 (=, ^=, *=, $= 등부호 활용)
# >                 직계자손 태그 선택
# :nth-child(n)     n번째 태그 선택

