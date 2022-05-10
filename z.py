for i, x in enumerate(old):
    print(i, 'is', x)
old[1] = 10

a = [1, 7, 3, 2, 9, 4]
n = len(a)
for i in range(1, n):
    j = i
    tmp = a[i]
    while j > 0 and a[j - 1] > tmp:
        a[j] = a[j - 1]
        print(a)
        j -= 1
    a[j] = tmp
    print(a)


import pandas as pd
import datetime
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', family='malgun gothic')

df = pd.read_excel('c://Users//Administrator//Desktop//2022.xlsx',
                   parse_dates=['발생일시', '확인일시', '복구일시', '종료일시'])
df.info()

df.loc[1, '확인일시'] - df.loc[1, '발생일시']
