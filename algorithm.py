"""
알고리즘 입문
"""


# -----------------------------------------
# 1장. 알고리즘 기초
# -----------------------------------------


# 1. 알고리즘 이란----------------


# 세 정수의 최대값
print("세 정수의 최대값을 구합니다")
a = int(input(print("첫번째 정수값을 입력하세요: ", end="")))
b = int(input(print("두번째 정수값을 입력하세요: ", end="")))
c = int(input(print("세번째 정수값을 입력하세요: ", end="")))

# 순차구조: 한문장씩 순서대로 실행
maximum = a  # 대입문
if b > maximum:
    maximum = b  # 선택구조: 조건식(조건)에 따른 실행흐름 변경
if c > maximum:
    maximum = c

print(f"최대값은 {maximum} 입니다")

# <보충> input()
# 1.input('문자열')에 전달된 문자열을 우선 출력
# 2.엔터가 입력때까지 키보드의 문자열을 입력 받음
# 3.엔터를 제외한 문자열을 반환

# <보충> ;
# 스위트가 단순문이면 헤드와 같은 행에 둘 수 있고
# 단순문이 여럿이면 ;으로 구분하여 같은 행에 둘 수 있다
# if a<b: min=a; max=b;


# 세 정수의 중앙값
def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b


print("세 정수의 최대값을 구합니다")
a = int(input(print("첫번째 정수값을 입력하세요: ", end="")))
b = int(input(print("두번째 정수값을 입력하세요: ", end="")))
c = int(input(print("세번째 정수값을 입력하세요: ", end="")))

print(f"중앙값은 {med3(a,b,c)} 입니다")

# <보충> 삼항연산자
# a if b else c # 피연산자수 3개, 파이썬에서 유일한 삼항연산자


# 반복하는 알고리즘----------------
# 변수가 하나일때는 for문 권장

# 1부터 n까지 정수의 합: while문
n = int(input("n 값을 넣으세요: "))

sum = 0  # 합 저장 변수
i = 1  # 카운터용 변수(반복제어)

while i <= n:  # 반복구조, i가 n+1 이어야 while 탈출
    sum += i
    i += 1

print(f"1부터 {n}까지의 합은 {sum}입니다")


# 1부터 n까지 정수의 합: for문, 변수가 1개이면 추천
n = int(input("n 값을 넣으세요: "))

sum = 0  # 합 저장 변수
for i in range(1, n + 1):  # 이터러블(반복)객체_str,list,tuple_생성
    sum += i

print(f"1부터 {n}까지의 합은 {sum}입니다")


# 반복 과정에서 조건 판단1: 비추천
print("a부터 b까지의 합을 구합니다")
a = int(input("정수 a 값을 넣으세요: "))
b = int(input("정수 b 값을 넣으세요: "))

if a > b:
    a, b = b, a  # a와 b 교환

sum = 0
for i in range(a, b + 1):  # 오름차순
    if i < b:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")  # 1번만 실행
    sum += i

print(sum)


# 반복 과정에서 조건 판단1: 추천
print("a부터 b까지의 합을 구합니다")
a = int(input("정수 a 값을 넣으세요: "))
b = int(input("정수 b 값을 넣으세요: "))

if a > b:
    a, b = b, a  # a와 b 교환

sum = 0
for i in range(a, b):  # 반복횟수 1번(b+1) 축소
    # if i<b:              # 조건 판단 제거
    print(f"{i} + ", end="")
    sum += i

print(f"{b} = ", end="")  # 1번만 실행되는 반복문 독립
sum += b
print(sum)


# 반복 과정에서 조건 판단2: 비추천
print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for i in range(n):
    if i % 2:  # 홀수
        print("-", end="")
    else:
        print("+", end="")

print()  # 줄바꿈

# <보충> 몫과 나머지
# 7/4의 몫은     1 = 7 // 4
# 7/4의 나머지는 3 = 7 % 4


# 개선포인트
# 1: for문을 반복할 때마다 if문도 반복 수행되는 문제 개선
# 2: 유연성 결핍(i를 1~n까지로 바꾸려면, range(범위)와 print(+-)문 내용을 바꿔야함) 개선
# for i in range(1, n+1):
#     if i % 2:
#         print('+', end='')
#     else:
#         print('-', end='')


# 반복 과정에서 조건 판단2: 추천
print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))

for _ in range(n // 2):  # 파이썬은 인덱스가 필요 없는 등 필요없는 값은 _로 표현
    print("+-", end="")

if n % 2:
    print("+", end="")

print()  # 줄바꿈


# 반복 과정에서 조건 판단3: 비추천
print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))

for i in range(n):
    print("*", end="")
    if i % w == w - 1:
        print()  # 줄바꿈

if n % w:
    print()  # 줄바꿈


# 반복 과정에서 조건 판단3: 추천
print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))

for _ in range(n // w):
    print("*" * w)

rest = n % w
if rest:
    print("*" * rest)


# 무한 루프와 break
while True:
    n = int(input("n 값을 입력하세요"))
    if n > 0:
        break  # n 이 0 보다 커질 때까지 반복

# <보충> n까지의 반복문 종료 시 카운터 i 값은?
# while i <= n :            # i는 n+1
# for i in range(n+1):      # i는 n


# 직사각형 넓이로 변의 길이 구하기
area = int(input("직사각형의 넓이를 입력하세요: "))

for i in range(1, area + 1):  # 약수를 나열
    if i * i > area:
        break  # i*i 가 area를 초과하면 반복 종료
    if area % i:
        continue  # 나누어 떨어지지 않으면 다음 스위트 건너띄고 진행
    print(f"{i} x {area//i}")


# else문이 뒤따르는 for문
# 10~99 사이의 난수 n개 생성(13이 나오면 중단)
import random

n = int(input("난수의 개수를 입력하세요: "))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=" ")
    if r == 13:
        print("\n프로그램을 중단합니다")
        break
else:  # 반복이 정상 종료된 다음 실행
    print("\n난수 생성을 종료합니다")

# <보충> else 문
# 조건식에 의해 반복문이 정상 종료되는 경우 실행
# break 문으로 종료되면 미실행


# 반복문 건너뛰기
# 건너뛰어야할 값을 모르거나 값이 변화할 때 사용(판단비용 과다)
for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=" ")
print()

# 판단보다 리스트연산비용이 저렴
for i in list(range(1, 8)) + list(range(9, 13)):
    if i == 8:
        continue
    print(i, end=" ")
print()

# <보충> 연속 비교연산자 사용
while True:
    no = int(input("2자리 양수를 입력하세요: "))
    if no >= 10 and no <= 99:  # 종료조건(2자리수)
        # if 10 <= no <= 99:
        # if not(no < 10 or no > 99):  # 계속조건(2자리수가아님)의 부정
        break
print(f"입력받은 양수는 {no}입니다.")

# 다중 루프
print("-" * 27)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:3}", end='')
    print()
print("-" * 27)

# 다중 루프: 직각 이등변 삼각형
print("왼쪽 아래가 직각이등변 삼각형을 출력합니다")
for i in range(1, 10):
    for j in range(1, i + 1):
        print('*', end='')
    print()

# 다중 루프: 직각 이등변 삼각형2
print("오른쪽 아래가 직각이등변 삼각형을 출력합니다")
for i in range(1, 10):
    for j in range(1, 10 + 1 - i):   # hint. 공백과 *의 개수를 합하면 n
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end='')
    print()

# 변수는 객체를 참조하는 객체에 연결된 이름에 불과함
# 모든 객체는 메모리를 가지며 자료형뿐만 아니라 식별번호(id)도 가짐
n = 1  # 전역변수


def put_id():
    x = 1  # 지역변수
    print(f'id(x) = {id(x)}')


print(f'id(1) = {id(1)}')
print(f'id(n) = {id(n)}')
put_id()  # n, x 모두 int객체 1을 참조하는 이름에 불과


# -----------------------------------------
# 2장. 기본 자료구조와 배열
# -----------------------------------------

# 자료구조와 배열----------------
# 배열: 묶음 단위로 값을 저장하는 배열은 흩어진 변수를 하나로 묶어서 사용할 수 있음
# 원소: 배열에 저장된 객체 하나하나로 각 원소는 고유의 인덱스를 부여 받음
# 파이썬의 배열: 뮤터블 객체인 list와 인뮤터블 객체인 tuple

# 실습2-1: 학생 수 변경, 특정 학생의 점수 확인|변경, 최고점|최저점|정렬 필요 등 대응 어려움
print('학생 그룹 점수의 합계와 평균을 구합니다.')

score1 = int(input('1번 학생의 점수를 입력하세요.: '))
score2 = int(input('2번 학생의 점수를 입력하세요.: '))
score3 = int(input('3번 학생의 점수를 입력하세요.: '))
score4 = int(input('4번 학생의 점수를 입력하세요.: '))
score5 = int(input('5번 학생의 점수를 입력하세요.: '))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'합계는 {total}점입니다.')
print(f'평균은 {total / 5}점입니다.')

# 리스트와 내장함수 list() 기초
list01 = []                  # 빈리스트
list02 = [None] * 5          # 원소가 5개이면서 원소값이 없는 리스트
list03 = [1, 2, 3, ]

list04 = list()              # 빈리스트
list05 = list('str')
list06 = list([1, 2, 3, ])
list07 = list((1, 2, 3, ))
list08 = list({1, 2, 3, })
list09 = list(range(3, 8))

# 튜플과 내장함수 tuple() 기초
tuple01 = ()                   # 빈튜플
tuple02 = (1,)
tuple03 = (1, 2, 3,)
tuple04 = 1,                   # 쉼표가 있으면 튜플로 인식
tuple05 = 1, 2, 3
tuple06 = 1, 2, 3,

tuple07 = tuple()              # 빈튜플
tuple08 = tuple('str')
tuple09 = tuple([1, 2, 3, ])
tuple10 = tuple({1, 2, 3, })
tuple11 = tuple(range(3, 8))

# 언팩
x = [1, 2, 3]
a, b, c = x
a, b, c

# 인덱스로 원소에 접근
x[0]
x[-1]

# 슬라이스식으로 원소에 접근
s = [11, 22, 33, 44, 55, 66, 77]
s[0:6:2]
s[3:1]  # !! i, j가 len(s)보다 크면 len(s)로 간주, i가 없으면 0로 간주, j가 없으면 len(s)로 간주

# 응용
x = 6
y = 2
x, y = y + 2, x + 3  # !! 동시 수행으로 x는 6으로 진행
print(x, y)

x = 6
y = 2
x = y + 2
y = x + 3  # 순차 수행으로 x는 4로 진행
print(x, y)

# 배열의 등가관계
# == : 두 객체의 값이 같은지 비교
# is : 두 객체의 값과 식별 번호가 같은지 비교
[1, 2, 3] == [1, 2, 3]    # 원소를 순차적으로 비교
[1, 2, 3] < [1, 2, 3, 1]  # 같은 경우는 배열 갯수가 많으면 그 배열이 크다
[1, 2, 3] < [1, 4]        # 대응 원소값 하나가 크면 그 배열이 크다
[1, 2, 3] < [1, 2, 3, 1] < [1, 4]

# 배열이란----------------

# 시퀀스형 자료를 받아서 애니형 자료를 반환
# 시퀀스자료형: 리스트, 튜플, 문자열, 바이트형 등 배열관련 자료형
# 애니자료형: 제약이 없는 자료형

# [Do it! 실습 2-2] 시퀀스 원소의 최댓값 출력하기(max.py)
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


# 파이썬에서는 하나의 스크립트프로그램을 모듈이라 칭하며 확장자를 제외한 파일명이 모듈명이다
# 모듈이 직접 수행될 때 '변수__name__' 은 '__main__'이다
# 모듈이 임포트될 때 '변수__name__' 은 원래의 '모듈명'이다
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num    # 원소 수가 num인 리스트를 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))

    print(f'최댓값은 {max_of(x)}입니다.')

# [Do it! 실습 2-3] 배열 원소의 최댓값을 구해서 출력하기(원솟값을 입력받음)
from max import max_of  # max.py 파일의 max_of 함수 호출

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                  # 빈 리스트

while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))    # 배열의 끝에 추가
    number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')

# 배열 원소를 하나씩 살펴보기(스캔) 위한 방법 4가지
x = ['Jone', 'George', 'Paul', 'Ringo']

# len()함수로 원소 수를 알아내어 반복
for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

# enumerate()함수로 인덱스로 반복: 인덱스와 원소를 짝지어 튜플로 꺼냄
for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

# enumerate()함수로 인덱스로 반복(1부터 카운트)
for i, name in enumerate(x, 1):
    print(f'x[{i}] = {name}')

# in을 사용하여 처음부터 순서대로 반복(인덱스 미사용)
for i in x:
    print(i)

# 배열 원소를 역순으로 정렬
from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx   # 원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))

    reverse_array(x)  # x를 역순으로 정렬

    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

# 리스트를 역순으로 정렬
x.reverse()            # 리스트가 자기자신을 역순으로 정렬하는 리스트형 함수 reverse()
y = list(reversed(x))  # x의 원소를 역순으로 꺼내서 새로운 리스트에 담는다

# 기수(n진수) 변환하기
# 10진수 정수를 n진수로 변환하려면 정수를 n으로 나눈 나머지를 구하는 동시에
# 몫이 0이 될때까지 나누기를 반복한 후 나머지를 역순으로 늘어 놓는다


# Do it! 실습 2-7 [A] 10진수 정수값을 입력받아 2~36진수로 변환하여 출력하기
def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r
    return d[::-1]         # 역순으로 반환


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True:  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
        if retry in {'N', 'n'}:
            break


# Do it! 실습 2-7 [A] 수정: 식으로 출력하기
def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:>{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:>{n}d} ... {x % r}')
        else:
            print(f'     {x // r:>{n}d} ... {x % r}')
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r
    return d[::-1]         # 역순으로 반환


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True:  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
        if retry in {'N', 'n'}:
            break

# !! 함수로 전달되는 매개변수 자료형에 따라서 달라지는 영향----------
# 함수에서 이뮤터블형의 매개변수를 변경하면 원래 매개변수값에는 영향없다
# 함수에서 뮤터블형의 매개변수를 변경하면 원래 매개변수값도 바뀐다


# 이뮤터블형 매개변수
def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s


x = int(input('x의 값을 입력하세요.: '))
print(f'1부터 {x}까지 합은 {sum_1ton(x)}입니다.')

print(x)


# 뮤터블형 매개변수
def change(lst, idx, val):
    """lst[idx]의 값을 val로 업데이트"""
    lst[idx] = val


x = [11, 22, 33, 44, 55]
print('x =', x)

index = int(input('업데이트할 인덱스를 선택하세요.: '))
value = int(input('새로운 값을 입력하세요.: '))

change(x, index, value)
print(f'x = {x}')

print(x)

# 소수 구하기---------------------

# 소수는 1과 자기자신(n) 이외에는 나누어 떨어지지 않음
counter = 0
for n in range(2, 1001):   # 1000 이하의 소수 구하기
    for i in range(2, n):  # 2 부터 최대 999까지 나누어 보기
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')

# 알고리즘개선1: 소수는 2 부터 n-1까지 어떤 소수로도 나누어 떨어지지 않음
counter = 0               # 알고리즘의 계산비용을 측정하는 변수
ptr = 0
prime = [None] * 500      # 찾은 소수를 저장할 배열
prime[ptr] = 2            # 2는 소수이므로 초기값으로 지정
ptr += 1
for n in range(3, 1001, 2):   # 홀수만을 대상으로 설정
    for i in range(1, ptr):  # 이미 찾은 소수로 나누기(n이 홀수이므로 prime[0]의 2로 나눌필요가 없어서 1부터 시작)
        counter += 1
        if n % prime[i] == 0:
            break
    else:
        prime[ptr] = n      # 소수를 배열에 등록
        ptr += 1
for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')

# 알고리즘개선2: 제곱근(대칭구조(5x20 과 20x5)) 이하의 어떤 소수로도 나누어 떨어지지 않는다
counter = 0           # 곱셈과 나눗셈을 합한 횟수
ptr = 0               # 이미 찾은 소수의 개수
prime = [None] * 500  # 1000개 중 짝수는 소수가 아니므로 500으로 지정

prime[ptr] = 2  # 2는 소수
ptr += 1

prime[ptr] = 3  # 3은 소수
ptr += 1

for n in range(5, 1001, 2):    # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:   # 제곱근 이하인지 확인
        counter += 2           # 곱셈과 나눗셈의 산식 2개를 반영
        if n % prime[i] == 0:  # 제곱근으로 나누어 떨어지므로 소수가 아님
            break              # 반복 중단
        i += 1
    else:                      # 끝까지 나누어 떨어지지 않았다면
        prime[ptr] = n         # 소수로 배열에 등록
        ptr += 1
        counter += 1

for i in range(ptr):  # ptr개의 소수를 출력
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

# 알고리즘개선2-1: 배열의 원소수를 미리 결정하지 않는 방법(변수ptr 불필요)

counter = 0             # 곱셈과 나눗셈을 합한 횟수
prime = [2, 3]          # 소수를 저장하는 배열

for n in range(5, 1001, 2):     # 홀수만을 대상으로 설정
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:   # 나누어 떨어지므로 소수가 아님
            break               # 반복 중단
        i += 1
    else:                       # 끝까지 나누어 떨어지지 않았다면
        prime += [n]            # !! 소수로 배열에 등록
        counter += 1

for i in prime:                 # 소수를 출력
    print(i)
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

# 보충. 얕은복사 깊은복사
import copy
x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()          # 얕은복사: 참조값만 복사
z = copy.deepcopy(x)  # 깊은복사: 참조하는 객체자체를 복사
m = x
n = x[:]
x[0][1] = 9
print(x, y, z, m, n, sep='\n')


# -----------------------------------------
# 3장. 검색 알고리즘
# -----------------------------------------

# # 선형검색: 정렬되지 않은 데이터셋(의 유일한 방법)을 맨 앞부터 검색 수행
# # 이진검색: 정렬된 데이터셋을 빠르게 검색 수행
# # 해시법: 추가, 삭제도 효율적으로 수행가능한 빠른 검색법


# # 선형검색 ----------

# 선형검색의 종료 조건(2가지)
# (1) 성공, 검색값과 일치하는 원소 찾음: if a[i] == key
# (2) 실패, 검색값을 못찾고 배열의 맨 끝에 도착: if i == len(a)

# [Do it! 실습 3-1] while 문으로 작성한 선형 검색 알고리즘
from typing import Any, Sequence


def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key값이 같은 원소를 선형 검색(while 문)"""
    i = 0
    while True:
        if a[i] == key:  # 종료조건1
            return i
        if i == len(a):  # 종료조건2
            return -1
        i += 1


# for문으로 구현하면 코드가 짧아짐
#     for i in range(len(a)):
#         if a[i] == key:
#             return i
#     return -1

if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    ky = int(input('검색할 값을 입력하세요.: '))
    idx = seq_search(x, ky)
    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

# # 보초법
# 검색할 원소를 배열의 마지막에 넣고 검색하여
# 종료조건2(실패) 가능성을 제거하여 if 판단 횟수를 반으로 줄임

# [Do it! 실습 3-3] 선형 검색 알고리즘(실습 3-1)을 보초법으로 수정
from typing import Any, Sequence
import copy


def seq_search(seq: Sequence, key: Any) -> int:
    """시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)"""
    a = copy.deepcopy(seq)  # seq를 복사
    a.append(key)           # 보초 key를 추가

    i = 0
    while True:
        if a[i] == key:
            break  # 검색에 성공하면 while 문을 종료
        i += 1
    return -1 if i == len(seq) else i


# # 이진검색 ----------

# 이진검색의 종료 조건(2가지)
# (1) 성공, a[pc]와 key가 일치하는 경우
# (2) 실패, 검색범위가 더 이상 없음

# [Do it! 실습 3-3] 이진 검색 알고리즘
from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0                   # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1          # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2  # 검색범위 중앙원소의 인덱스, 정수의 나눗셈은 소수점 버림 (6+7)//2 는 6
        if a[pc] == key:     # 검색조건1(성공)
            return pc
        elif a[pc] < key:
            pl = pc + 1      # 검색 범위를 뒤쪽의 절반으로 좁힘
        else:
            pr = pc - 1      # 검색 범위를 앞쪽의 절반으로 좁힘
        if pl > pr:          # 검색조건2(실패)
            break
    return -1


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    print('배열 데이터를 오름차순으로 입력하세요.')
    x[0] = int(input('x[0]: '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break
    ky = int(input('검색할 값을 입력하세요.: '))
    idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색
    if idx < 0:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')

# [Do it! 실습 3C-3] 이진 검색 알고리즘의 실행 과정을 출력
from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행 과정을 출력)"""
    pl = 0
    pr = len(a) - 1

    print('   |', end='')
    for i in range(len(a)):
        print(f'{i : 4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2

        print('   |', end='')
        if pl != pc:         # pl 원소 위에 <-를 출력
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:         # pr 원소 위에 ->를 출력
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')
        print(f'{pc:3}|', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n   |')

        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1


if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num
    print('배열 데이터를 오름차순으로 입력하세요.')
    x[0] = int(input('x[0]: '))
    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break
    ky = int(input('검색할 값을 입력하세요.: '))
    idx = bin_search(x, ky)                     # ky와 같은 값의 원소를 x에서 검색
    if idx < 0:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')


# # 해시법 ----------

# 배열의키(원소값)를 원소개수로 나눈 나머지(해시값)를 배열 인덱스로
# 지정하여 새로운 해시테이블 생성, 해시테이블의 원소는 버킷이라고 함


# # 체인법(오픈해시법): 해시값을 기준으로 연결 리스트 생성

# 개별 버킷의 속성: 노드클래스(key, value, next)로 생성
# 해시테이블의 크기는 소수를 선호, 테이블이 크면 충돌위험은 감소하나 메모리낭비와 상충

# # chained_hash.py 로 저장 =====
from __future__ import annotations
from typing import Any, Type
import hashlib


# 노드 클래스 만들기
class Node:
    """해시를 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key    # 키
        self.value = value  # 값
        self.next = next   # 뒤쪽 노드를 참조


# 해시 클래스 만들기
class ChainedHash:
    """체인법을 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity             # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity  # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
        # str(key): key를 문자열로 변환한 후 encode(): 바이트문자열로 재변환
        # hashlib.sha256(): 바이트문자열의 해시값을 구함
        # hashlib.sha256().hexdigest(): 해시값에서 16진수 문자열을 꺼냄
        # int(): 16진수 int형 변환

# 원소검색
    def search(self, key: Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 노드를 노드

        while p is not None:
            if p.key == key:
                return p.value   # 검색 성공
            p = p.next           # 뒤쪽 노드를 주목

        return None              # 검색 실패

# 원소추가: 리스트의 맨앞에 추가
    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 삽입"""
        hash = self.hash_value(key)  # 삽입하는 키의 해시값
        p = self.table[hash]         # 주목하는 노드

        while p is not None:
            if p.key == key:
                return False         # 삽입 실패
            p = p.next               # 뒤쪽 노드에 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp      # 노드를 삽입
        return True                  # 삽입 성공

# 원소삭제
    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)  # 삭제할 키의 해시값
        p = self.table[hash]         # 주목하고 있는 노드
        pp = None                    # 바로 앞 주목 노드

        while p is not None:
            if p.key == key:  # key를 발견하면 아래를 실행
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True  # key 삭제 성공
            pp = p
            p = p.next       # 뒤쪽 노드에 주목
        return False         # 삭제 실패(key가 존재하지 않음)

# 원소출력
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f'  → {p.key} ({p.value})', end='')  # 해시 테이블에 있는 키와 값을 출력
                p = p.next
            print()
# chained_hash.py 파일의 끝 =====


# [Do it! 실습 3-6] 체인법을 구현하는 해시 클래스 ChainedHash의 사용
from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])  # 메뉴를 선언


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)     # 크기가 13인 해시 테이블을 생성

while True:
    menu = select_menu()   # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break

# # 오픈주소법(닫힌해시법): 충돌 발생하면 재해시를 통하여 빈 버킷을 찾는 방법

# 개별 버킷의 속성: 노드클래스(데이터가 저장되어 있음, 비어 있음, 삭제 완료)로 생성

# # opem_hash.py 로 저장 =====
from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib


# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료


class Bucket:
    """해시를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값을 설정"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set_status(self, stat: Status) -> None:
        """속성을 설정"""
        self.stat = stat


class OpenHash:
    """오픈 주소법을 구현하는 해시 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                 # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 해시 테이블

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
               % self.capacity)

    # 해시값에 1을 더하여 재해시한 식으로 새로운 해시값을 구함
    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """키가 key인 갖는 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 요소를 추가"""
        if self.search(key) is not None:
            return False             # 이미 등록된 키

        hash = self.hash_value(key)  # 추가하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return False                        # 해시 테이블이 가득 참

    def remove(self, key: Any) -> int:
        """키가 key인 갖는 요소를 삭제"""
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False           # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')
# # opem_hash.py 끝 =====


# [Do it! 실습 3-8] 오픈 주소법을 구현하는 해시 클래스 OpenHash 사용
from enum import Enum
from open_hash import OpenHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = OpenHash(13)  # 크기가 13인 해시 테이블 생성

while True:
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break


# -----------------------------------------
# 4장. 스택과 큐(선형 검색)
# -----------------------------------------

# 데이터를 임시 저장하는 기본 자료구조
# 스택은 후입선출, 큐는 선입선출 방식

# fixed_stack.py 저장 =====
from typing import Any


class FixedStack:
    """고정 길이 스택 클래스"""

    class Empty(Exception):
        """비어 있을 때 pop 또는 peek를 호출하는 경우의 예외 처리"""
        pass

    class Full(Exception):
        """가득 찼을 때 push를 호출하는 경우의 예외 처리"""
        pass

    def __init__(self, capacity: int = 256) -> None:
        """초기화"""
        self.stk = [None] * capacity  # 스택 본체
        self.capacity = capacity      # 스택의 크기
        self.ptr = 0                  # 스택 포인터

    def __len__(self) -> int:
        """스택의 데이터 개수 반환
        더블언더스코어인 던더len함수는 인스던스를 전달받아
        obj.__len__() 및 len(obj) 모두 가능"""
        return self.ptr

    def is_empty(self) -> bool:
        """빈 스택 여부"""
        return self.ptr <= 0

    def is_full(self) -> bool:
        """스택의 full 여부"""
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        """데이터를 넣는 푸시"""
        if self.is_full():              # 스택이 가득 참
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        """꼭대기 데이터를 꺼내는 팝"""
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        """꼭대기 데이터를 들여다 보는 피크"""
        if self.is_empty():             # 스택이 비어 있음
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        """모든 데이터를 삭제: 모든 작업은 스택포인터 ptr로 이루어지므로
           배열 원솟값을 변경할 필요가 없이 0으로 하면 끝남"""
        self.ptr = 0

    def find(self, value: Any) -> Any:
        """먼저 팝할 데이터를 찾기 위해서 꼭대기(인덱스가 큰 쪽)부터 선형 검색을 수행"""
        for i in range(self.ptr - 1, -1, -1):  # 꼭대기 쪽부터 선형 검색
            if self.stk[i] == value:
                return i  # 검색 성공
        return -1         # 검색 실패

    def count(self, value: Any) -> bool:
        """스택에 원하는 데이터 개수를 반환"""
        c = 0
        for i in range(self.ptr):  # 바닥 쪽부터 선형 검색
            if self.stk[i] == value:
                c += 1             # 들어 있음
        return c

    def __contains__(self, value: Any) -> bool:
        """스택에 value 존재여부 판단
        더블언더스코어인 던더contains함수는 인스던스를 전달받아
        obj.__contains__(x) 및 x in obj, x not in obj 모두 가능"""
        return self.count(value)

    def dump(self) -> None:
        """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
        if self.is_empty():  # 스택이 비어 있음
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
# fixed_stack.py 끝 =====


# [Do it! 실습 4-2] 고정 길이 스택 FixedStack의 사용하기
from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = FixedStack(64)  # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색할 값을 입력하세요.: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break

# # stack.py: 표준라이브러리(collections.deque)를 사용 저장 =====
from typing import Any
from collections import deque


class Stack:
    """고정 길이 스택 클래스(collections.deque를 사용)"""

    def __init__(self, maxlen: int = 256) -> None:
        """초기화 선언"""
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """스택에 쌓여있는 데이터 개수를 반환"""
        return len(self.__stk)

    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단"""
        return not self.__stk

    def is_full(self) -> bool:
        """스택이 가득 찼는지 판단"""
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        """스택에 value를 푸시"""
        self.__stk.append(value)

    def pop(self) -> Any:
        """스택에서 데이터를 팝"""
        return self.__stk.pop()

    def peek(self) -> Any:
        """스택에서 데이터를 피크"""
        return self.__stk[-1]

    def clear(self) -> None:
        """스택을 비웁니다"""
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        """스택에서 value를 찾아 인덱스(없으면 -1)를 반환"""
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        """스택에 포함된 value의 개수를 반환"""
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        """스택에 value가 포함되어 있는지 판단"""
        return self.count(value)

    def dump(self) -> int:
        """스택 안에 있는 모든 데이터를 나열"""
        print(list(self.__stk))
# # stack.py 끝=====


# [Do it! 4C-1] 고정 길이 스택 클래스(collections.deque)를 사용하기
from enum import Enum
from stack import Stack

Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)


s = Stack(64)  # 최대 64 개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수：{len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터：'))
        try:
            s.push(x)
        except IndexError:
            print('스택이 가득 찼습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except IndexError:
            print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except IndexError:
            print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색 값을 입력하세요：'))
        if x in s:
            print(f'{s.count(x)} 개를 포함하고, 맨 앞쪽의 위치는 {s.find(x)}입니다.')
        else:
            print('검색 값은 포함되어 있지 않습니다.')

    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break

# # 큐
# 데이터를 임시저장하는 선입선출 자료구조
# 리어(맨끝)에서 인큐(넣음)작업을, 프론트(맨앞)에서 디큐(꺼냄)이 진행됨

# # 링 버퍼로 큐 구현하기
# 디큐를 하면 2번째 이후 모든 원소의 인덱스번호가 하나씩 앞으로 옮겨지며 업무복잡도가 큼
# 이의 해결방안으로 시작인덱스번호는 프론트변수로, 마지막인덱스번호는 리얼변수의 증감으로 관리함

# 고정 길이 큐 클래스 fixed_queue.py 저장 =====
from typing import Any


class FixedQueue:

    class Empty(Exception):
        """비어 있는 FixedQueue에 대해 deque 또는 peek를 호출할 때 내보내는 예외처리"""
        pass

    class Full(Exception):
        """가득 찬 FixedQueue에 enque를 호출할 때 내보내는 예외처리"""
        pass

    def __init__(self, capacity: int) -> None:
        """초기화 선언"""
        self.no = 0     # 현재 데이터 개수
        self.front = 0  # 맨앞 원소 커서(인덱스를 저장하는 변수를 커서라고 함)
        self.rear = 0   # 맨끝 원소 커서
        self.capacity = capacity      # 큐의 크기
        self.que = [None] * capacity  # 큐의 본체

    def __len__(self) -> int:
        """큐에 있는 모든 데이터 개수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """큐가 비어 있는지 판단"""
        return self.no <= 0

    def is_full(self) -> bool:
        """큐가 가득 찼는지 판단"""
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        """데이터 x를 인큐"""
        if self.is_full():
            raise FixedQueue.Full  # 큐가 가득 찬 경우 예외처리를 발생
        self.que[self.rear] = x
        self.rear += 1             # 데이터를 넣으면서 리얼변수를 1 증가시키고
        self.no += 1               # 전체 데이터 수도 1 증가 시킴
        if self.rear == self.capacity:  # 리얼변수가 배열의 마지막 인덱스이면
            self.rear = 0               # 배열의 처음(0)으로 보냄

    def deque(self) -> Any:
        """데이터를 디큐합니다"""
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있는 경우 예외처리를 발생
        x = self.que[self.front]
        self.front += 1             # 데이터를 꺼내면서 프론트변수를 1 증가시키고
        self.no -= 1                # 전체 데이터 수는 1 감소 시킴
        if self.front == self.capacity:  # 프론트변수가 배열의 마지막 인덱스이면
            self.front = 0               # 배열의 처음(0)으로 보냄
        return x

    def peek(self) -> Any:
        """데이터를 피크합니다(맨 앞 데이터를 들여다 봄)"""
        if self.is_empty():
            raise FixedQueue.Empty  # 큐가 비어 있으면 예외처리를 발생
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        """큐에서 value를 찾아 인덱스를 반환하고 없으면 -1을 반환합니다"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity  # 큐의 맨앞부터 검색
            if self.que[idx] == value:  # 검색 성공
                return idx
        return -1  # 검색 실패

    def count(self, value: Any) -> bool:
        """큐에 포함되어 있는 value의 개수를 반환합니다"""
        c = 0
        for i in range(self.no):  # 큐 데이터를 선형 검색
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  # 검색 성공
                c += 1  # 들어있음
        return c

    def __contains__(self, value: Any) -> bool:
        """큐에 value가 포함되어 있는지 판단합니다"""
        return self.count(value)

    def clear(self) -> None:
        """큐의 모든 데이터를 비웁니다"""
        self.no = self.front = self.rear = 0  # 실제 원솟값 삭제는 불필요

    def dump(self) -> None:
        """모든 데이터를 맨 앞에서 맨 끝 순서로 출력합니다"""
        if self.is_empty():  # 큐가 비어 있으면 예외처리를 발생
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
# fixed_queue.py 끝 =====


# [Do it! 실습 4-4] 고정 길이 큐 클래스(FixedQueue)를 사용하기
from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['인큐', '디큐', '피크', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


q = FixedQueue(64)  # 최대 64개를 인큐할 수 있는 큐 생성(고정 길이)

while True:
    print(f'현재 데이터 개수: {len(q)} / {q.capacity}')
    menu = select_menu()   # 메뉴 선택

    if menu == Menu.인큐:  # 인큐
        x = int(input('인큐할 데이터를 입력하세요.: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print('큐가 가득 찼습니다.')

    elif menu == Menu.디큐:  # 디큐
        try:
            x = q.deque()
            print(f'디큐한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = q.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedQueue.Empty:
            print('큐가 비었습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색할 값을 입력하세요.: '))
        if x in q:
            print(f'{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        q.dump()
    else:
        break

# # 링 버퍼의 활용: n개의 배열에서 최근 입력된 n개만 남기고 오래된 원소는 버림
n = int(input('정수를 몇 개 저장할까요? : '))
a = [None] * n  # 입력 받은 값을 저장하는 배열

cnt = 0         # 입력 받은 개수
while True:
    # 입력값을 저장할 인덱스 구하기
    a[cnt % n] = int(input((f'{cnt + 1} 번째 정수를 입력하세요.: ')))
    # cnt 값을 증가시켜 링 버퍼를 순환하면서 저장하기
    cnt += 1

    retry = input(f'계속 할까요?(Y ... Yes / N ... No) : ')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0:
    i = 0

while i < cnt:
    print(f'{i + 1}번째 = {a[i % n]}')  # %연산자를 사용하여 마지막 남은 값의 인덱스 순서대로 출력
    i += 1

# # 양방향 대기열 덱(double-ended queue): 양끝에서 입출력이 가능한 큐와 스택을 합친 데이터 자료구조
# 파이썬에서는 collections.deque컨테이너로 제공됨


# -----------------------------------------
# 5장. 재귀 알고리즘
# -----------------------------------------

# # 재귀 알로리즘의 기본: 자기 자신을 사용하여 정의 ----------


# [Do it! 실습 5-1] 양의 정수인 팩토리얼 구하기
def factorial(n: int) -> int:
    """양의 정수 n의 팩토리얼을 구하는 과정"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1


if __name__ == '__main__':
    n = int(input('출력할 팩토리얼 값을 입력하세요.: '))
    print(f'{n}의 팩토리얼은 {factorial(n)}입니다.')


# [Do it! 실습 5-2] 유클리드 호제법으로 최대 공약수 구하기
def gcd(x: int, y: int) -> int:
    """정숫값 x와 y의 최대 공약수를 반환"""
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


if __name__ == '__main__':
    print('두 정숫값의 최대 공약수를 구합니다.')
    x = int(input('첫 번째 정숫값을 입력하세요.: '))
    y = int(input('두 번째 정숫값을 입력하세요.: '))

    print(f'두 정숫값의 최대 공약수는 {gcd(x, y)}입니다.')

# # 재귀 알로리즘 분석 ----------

# 하향식과 상향식 분석 방법이 존재


# [Do it! 실습 5-3] 순수한 재귀 함수 구현하기
def recur(n: int) -> int:
    """순수한 재귀 함수 recur의 구현"""
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)


x = int(input('정숫값을 입력하세요.: '))
recur(x)


# [Do it! 실습 5-4] 재귀 함수의 구현(꼬리 재귀를 제거)
def recur(n: int) -> int:
    """꼬리재귀(recur(n - 2)) 제거"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2


x = int(input('정수값을 입력하세요.: '))
recur(x)

# [Do it! 실습 5-5] 스택으로 재귀 함수 구현하기(재귀를 제거)
from stack import Stack  # stack.py의 Stack 클래스를 임포트


def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n 값을 푸시
            n = n - 1
            continue          # while문 시작으로 돌아감
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(n)
            n = n - 2
            continue
        break                 # while문 종료


x = int(input('정수값을 입력하세요.: '))
recur(x)

# # 하노이의 탑 ----------

# [1] 마지막원반을 제외한 상단원반들을 시작기둥(1)에서 중간기둥(2)으로 이동
# [2] 마지막원반을 시작기둥(1)에서 마지막기둥(3)으로 이동
# [3] 중간기둥의 원반들을 중간기둥(2)에서 마지막기둥(3)으로 이동


# [Do it! 실습 5-6] 하노이의 탑 구현하기
def move(no: int, x: int, y: int) -> None:
    """원반을 no개를 x 기둥에서 y 기둥으로 옮김"""
    if no > 1:                         # [1]과정
        move(no - 1, x, 6 - x - y)     # 6(기둥번호의 합)-x-y으로 중간기둥 번호를 구함

    print(f'원반 [{no}]을(를) {x}기둥에서 {y}기둥으로 옮깁니다.')  # [2]과정

    if no > 1:                         # [3]과정
        move(no - 1, 6 - x - y, y)


print('하노이의 탑을 구현하는 프로그램입니다.')
n = int(input('원반의 개수를 입력하세요.: '))
move(n, 1, 3)

# # 8퀸 문제 ----------

# 문제: 8개의 퀸이 서로 공격하여 잡을 수 없도록 8 x 8 체스판에 배치하시오
# (퀸은 가로, 세로, 대각선의 8 방향으로 이동하여 상대를 잡을 수 있다)
# 규칙1. 각 열에 퀸을 1개만 배치한다(1열에 퀸을 배치하는 방법은 8가지(8행))
# 규칙2. 각 행에 퀸을 1개만 배치한다
# 규칙3. 대각선에 중첩되지 않도록 퀸을 1개만 배치한다
# 퀸을 1개 배치하고 나서 문제를 다시 8개의 부분 문제로 나누는 작업을 반복합니다

# [규칙1] 각 열에 1개 퀸을 배치한 조합을 재귀적으로 나열하기
pos = [0] * 8  # 각 열에서 퀸의 위치를 출력


def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    """i 열에 퀸을 배치"""
    for j in range(8):
        pos[i] = j   # 퀸을 'i열j행'에 배치
        if i == 7:  # 모든 열에 배치를 종료
            put()
        else:
            set(i + 1)  # 다음 열에 퀸을 배치(재귀호출)


set(0)  # 0 열에 퀸을 배치

# [+규칙2] 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기
pos = [0] * 8       # 각 열에서 퀸의 위치
flag = [False] * 8  # 각 행에 퀸을 배치했는지 체크


def put() -> None:
    """각 열에 놓은 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if not flag[j]:  # j 행에 퀸을 배치하지 않았으면
            pos[i] = j   # 퀸을 j 행에 배치
            if i == 7:   # 모든 열에 퀸을 배치를 완료
                put()
            else:
                flag[j] = True   # j 행에 퀸을 배치하면 true, 그렇지않으면 false 유지
                set(i + 1)       # 다음 열에 퀸을 배치
                flag[j] = False  # flag를 false로 초기화


set(0)  # 0열에 퀸을 배치

# [+규칙3] 8퀸 문제 알고리즘 구현하기(퀸을 놓는 상황을 네모로 표시)
pos = [0] * 8          # 각 열에 배치한 퀸의 위치
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크


def put() -> None:
    """퀸을 놓는 상황을 □와 ■로 출력"""
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 놓기"""
    for j in range(8):
        if(not flag_a[j] and not    # j 행에 아직 퀸을 놓지 않았으면
           flag_b[i + j] and not    # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면(대각선의 인덱스x+y합이 동일함 활용)
           flag_c[i - j + 7]):  # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면(대각선의 인덱스x-y+7의 값과 동일함 활용)
            pos[i] = j          # 퀸을 j 행에 놓기
            if i == 7:          # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 다음 열에 퀸을 놓기
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False


set(0)          # 0 열에 퀸을 놓기


# -----------------------------------------
# 6장. 정렬 알고리즘
# -----------------------------------------

# 정렬 알고리즘의 핵심은 교환, 선택, 삽입입니다
# 버블정렬, 단순선택정렬, 단순삽입정렬, 셀정렬, 퀵정렬, 병합정렬, 힙정렬, 도수정렬을 다룸

# 1. 버블정렬(bubble sort, 단순교환정렬)

# [Do it! 실습 6-1] 버블 정렬 알고리즘: 이웃한 원소의 대소를 패스(비교&교환)반복
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬"""
    n = len(a)
    for i in range(n - 1):             # n-1개의 정렬이 끝나면 마지막 원소는 이미 끝에 놓임
        for j in range(n - 1, i, -1):  # 배열의 뒤부터 패스(비교,교환) 진행
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-2] 버블 정렬 알고리즘 구현하기(정렬과정 상세출력 코드추가)
from typing import MutableSequence


def bubble_sort_verbose(a: MutableSequence) -> None:
    """버블 정렬(정렬 과정을 출력)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    for i in range(n - 1):
        print(f'패스 {i + 1}')
        for j in range(n - 1, i, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'),  # +교환, -스테이
                      end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')


if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort_verbose(x)  # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# [개선1: 중단점삽입] 교환횟수가 0이면 배열 정렬완료로 간주(비교횟수 감소효과)
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    """버블 정렬(교환 횟수에 따른 중단)"""
    n = len(a)
    for i in range(n - 1):
        exchng = 0        # 패스에서 교환 횟수 변수
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                exchng += 1
        if exchng == 0:
            break


if __name__ == '__main__':
    print('버블 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)      # 배열 x를 버블 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# [개선2: 스캔범위축소] 특정원소이후 교환이벤트가 없으면 그 원소 앞쪽은 정렬완료로 간주
from typing import MutableSequence


def bubble_sort3_verbose(a: MutableSequence) -> None:
    """버블 정렬(스캔 범위를 제한)"""
    ccnt = 0  # 비교 횟수
    scnt = 0  # 교환 횟수
    n = len(a)
    k = 0
    i = 0
    while k < n - 1:
        print(f'패스 {i + 1}')
        i += 1
        last = n - 1  # 마지막으로 교환된 두원소의 오른쪽 원소의 인덱스를 저장
        for j in range(n - 1, k, -1):
            for m in range(0, n - 1):
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'),
                      end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        k = last     # 다음에 수행할 패스범위를 a[last]로 제한
        for m in range(0, n - 1):
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')


if __name__ == '__main__':
    print('버블 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    bubble_sort3_verbose(x)  # 배열 x를 버블

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# 1-1. 셰이커정렬(번갈아바꾸어정렬)

# [Do it! 실습 6-5] 셰이커 정렬 알고리즘 구현하기(정렬 과정을 출력 포함)
from typing import MutableSequence


def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    ccnt = 0    # 출력변수: 비교 횟수
    scnt = 0    # 출력변수: 교환 횟수
    n = len(a)  # 출력변수
    left = 0
    right = len(a) - 1
    last = right
    i = 0       # 출력변수
    while left < right:
        print(f'패스{i + 1}')  # 출력변수
        i += 1                 # 출력변수
        for j in range(right, left, -1):  # 맨뒤부터 앞으로 스캔

            for m in range(0, n - 1):                                       # 출력변수-s
                print(f'{a[m]:2}' + ('  ' if m != j - 1 else
                                     ' +' if a[j - 1] > a[j] else ' -'), end='')
            print(f'{a[n - 1]:2}')
            ccnt += 1                                                       # 출력변수-e
            if a[j - 1] > a[j]:
                scnt += 1                                                   # 출력변수
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last                       # 스캔범위의 첫 원소 인덱스

        for m in range(0, n - 1):                                           # 출력변수-s
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')                                              # 출력변수-e

        if (left == right):
            break
        print(f'패스 {i + 1}')
        i += 1

        for j in range(left, right):      # 맨앞부터 뒤로 스캔

            for m in range(0, n - 1):                                      # 출력변수-s
                print(f'{a[m]:2}' + ('  ' if m != j else
                                     ' +' if a[j] > a[j + 1] else ' -'), end='')
            print(f'{a[n - 1]:2}')                                         # 출력변수-e

            if a[j] > a[j + 1]:
                scnt += 1                                                  # 출력변수
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last                      # 스캔범위의 마지막 원소 인덱스

        for m in range(0, n - 1):                                          # 출력변수-s
            print(f'{a[m]:2}', end='  ')
        print(f'{a[n - 1]:2}')
    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')                                     # 출력변수-e


if __name__ == '__main__':
    print('셰이커 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    shaker_sort(x)      # 배열 x를 단순 교환 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# 2. 단순선택정렬(straight selection sort, 작은 원소부터 알맞는 위치로 옮김)

# [단계1] 아직 정렬되지 않은 부분의 가장 작은 원소(a[min])를 선택한다
# [단계2] a[min]과 아직 정렬되지 않은 부분의 맨 앞의 원소와 교환한다

# [Do it! 실습 6-6] 단순 선택 정렬 알고리즘 구현
from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    """단순 선택 정렬"""
    n = len(a)
    for i in range(n - 1):
        min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환


if __name__ == '__main__':
    print('단순 선택 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    selection_sort(x)  # 배열 x를 단순 선택 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 3. 단순삽입정렬(straight insertion sort, 두번째 위치 원소부터 앞쪽에 삽입하여 옮김)

# [종료조건1] 정렬된 배열의 왼쪽 끝에 도달한 경우 (계속조건1, j가 0보다 큰 경우)
# [종료조건2] 이동하고픈 원소값보다 작거나 같은 원소를 발견한 경우 (계속조건2, a[j-1]이 원소값보다 큰 경우)

# [Do it! 실습 6-7] 단순 삽입 정렬 알고리즘 구현하기
from typing import MutableSequence


def insertion_sort(a: MutableSequence) -> None:
    """단순 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:  # [계속조건1] and [계속조건2]
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)  # 배열 x를 단순 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')


# 3-1. 이진삽입정렬(binary insertion sort)

# [Do it! 실습 6C-2] 이진 삽입 정렬 알고리즘의 구현(bisect.insort 사용)
from typing import MutableSequence


# def binary_insertion_sort(a: MutableSequence) -> None:
#     """이진 삽입 정렬"""
#     n = len(a)
#     for i in range(1, n):
#         key = a[i]
#         pl = 0                   # 검색 범위의 맨 앞 원소 인덱스
#         pr = i - 1               # 검색 범위의 맨 끝 원소 인덱스

#         while True:
#             pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
#             if a[pc] == key:     # 검색 성공
#                 break
#             elif a[pc] < key:
#                 pl = pc + 1      # 검색 범위의 뒤쪽 절반으로 좁힘
#             else:
#                 pr = pc - 1      # 검색 범위의 앞쪽 절반으로 좁힘
#             if pl > pr:
#                 break

#         pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스

#         for j in range(i, pd, -1):
#             a[j] = a[j - 1]
#         a[pd] = key

# # 파이썬 표준 라이브러리 bisect 모듈 사용
import bisect


def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬(bisect.insort을 사용)"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i), 0, i)


if __name__ == '__main__':
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num            # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)    # 배열 x를 이진 삽입 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 4. 셀정렬(shell sort, 단순삽입정렬의 보완판)

# h개 떨어진 원소끼리 정렬을 반복하고 마지막에 단순삽입정렬을 수행하여 정렬횟수는 늘지만 원소이동횟수가 줄어서 효율성 향상

# [Do it! 실습 6-9] 셸 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)
from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    """셸 정렬(h * 3 + 1의 수열 사용)"""
    n = len(a)
    h = 1

    while h < n // 9:                # h의 초기값이 지나치게 크면 비효율로 배열수를 9로 나눈 몫을 넘지 않도록 함
        h = h * 3 + 1                # + 최적의 h값 구하는 산식

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3                     # 반복할 때마다 h 감소하다가 최종적으로 1이 됨


if __name__ == '__main__':
    print('셸 정렬을 수행합니다(h * 3 + 1의 수열 사용).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num  # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)  # 배열 x를 셸 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 5. 퀵정렬(quick sort)

# 피벗(중심축)을 기준으로 작은 그룹과 큰 그룹으로 나누어서 최종적으로 모든 그룹이 1개 원소가 되면 종료
# 스택의 크기는 배열의 원소 수와 같은 값으로 하고, 원소 수가 적은 쪽의 그룹을 먼저 푸시하여야 쌓이는 데이터 수를 최소화함
# 피벗선택은 배열의 맨앞,가운데,맨뒤 원소를 정렬하고 가운데(피벗선택)와 맨뒤-1번째 원소를 교체하며
# 범위는 left+1 ~ right+2 로 좁히며 진행
# 원소 수가 9개 미만인 경우는 비효율적이라서 단순삽입정렬로 진행

# [Do it! 실습 6-10] 배열을 두 그룹으로 나누기
from typing import MutableSequence


def partition(a: MutableSequence) -> None:
    """배열을 분할하여 출력"""
    n = len(a)
    pl = 0         # 왼쪽 커서
    pr = n - 1     # 오른쪽 커서
    x = a[n // 2]  # 피벗(가운데 원소)

    while pl <= pr:
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'피벗은 {x}입니다.')

    print('피벗 이하인 그룹입니다.')
    print(*a[0: pl])           # a[0] ~ a[pl - 1]

    if pl > pr + 1:
        print('피벗과 일치하는 그룹입니다.')
        print(*a[pr + 1: pl])  # a[pr + 1] ~ a[pl - 1]

    print('피벗 이상인 그룹입니다.')
    print(*a[pr + 1: n])       # a[pr + 1] ~ a[n - 1]


if __name__ == '__main__':
    print('배열을 나눕니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    partition(x)         # 배열 x를 나누어서 출력

# [Do it! 실습 6-10] 퀵 정렬 알고리즘 구현: 원소가 2개 이상인 그룹을 재귀함수로 분류 반복하기
from typing import MutableSequence


def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    print(f'a[{left}] ~ a[{right}]: ', *a[left: right + 1])  # 과정 출력을 위한 추가된 부분(1줄)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x: pl += 1
        while a[pr] > x: pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)     # 좌우 각 그룹을 다시 나누기 위한 재귀 호출 추가
    if pl < right: qsort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-12] 퀵 정렬 알고리즘 구현(비재귀적인 퀵 정렬)
from stack import Stack                     # 실습 4C-1의 stack.py 파일 import
from typing import MutableSequence


def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a [right]를 퀵 정렬(비재귀 버전)"""
    range = Stack(right - left + 1)         # 스택 생성

    range.push((left, right))               # 나눠야할 배열 범위의 맨앞과 맨뒤 원소 인덱스

    while not range.is_empty():
        pl, pr = left, right = range.pop()  # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2]          # 피벗(중앙 요소)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:                        # 실습 6-10, 실습 6-11과 같음
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 저장
        if pl < right: range.push((pl, right))  # 오른쪽 그룹의 커서를 저장


def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('비재귀적인 퀵 정렬')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# [Do it! 실습 6-13] 퀵 정렬 알고리즘 구현하기(원소 수가 9개 미만인 경우 단순삽입정렬)
from typing import MutableSequence


def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 가운데 값의 인덱스를 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2


def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 단순 삽입 정렬"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp


def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if right - left < 9:            # 원소 수가 9개 미만이면 단순 삽입 정렬을 호출
        insertion_sort(a, left, right)
    else:                           # 원소 수가 9개 이상이면 퀵 정렬을 수행
        pl = left                   # 왼쪽 커서
        pr = right                  # 오른쪽 커서
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)


def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)


if __name__ == '__main__':
    print('퀵 정렬을 합니다(원소 수가 9개 미만이면 단순 삽입 정렬).')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)       # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 6. 병합정렬(merge sort)

# 알고리즘: 각각의 배열의 앞쪽 작은 원소부터 서로 비교하여 작은 원소를 꺼내 새로운 배열에 저장
# 배열을 두그룹으로 나누어 앞부분과 뒷부분으로 나누어 정렬한 후, 병합을 반복함

# [Do it! 실습 6-14] 정렬을 마친 두 배열을 병합하기
from typing import Sequence, MutableSequence


def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) -> None:
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0                 # 각 배열의 커서(인덱스변수를지칭)
    na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소수

    while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:              # a에 남은 원소를 복사(a배열의 중간지점에서 b배열이 종료된 경우, a배열의 나머지 옮김)
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:              # b에 남은 원소를 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1


if __name__ == '__main__':
    a = [2, 4, 6, 8, 11, 13]
    b = [1, 2, 3, 4, 9, 16, 21]
    c = [None] * (len(a) + len(b))
    print('정렬을 마친 두 배열의 병합을 수행합니다.')

    merge_sorted_list(a, b, c)  # 배열 a와 b를 병합하여 c에 저장

    print('배열 a와 b를 병합하여 배열 c에 저장하였습니다.')
    print(f'배열 a: {a}')
    print(f'배열 b: {b}')
    print(f'배열 c: {c}')

# Tip. sorted() 함수로 정렬: 이터러블객체의 원소를 정렬하여 list형으로 반환
a = [14, 6, 8, 11, 13]
b = [11, 2, 7, 4]
a, b = sorted([a, b])    # a, b를 배열단위(첫번째 원소부터)로 비교하여 정렬(배열내 원소정렬 않함)
c = list(sorted(a + b))  # a와 b를 연결하여 오름차순정렬후 list로 변환하여 c에 저장
print(a, b, c, sep='\n')

# [Do it! 실습 6-15] 병합 정렬 알고리즘 구현하기
from typing import MutableSequence


def merge_sort(a: MutableSequence) -> None:
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center:                     # 배열a의 앞부분을 배열buff로 복사
                buff[p] = a[i]
                p += 1
                i += 1

            while i <= right and j < p:            # 배열a의 뒷부분과 배열buff 앞부분을 배열a에 병합
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:                           # 배열buff의 나머지 원소를 배열a에 복사
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 병합결과를 임시저장하는 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬
    del buff                    # 작업용 배열을 소멸


if __name__ == '__main__':
    print('병합 정렬을 수행합니다')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    merge_sort(x)       # 배열 x를 병합 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 7. 힙정렬(heap sort)

# 알고리즘: 각각의 배열의 앞쪽 작은 원소부터 서로 비교하여 작은 원소를 꺼내 새로운 배열에 저장


# -----------------------------------------
# 7장. 문자열 검색
# -----------------------------------------
# -----------------------------------------
# 8장. 연결 리스트 검색
# -----------------------------------------
# -----------------------------------------
# 9장. 이진 트리 검색
# -----------------------------------------

# END.
