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
    for j in range(1, 10+1-i):   # hint. 공백과 *의 개수를 합하면 n
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
list06 = list([1, 2, 3,])
list07 = list((1, 2, 3,))
list08 = list({1, 2, 3,})
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
tuple09 = tuple([1, 2, 3,])
tuple10 = tuple({1, 2, 3,})
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
s[3:1]  # i, j가 len(s)보다 크면 len(s)로 간주, i가 없으면 0로 간주, j가 없으면 len(s)로 간주

# 응용
x = 6
y = 2
x, y = y+2, x+3  # 동시 수행으로 x는 6으로 진행
print(x, y)

x = 6
y = 2
x = y+2
y = x+3  # 순차 수행으로 x는 4로 진행
print(x, y)

# 배열의 등가관계
[1, 2, 3] == [1, 2, 3]    # 원소를 순차적으로 비교
[1, 2, 3] < [1, 2, 3, 1]  # 같은 경우는 배열 갯수가 많으면 그 배열이 크다
[1, 2, 3] < [1, 4]        # 대응 원소값 하나가 크면 그 배열이 크다
[1, 2, 3] < [1, 2, 3, 1] < [1, 4]

# == : 두 객체의 값이 같은지 비교
# is : 두 객체의 값과 식별 번호가 같은지 비교
# n++ 와 n+=1 같은 표현임


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
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]


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
        while True :  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True :  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <=  cd <=  36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input( "한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
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
        print('   +' + (n+2) * '-')
        if x//r:
            print(f'{r:2} | {x // r:>{n}d} ... {x % r}')
        else:
            print(f'     {x // r:>{n}d} ... {x % r}')
        d += dchar[x % r]  # 해당하는 문자를 꺼내 결합
        x //= r
    return d[::-1]         # 역순으로 반환

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True :  # 음이 아닌 정수를 입력받음
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break

        while True :  # 2~36진수의 정수값을 입력받음
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <=  cd <=  36:
                break

        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input( "한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
        if retry in {'N', 'n'}:
           break

# 함수로 전달되는 매개변수 자료형에 따라서 달라지는 영향----------
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
    lst [idx] = val

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
for n in range(2,1001):   # 1000 이하의 소수 구하기
    for i in range(2,n):  # 2 부터 최대 999까지 나누어 보기
        counter += 1
        if n%i == 0:
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
for n in range(3,1001,2):   # 홀수만을 대상으로 설정
    for i in range(1,ptr):  # 이미 찾은 소수로 나누기(n이 홀수이므로 prime[0]의 2로 나눌필요가 없어서 1부터 시작)
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

# 알고리즘개선2-1: 배열의 원소수를 미리 결정하지 않는 방법

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
        prime += [n]            # 소수로 배열에 등록
        counter += 1

for i in prime:                 # 소수를 출력
    print(i)
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')

# -----------------------------------------
# 3장. 검색 알고리즘
# -----------------------------------------
# -----------------------------------------
# 4장. 스택과 큐
# -----------------------------------------
# -----------------------------------------
# 5장. 재귀 알고리즘
# -----------------------------------------
# -----------------------------------------
# 6장. 정렬 알고리즘
# -----------------------------------------
# -----------------------------------------
# 7장. 문자열 검색
# -----------------------------------------
# -----------------------------------------
# 8장. 리스트
# -----------------------------------------
# -----------------------------------------
# 9장. 트리
# -----------------------------------------

# END.
