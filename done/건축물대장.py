"""
_건축물대장 표제부 DB작업.py
2022.03.11
"""

import pandas as pd
import re

# 건축물대장 데이터 로딩

bookdb = pd.read_csv(
                '\\mart_djy_03.txt',
                sep='|',
                index_col=None,
                header=None,
                names=['PK', '대지위치', '건축물명칭',
                       '대지면적(㎡)', '건축면적(㎡)', '연면적(㎡)',
                       '주용도', '기타용도', '세대수',
                       '가구수', '지상층수', '지하층수',
                       '옥내기계식대수(대)', '옥내기계식면적(㎡)', '옥외기계식대수(대)',
                       '옥외기계식면적(㎡)', '옥내자주식대수(대)', '옥내자주식면적(㎡)',
                       '옥외자주식대수(대)', '옥외자주식면적(㎡)', '착공일',
                       '사용승인일'],
                usecols=[0, 5, 7, 25, 26, 28, 35, 36, 40, 41, 43, 44, 50, 51,
                         52, 53, 54, 55, 56, 57, 59, 60],
                encoding='CP949',
                na_values=['?', '??', 'N/A', 'NA', 'nan', 'NaN', '-nan',
                           '-NaN', 'null'],
                dtype={'대지면적(㎡)': float, '건축면적(㎡)': float, '건폐율': float,
                       '연면적(㎡)': float, '용적율산정연면적': float, '용적율': float,
                       '세대수': int, '가구수': int, '높이': float, '지상층수': int,
                       '지하층수': int, '옥내기계식대수(대)': int, '옥내기계식면적(㎡)': float,
                       '옥외기계식대수(대)': int, '옥외기계식면적(㎡)': float,
                       '옥내자주식대수(대)': int, '옥내자주식면적(㎡)': float,
                       '옥외자주식대수(대)': int, '옥외자주식면적(㎡)': float})

len(bookdb)
len(set(bookdb['주용도']))
bookdb['주용도'].value_counts()

# 그룹핑
grouped = bookdb.groupby(by='주용도')

# 그룹핑 결과 저장
bookdb['주용도'].value_counts().to_excel('\\주용도별데이터수.xlsx')

# 결과 저장
bookdb[bookdb.주용도 == '제1종근린생활시설'].to_excel('\\제1종근린생활시설.xlsx')
bookdb[bookdb.주용도 == '제2종근린생활시설'].to_excel('\\제2종근린생활시설.xlsx')
bookdb[bookdb.주용도 == '공장'].to_excel('\\공장.xlsx')
bookdb[bookdb.주용도 == '창고시설'].to_excel('\\창고시설.xlsx')
bookdb[(bookdb.주용도 != '제1종근린생활시설') &
       (bookdb.주용도 != '제2종근린생활시설') &
       (bookdb.주용도 != '단독주택') &
       (bookdb.주용도 != '공동주택') &
       (bookdb.주용도 != '공장') &
       (bookdb.주용도 != '창고시설')].to_excel('\\기타.xlsx')

# # 결과 저장(방법2)
# for key, group in grouped:
#     group.to_excel(f'{key}.xlsx')  # 백만개 행이 넘는 파일에 대한 추가 조치 필요

"""
import pandas as pd
import sqlite3

conn = sqlite3.connect('D:\\22년1월표제부\\표제부2201month.db')

query = '''
SELECT *
FROM bookdb
WHERE 대지위치 like "%서울%"
  AND ("옥내자주식대수(대)" + "옥외자주식대수(대)") >=1;
'''
Temp = pd.read_sql(query, conn)
conn.commit()
conn.close()
"""

# END
