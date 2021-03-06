"""
_Algorithm.py
"""

# =========================
# 1장. 알고리즘 기초
# =========================

# # 순차 구조 ----------

maximum = a
if b > maximum:
    maximum = b
if c > maximum:
    maximum = c
print(f"최대값은 {maximum} 입니다")

# # 반복 구조 ----------

# # while 문
sum = 0
i = 1
while i <= n:  # i가 n+1 이어야 while 탈출
    sum += i
    i += 1
print(f"1부터 {n}까지의 합은 {sum}입니다")

# # for 문: 변수가 1개이면 추천
sum = 0
for i in range(1, n + 1):  # 이터러블 객체
    sum += i
print(f"1부터 {n}까지의 합은 {sum}입니다")

# # [비추천] 반복문과 조건문 혼용, 불필요한 반복 작업 수행
if a > b:
    a, b = b, a
sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f"{i} + ", end="")
    else:
        print(f"{i} = ", end="")  # 매번 불필요한 반복 실행
    sum += i
print(sum)

# # [추천]
if a > b:
    a, b = b, a
sum = 0
for i in range(a, b):      # 반복횟수 1번(b+1) 축소, 조건판단(if i<b) 제거!!
    print(f"{i} + ", end="")
    sum += i
print(f"{b} = ", end="")   # 1번만 실행되는 구문 독립!!
sum += b
print(sum)

# # [비추천] 반복문과 조건문 혼용, range 범위 1부터 시작 시 본문 수정 필요
print("+와 -를 번갈아 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
for i in range(n):
    if i % 2:               # 홀수
        print("-", end="")  # 1부터 시작하면 "+" 변경 필요
    else:
        print("+", end="")  # 1부터 시작하면 "-" 변경 필요
print()

# # [추천]
for _ in range(n // 2):     # 필요없는 값은 _로 표현
    print("+-", end="")
if n % 2:
    print("+", end="")
print()

# # [비추천]
print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))
for i in range(n):
    print("*", end="")
    if i % w == w - 1:
        print()  # 줄바꿈
if n % w:
    print()      # 줄바꿈

# # [추천]
for _ in range(n // w):
    print("*" * w)
rest = n % w
if rest:
    print("*" * rest)

# # [비추천]
for i in range(1, 13):
    if i == 8:    # 한번을 위한 판단비용 과다(건너뛸 값을 모르거나 값이 변화할 때는 사용)
        continue  # 반복문 건너뛰기
    print(i, end=" ")
print()

# # [추천]
for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=" ")
print()

# # 다중 루프: 직각 이등변 삼각형
print("오른쪽 아래가 직각이등변 삼각형을 출력합니다")
for i in range(1, 10):
    for j in range(1, 10 + 1 - i):   # 공백과 *의 개수를 합하면 n
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end='')
    print()


# =========================
# 2장. 기본 자료구조와 배열
# =========================

# # 자료구조와 배열 ----------

# # 리스트와 내장함수 list() 기초
[]
list()
list('str')
list([1, 2, 3, ])
list(range(3, 8))

# # 튜플과 내장함수 tuple() 기초
()
tuple()
1,
1, 2, 3,
tuple('str')
tuple([1, 2, 3, ])
tuple({1, 2, 3, })
tuple(range(3, 8))

# # if 문과 빈배열
if []:
    print('The array with the elements is true')
else:
    print(bool([]))

# # 배열이란----------

# # 시퀀스 원소의 최댓값 출력하기(max.py)
from typing import Any, Sequence


def max_of(a: Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum


# 모듈(파일)이 직접 실행될 때 수행되는 구문
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}]를 입력하세요.: '))
    print(f'최댓값은 {max_of(x)}입니다.')

# # 배열 원소의 최댓값을 구해서 출력하기(사용자 입력 받기)
# max.py 파일의 max_of 함수 호출
from max import max_of

print('배열의 최댓값을 구합니다.')
print('주의: "End"를 입력하면 종료합니다.')
number = 0
x = []
while True:
    s = input(f'x[{number}]를 입력하세요.: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1
print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)}입니다.')

# # 배열 원소를 하나씩 살펴보기(스캔) 위한 방법 4가지
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

# # 배열 원소를 역순으로 정렬
from typing import Any, MutableSequence


def reverse_array(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]


if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요.: '))
    x = [None] * nx
    for i in range(nx):
        x[i] = int(input(f'x[{i}] : '))
    reverse_array(x)
    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')

# # 기수(n진수) 변환하기
# 10진수 정수를 n진수로 변환하려면 정수를 n으로 나눈 나머지를 구하는 동시에
# 몫이 0이 될때까지 나누기를 반복한 후 나머지를 역순으로 놓는다


# 10진수 정수값을 입력 받아 2~36진수로 변환하여 출력하기
def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''  # 변환 뒤 문자열
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]


"""
# 변환과정을 출력하여 보기
def card_conv(x: int, r: int) -> str:
    """정수 x를 r 진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))
    print(f'{r:2} | {x:>{n}d}')
    while x > 0:
        print('   +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:>{n}d} ... {x % r}')
        else:
            print(f'     {x // r:>{n}d} ... {x % r}')
        d += dchar[x % r]
        x //= r
    return d[::-1]
"""

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')
    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요.: '))
            if no > 0:
                break
        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')
        retry = input("한 번 더 변환할까요?(Y ... 예/N ... 아니오): ")
        if retry in {'N', 'n'}:
            break


>>>>>>>>>>>>>>>>>
# 소수 구하기---------------

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


# =========================
# 3장. 검색 알고리즘
# =========================

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
# from __future__ import annotations
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
# from __future__ import annotations
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


# =========================
# 4장. 스택과 큐(선형 검색)
# =========================

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


# =========================
# 5장. 재귀 알고리즘
# =========================

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


# =========================
# 6장. 정렬 알고리즘
# =========================

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
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
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
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        qsort(a, left, pr)     # 좌우 각 그룹을 다시 나누기 위한 재귀 호출 추가
    if pl < right:
        qsort(a, pl, right)


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
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:                        # 실습 6-10, 실습 6-11과 같음
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            range.push((left, pr))    # 왼쪽 그룹의 커서를 저장
        if pl < right:
            range.push((pl, right))  # 오른쪽 그룹의 커서를 저장


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
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
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
            while a[pl] < x:
                pl += 1
            while a[pr] > x:
                pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            qsort(a, left, pr)
        if pl < right:
            qsort(a, pl, right)


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

# 알고리즘: 힙(쌓아둔더미)에서는 최대 또는 최소값이 루트에 존재
# 루트값을 꺼낸 후 마지막 원소를 루트로 이동
# 루트에서 시작하여 자신값과 직계자손값을 비교하여 최댓, 최솟값을 가진 원소와 자신값을 교환하며
# 아래쪽으로 내려가는 작업을 반복
# 자신값이 최적값이거나 자식이없는 노드까지 도달하면 종료

# [Do it! 실습 6-16] 힙 정렬 알고리즘 구현하기
from typing import MutableSequence


def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left]      # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식(parent * 2 + 2)
            child = cr if cr <= right and a[cr] > a[cl] else cl  # 큰 값을 선택합니다.
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]을 힙으로 만들기
        """배열a를 힙상태로 만듦"""
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        """최댓값a[0]을 마지막원소와 교환하고 남은 부분을 다시 힙상태로 만듦"""
        a[0], a[i] = a[i], a[0]     # 최댓값인 a[0]과 마지막 원소 a[i]를 교환
        down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]을 힙으로 만들기(2단계)


if __name__ == '__main__':
    print('힙 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num    # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    heap_sort(x)        # 배열 x를 힙 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# 8. 도수정렬(counting sort)

# 원소의 대소를 판단하지 않고 단일 for문만을 사용하여 빠르게 정렬하는 알고리즘
# 사전에 데이터의 최솟, 최댓값을 아는 경우에만 적용 가능
# [1단계] 도수구간수만큼의 도수분포배열f 생성하고 a원소값을 f배열의 인덱스에 맞춰 f원소값을 1씩 증가시킴
# [2단계] f[1]부터 바로앞의 원소수를 누적하며 누적도수분포배열f 로 덮었씌움
# [3단계] a배열의 맨뒤 원소값부터 누적도수배열과 비교하며 작업용배열(Raw원소만큼의 배열)에 배치
#         (앞쪽부터정렬하면 같은 원솟값의 순서가 바뀌어 불안정배열이 됨)
#         중복방지위해 a배열의 원소와 비교된 누적도수배열의 원소값은 -1씩 줄임
# [4단계] 작업용배열을 a배열에 복사

# [Do it! 실습 6-17] 도수 정렬 알고리즘 구현하기
from typing import MutableSequence


def fsort(a: MutableSequence, max: int) -> None:
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):
        f[a[i]] += 1                  # [1단계]
    for i in range(1, max + 1):
        f[i] += f[i - 1]              # [2단계]
    for i in range(n - 1, -1, -1):
        f[a[i]] -= 1                  # [3단계]
    b[f[a[i]]] = a[i]
    for i in range(n):
        a[i] = b[i]                   # [4단계]


def counting_sort(a: MutableSequence) -> None:
    """도수 정렬"""
    fsort(a, max(a))


if __name__ == '__main__':
    print('도수 정렬을 합니다.')
    num = int(input('원소 수를 입력하세요. : '))
    x = [None] * num                                 # 원소 수가 num인 배열을 생성

    for i in range(num):                             # 양수만 입력받도록 제한
        while True:
            x[i] = int(input(f'x[{i}] : '))
            if x[i] >= 0:
                break

    counting_sort(x)                                 # 배열 x를 도수 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

# =========================
# 7장. 문자열 검색
# =========================

# # 1. 브루트포스법(단순법)
# 검색받는 쪽의 문자열을 '텍스트', 검색조건 문자열을 '패턴'이라고 칭함

# [Do it! 실습 7-1] 브루트 포스법으로 문자열 검색하기


def bf_match(txt: str, pat: str) -> int:
    """브루트 포스법으로 문자열 검색"""
    pt = 0                                # txt(텍스트)를 따라가는 커서
    pp = 0                                # pat(패턴)를 따라가는 커서

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt - pp + 1
            pp = 0

    return pt - pp if pp == len(pat) else -1  # 검색성공하면 텍스트의 첫번째 인덱스반환, 실패하면 -1 반환


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = bf_match(s1, s2)               # 문자열 s1~s2를 브루트 포스법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')

# # Tip
# T-1. 멤버쉽연산자: 검색한 문자열 포함 여부 반환
# 패턴 in 텍스트, 패턴 not in 텍스트
# T-2. find, index 계열 함수: 검색한 문자열 위치 반환
# str.find(sub, start, end)    # 처음찾은인덱스 또는 -1
# str.rfind(sub, start, end)   # 마지막찾은인덱스 또는 -1
# str.index(sub, start, end)   # 처음찾은인덱스 또는 ValueError
# str.rindex(sub, start, end)  # 마지막찾은인덱스 또는 ValueError
# T-3. with 계열 함수: 패턴이 문자열의 시작 또는 끝에 포함되어 있는지 여부 반환
# str.startswith(prefix, start, end)
# str.endswith(suffix, start, end)

# # 2. KMP법

# 패턴을 이용한 표를 작성하여 검사할 위치를 조정하는 알고리즘

# 사전에 패턴 2개를 겹치도록 맞추어 검사를 시작할 곳을 계산한 skip table 작성


# [Do it! 실습 7-2] KMP법으로 문자열 검색하기
def kmp_match(txt: str, pat: str) -> int:
    """KMP법에 의한 문자열 검색"""
    pt = 1                       # txt를 따라가는 커서
    pp = 0                       # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기표(skip table)

    # 건너뛰기표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 문자열 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴용 문자열

    idx = kmp_match(s1, s2)              # 문자열 s1~s2를 KMP법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')

# # 3. 보이어무어법

# 패턴의 끝문자부터 앞쪽으로 검사수행하는 널리 사용되는 알고리즘
# 패턴에 포함되지 않은 문자를 만나면 한번에 m만큼 이동(패턴길이m, 문자열길이n)
# 패턴에 포함된 문자를 만나면 일치하는 패턴의 마지막문자 인덱스를 k라면 이동은 m-k-1


# [Do it! 실습 7-3] 보이어 무어법으로 문자열 검색하기(0~255 문자)
def bm_match(txt: str, pat: str) -> int:
    """보이어 무어법에 의한 문자열 검색"""
    skip = [None] * 256  # 모든 문자의 이동량 계산을 위한 건너뛰기표 원소는 256개 설정

    # 건너뛰기표 만들기
    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1  # ord()함수는 문자를 전달받아서 유니코드 정수를 반환

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')  # 텍스트 문자열
    s2 = input('패턴을 입력하세요.: ')    # 패턴 문자열

    idx = bm_match(s1, s2)               # 문자열 s1~s2를 KMP법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자에서 일치합니다.')

# =========================
# 8장. 연결 리스트(Linked list) 검색
# =========================

# 연결 리스트의 원소를 노드라고 칭하는데, 노드는 데이터와 뒤쪽 노드를 가리키는 참조 포인터를 갖고 있다
# 연결 리스트의 리스트는 파이썬에서 제공하는 리스트 자료형(배열)과는 다르다

# 포인터를 이용한 연결 리스트 만들기 linked_list.py 저장 ----------
from typing import Any, Type


class Node:
    """연결 리스트용 노드 클래스"""

    def __init__(self, data: Any = None, next: Node = None):
        """초기화"""
        self.data = data  # 데이터
        self.next = next  # 뒤쪽 포인터


class LinkedList:
    """연결 리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.no = 0          # 리스트에 등록되어 있는 노드의 개수
        self.head = None     # 머리 노드에 대한 참조(머리 노드가 아님)
        self.current = None  # 현재 주목하고 있는 노드에 대한 참조(주목 포인터)

    def __len__(self) -> int:
        """연결 리스트의 노드 개수를 반환"""
        return self.no

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt    # 종료조건2: 검색조건 만족하는 노드를 찾은 경우
            cnt += 1
            ptr = ptr.next
        return -1             # 종료조건1: 검색조건 만족하는 노드를 못찾고 꼬리노드에 왔을 때

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는지 판단"""
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        ptr = self.head                             # 삽입 전의 머리 노드를 참조하는 포인터 저장
        self.head = self.current = Node(data, ptr)  # 삽입할 노드를 생성
        self.no += 1

    def add_last(self, data: Any):
        """맨 끝에 노드를 삽입"""
        if self.head is None:     # 리스트가 비어 있으면 맨앞에 노드를 삽입하는 것과 같은 처리
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:                 # 꼬리노드(next가 None) 찾기
                ptr = ptr.next
            ptr.next = self.current = Node(data, None)  # 삽입할 노드를 생성
            self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head is not None:  # 리스트가 비어 있지 않으면 머리노드에 대한 참조를 다음 노드로 건너뜀
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self):
        """꼬리 노드 삭제"""
        if self.head is not None:
            if self.head.next is None:  # 노드가 1개 뿐이라면
                self.remove_first()     # 머리 노드를 삭제
            else:
                ptr = self.head         # 스캔 중인 노드
                pre = self.head         # 스캔 중인 노드의 앞쪽 노드

                while ptr.next is not None:  # 꼬리노드와 꼬리 바로앞노드를 찾음
                    pre = ptr
                    ptr = ptr.next
                pre.next = None        # 맨끝에서 2번째 노드에 none을 넣어서 꼬리참조를 끊음
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        """임의의 노드 p를 삭제"""
        if self.head is not None:
            if p is self.head:         # p가 머리 ​​노드이면 머리 노드를 삭제
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:    # None을 만나면 삭제 수행 않고 복귀
                        return
                ptr.next = p.next      # p 이전노드가 p 다음노드를 참조하도록하여 삭제 처리
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """전체 노드를 삭제"""
        while self.head is not None:  # 전체가 비어 있게 될 때까지
            self.remove_first()       # 머리 노드를 삭제
        self.current = None
        self.no = 0

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.current is None or self.current.next is None:
            return False              # 이동할 수 없음
        self.current = self.current.next
        return True

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current is None:
            print('주목 노드가 존재하지 않습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next

    def __iter__(self) -> LinkedListIterator:
        """이터레이터(반복자)를 반환"""
        return LinkedListIterator(self.head)


class LinkedListIterator:
    """클래스 LinkedList의 이터레이터(반복자)용 클래스"""

    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
# linked_list.py 파일 끝 ----------


# [Do it! 실습 8-2] 포인터로 이용한 연결 리스트 클래스 LinkedList 사용하기
from enum import Enum
from linked_list import LinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])


def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = LinkedList()  # 연결 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리에 넣을 값을 입력하세요.: ')))

    elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
        lst.remove_first()

    elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
        lst.remove_last()

    elif menu == Menu.주목노드출력:  # 주목 노드 출력
        lst.print_current_node()

    elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
        lst.next()

    elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:  # 모든 노드를 삭제
        lst.clear()

    elif menu == Menu.검색:  # 노드를 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.멤버십판단:  # 멤버십 판단
        print('그 값의 데이터는 포함되어' + (' 있습니다.' if int(input('멤버십 판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))

    elif menu == Menu.모든노드출력:  # 모든 노드 출력
        lst.print()

    elif menu == Menu.스캔:  # 모든 노드 스캔
        for e in lst:
            print(e)

    else:  # 종료
        break


# # 커서를 이용한 연결 리스트(ArrayLinkedList)
# 다음 노드의 인덱스를 저장하는 커서를 두는 배열로 구현, 꼬리노드의 커서값은 -1
# 연결리스트의 논리적 위치와 배열의 물리적 위치가 일치하지 않음
# 삭제이벤트는 배열 내 빈레코드를 발생시키므로 이를 해결하기 위해 프리리스트를 적용

# [Do it! 실습 8-3] 커서로 선형 리스트 만들기 array_list.py 저장 -----
# from __future__ import annotations
from typing import Any, Type

Null = -1


class Node:
    """선형 리스트용 노드 클래스(배열 커서 버전)"""

    def __init__(self, data=Null, next=Null, dnext=Null):
        """초기화"""
        self.data = data    # 데이터
        self.next = next    # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터


class ArrayLinkedList:
    """선형 리스트 클래스(배열 커서 버전)"""

    def __init__(self, capacity: int):
        """초기화"""
        self.head = Null                   # 머리 노드
        self.current = Null                # 주목 노드
        self.max = Null                    # 사용 중인 꼬리 레코드
        self.deleted = Null                # 프리 리스트의 머리 노드
        self.capacity = capacity           # 리스트의 크기
        self.n = [Node()] * self.capacity  # 리스트 본체
        self.no = 0

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def get_insert_index(self):
        """다음에 삽입할 레코드의 첨자를 구합니다"""
        if self.deleted == Null:              # 삭제 레코드는 존재하지 않아서 프리리스트가 비어 있으면
            if self.max + 1 < self.capacity:  # max를 증가시켜 배열 맨끝의 미사용 레코드를 사용함
                self.max += 1
                return self.max   # 새 레코드를 사용
            else:
                return Null       # 크기 초과
        else:
            rec = self.deleted                # 프리 리스트에서
            self.deleted = self.n[rec].dnext  # 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트(삭제된 레코드그룹을 관리)에 등록"""
        if self.deleted == Null:      # 삭제 레코드는 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null  # idx를 프리 리스트의 맨 앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx        # idx를 프리 리스트의 맨 앞에 삽입
            self.n[idx].dnext = rec

    def search(self, data: Any) -> int:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head             # 현재 스캔 중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt          # 검색 성공
            cnt += 1
            ptr = self.n[ptr].next  # 뒤쪽 노드에 주목
        return Null                 # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """선형 리스트에 data가 포함되어 있는지 확인"""
        return self.search(data) >= 0

    def add_first(self, data: Any):
        """머리 노드에 삽입"""
        ptr = self.head                     # 삽입하기 전의 머리 노드
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec  # rec번째 레코드에 삽입
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        """꼬리 노드에 삽입"""
        if self.head == Null:     # 리스트가 비어 있으면
            self.add_first(data)  # 맨 앞에 노드 삽입
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:       # rec번째 레코드에 삽입
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        """머리 노드를 삭제"""
        if self.head != Null:     # 리스트가 비어 있으면
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        """꼬리 노드를 삭제"""
        if self.head != Null:
            if self.n[self.head].next == Null:  # 노드가 1개 뿐이면
                self.remove_first()             # 머리 노드를 삭제
            else:
                ptr = self.head                 # 스캔 중인 노드
                pre = self.head                 # 스캔 중인 노드의 앞쪽 노드

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next
                self.n[pre].next = Null         # pre는 삭제한 뒤의 꼬리 노드
                self.delete_index(ptr)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """레코드 p를 삭제"""
        if self.head != Null:
            if p == self.head:
                self.remove_first()             # p가 머리 노드면 머리 노드를 삭제
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return                  # p는 리스트에 존재하지 않음
                self.n[ptr].next = Null
                self.delete_index(p)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        """주목 노드를 삭제"""
        self.remove(self.current)

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while self.head != Null:  # 리스트 전체가 빌 때까지
            self.remove_first()   # 머리 노드를 삭제
        self.current = Null

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 진행"""
        if self.current == Null or self.n[self.current].next == Null:
            return False          # 이동할 수 없음
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """배열을 덤프"""
        for i in self.n:
            print(f'[{i}]  {i.data} {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """이터레이터를 반환"""
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:
    """클래스 ArrayLinkedList의 이터레이터용 클래스"""

    def __init__(self, n: int, head: int):
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current = self.n[self.current].next
            return data
# array_list.py 저장 -----


# 커서를 이용한 선형 리스트 클래스 ArrayLinkedList 사용
from enum import Enum
from array_list import ArrayLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])


def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = ArrayLinkedList(100)  # 선형 리스트를 생성

while True:
    menu = select_Menu()  # 메뉴 선택
    if menu == Menu.머리에노드삽입:               # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
    elif menu == Menu.꼬리에노드삽입:             # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))
    elif menu == Menu.머리노드삭제:             # 맨 앞 노드를 삭제
        lst.remove_first()
    elif menu == Menu.꼬리노드삭제:             # 맨 끝 노드를 삭제
        lst.remove_last()
    elif menu == Menu.주목노드출력:             # 주목 노드를 출력
        lst.print_current_node()
    elif menu == Menu.주목노드이동:             # 주목 노드를 한 칸 뒤로 이동
        lst.next()
    elif menu == Menu.주목노드삭제:             # 주목 노드를 삭제
        lst.remove_current_node()
    elif menu == Menu.모든노드삭제:             # 모두 삭제
        lst.clear()
    elif menu == Menu.검색:                     # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'이 키를 갖는 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')
    elif menu == Menu.멤버십판단:               # 멤버십을 판단
        print('그 값의 데이터는 포함되어'
              + ('있습니다.' if int(input('판단할 값을 입력하세요.')) in lst else ' 있지 않습니다.'))
    elif menu == Menu.모든노드출력:             # 모든 노드를 출력
        lst.print()
    elif menu == Menu.스캔:                     # 모든 노드 스캔
        for e in lst:
            print(e)
    else:                                       # 종료
        break


# # 원형 이중 연결 리스트(circular doubly linked List)
# 원형 리스트의 꼬리 노드는 머리노드를 참조하는 포인터를 갖는다
# 이중 연결 리스트는 앞쪽 노드에 대한 참조 포인터를 갖는다

# 원형 이중 연결 리스트 구현하기 double_list.py 저장 -----
# from __future__ import annotations
from typing import Any, Type


class Node:
    """노드 클래스"""

    def __init__(self, data: Any = None, prev: Node = None,
                 next: Node = None) -> None:
        """초기화"""
        self.data = data          # 데이터
        self.next = next or self  # 뒤쪽 포인터(or 단축연산에 따라서 전달받은 값이 None인 경우 self를 대입)
        self.prev = prev or self  # 앞쪽 포인터 추가(None이 아니면 prev입력하고 None이면 self를 대입)


class DoubleLinkedList:
    """리스트 클래스"""

    def __init__(self) -> None:
        """초기화"""
        self.head = self.current = Node()  # 원할한 삽입과 삭제를 위한 더미 노드를 생성
        self.no = 0

    def __len__(self) -> int:
        """선형 리스트의 노드 수를 반환"""
        return self.no

    def is_empty(self) -> bool:
        """리스트가 비어 있는가?"""
        return self.head.next is self.head

    def search(self, data: Any) -> Any:
        """data와 값이 같은 노드를 검색"""
        cnt = 0
        ptr = self.head.next  # 현재 스캔 중인 노드(head가 참조하는 노드는 더미노드이므로 실제 머리노드는 head.next)
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt  # 검색 성공
            cnt += 1
            ptr = ptr.next  # 뒤쪽 노드에 주목
        return -1           # 검색 실패

    def __contains__(self, data: Any) -> bool:
        """연결 리스트에 data가 포함되어 있는가?"""
        return self.search(data) >= 0

    def print_current_node(self) -> None:
        """주목 노드를 출력"""
        if self.is_empty():
            print('주목 노드는 없습니다.')
        else:
            print(self.current.data)

    def print(self) -> None:
        """모든 노드를 출력"""
        ptr = self.head.next  # 더미 노드의 뒤쪽 노드
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self) -> None:
        """모든 노드를 역순으로 출력"""
        ptr = self.head.prev  # 더미 노드의 앞쪽 노드
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self) -> bool:
        """주목 노드를 한 칸 뒤로 이동"""
        if self.is_empty() or self.current.next is self.head:
            return False  # 이동할 수 없음
        self.current = self.current.next
        return True

    def prev(self) -> bool:
        """주목 노드를 한 칸 앞으로 이동"""
        if self.is_empty() or self.current.prev is self.head:
            return False  # 이동할 수 없음
        self.current = self.current.prev
        return True

    def add(self, data: Any) -> None:
        """주목 노드의 바로 뒤에 노드를 삽입"""
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data: Any) -> None:
        """맨 앞에 노드를 삽입"""
        self.current = self.head  # 더미 노드 head의 바로 뒤에 삽입
        self.add(data)

    def add_last(self, data: Any) -> None:
        """맨 뒤에 노드를 삽입"""
        self.current = self.head.prev  # 꼬리 노드 head.prev의 바로 뒤에 삽입
        self.add(data)

    def remove_current_node(self) -> None:
        """주목 노드 삭제"""
        if not self.is_empty():  # 더미노드 삭제 방지
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.prev
            self.no -= 1
            if self.current is self.head:
                self.current = self.head.next

    def remove(self, p: Node) -> None:
        """노드 p를 삭제"""
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:  # p를 발견
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next

    def remove_first(self) -> None:
        """머리 노드 삭제"""
        self.current = self.head.next  # 머리 노드 head.next를 삭제
        self.remove_current_node()

    def remove_last(self) -> None:
        """꼬리 노드 삭제"""
        self.current = self.head.prev  # 꼬리 노드 head.prev를 삭제
        self.remove_current_node()

    def clear(self) -> None:
        """모든 노드를 삭제"""
        while not self.is_empty():  # 리스트 전체가 빌 때까지
            self.remove_first()  # 머리 노드를 삭제
        self.no = 0              # 삭제한 결과 주목포인터 current가 참조하는 곳은 더미노드 head로 업데이트 됨

    def __iter__(self) -> DoubleLinkedListIterator:
        """반복자를 반환"""
        return DoubleLinkedListIterator(self.head)

    def __reversed__(self) -> DoubleLinkedListReverseIterator:
        """내림차순(역순) 반복자를 반환"""
        return DoubleLinkedListReverseIterator(self.head)


class DoubleLinkedListIterator:
    """DoubleLinkedList의 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.next

    def __iter__(self) -> DoubleLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


class DoubleLinkedListReverseIterator:
    """DoubleLinkedList의 내림차순(역순) 반복자용 클래스"""

    def __init__(self, head: Node):
        self.head = head
        self.current = head.prev

    def __iter__(self) -> DoubleLinkedListReverseIterator:
        return self

    def __next__(self) -> Any:
        if self.current is self.head:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.prev
            return data
# double_list.py 저장 -----


# [Do it! 실습 8-6] 원형 이중 연결 리스트 클래스 DoubleLinkedList 구현하기
from enum import Enum
from double_list import DoubleLinkedList

Menu = Enum('Menu', ['머리에노드삽입', '꼬리에노드삽입', '주목노드바로뒤삽입',
                     '머리노드삭제', '꼬리노드삭제', '주목노드출력',
                     '주목노드이동', '주목노드역순이동', '주목노드삭제',
                     '모든노드삭제', '검색', '멤버십판단', '모든노드출력',
                     '모든노드역순출력', '모든노드스캔', '모든노드역순스캔', '종료'])


def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


lst = DoubleLinkedList()  # 원형・이중 연결 리스트 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.머리에노드삽입:  # 맨 앞에 노드 삽입
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.: ')))
    elif menu == Menu.꼬리에노드삽입:  # 맨 끝에 노드 삽입
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.: ')))
    elif menu == Menu.주목노드바로뒤삽입:  # 주목 노드 바로 뒤에 삽입
        lst.add(int(input('주목 노드 바로 뒤에 넣을 값을 입력하세요 : ')))
    elif menu == Menu.머리노드삭제:  # 맨 앞 노드 삭제
        lst.remove_first()
    elif menu == Menu.꼬리노드삭제:  # 맨 끝 노드 삭제
        lst.remove_last()
    elif menu == Menu.주목노드출력:  # 주목 노드 출력
        lst.print_current_node()
    elif menu == Menu.주목노드이동:  # 주목 노드를 한 칸 뒤로 이동
        lst.next()
    elif menu == Menu.주목노드역순이동:  # 주목 노드를 한 칸 앞으로 이동
        lst.prev()
    elif menu == Menu.주목노드삭제:  # 주목 노드 삭제
        lst.remove_current_node()
    elif menu == Menu.모든노드삭제:  # 모두 삭제
        lst.clear()
    elif menu == Menu.검색:  # 검색
        pos = lst.search(int(input('검색할 값을 입력하세요.: ')))
        if pos >= 0:
            print(f'그 값의 데이터는 {pos + 1}번째에 있습니다.')
        else:
            print('해당 데이터가 없습니다.')
    elif menu == Menu.멤버십판단:  # 멤버십 판단
        print('그 값의 데이터는 포함되어'
              + (' 있습니다.' if int(input('판단할 값을 입력하세요.: ')) in lst else ' 있지 않습니다.'))
    elif menu == Menu.모든노드출력:  # 모든 노드를 출력
        lst.print()
    elif menu == Menu.모든노드역순출력:  # 모든 노드 역순 출력
        lst.print_reverse()
    elif menu == Menu.모든노드스캔:  # 모든 노드 스캔
        for e in lst:
            print(e)
    elif menu == Menu.모든노드역순스캔:  # 모든 노드 역순 스캔
        for e in reversed(lst):
            print(e)
    else:  # 종료
        break


# =========================
# 9장. 이진 트리 검색
# =========================

# 리스트는 순서를 매긴 데이터를 나열하는 자료구조
# 트리구조는 데이터 사이의 계층관계를 표현하는 자료구조

# # 이진 검색 트리(binary search tree)의 구현 bst.py 저장-----
# 왼쪽 서브트리노드의 키값은 자신의 노드키값보다 작아야한다
# 오른쪽 서브트리노드의 키값은 자신의 노드키값보다 커야한다

# from __future__ import annotations
from typing import Any, Type


class Node:
    """이진 검색 트리의 노드"""
    def __init__(self, key: Any, value: Any, left: Node = None,
                 right: Node = None):
        """생성자"""
        self.key = key      # 키
        self.value = value  # 값
        self.left = left    # 왼쪽 포인터(왼쪽 자식 참조), 기본값 None 지정
        self.right = right  # 오른쪽 포인터(오른쪽 자식 참조), 기본값 None 지정


class BinarySearchTree:
    """이진 검색 트리"""
    def __init__(self):
        """초기화"""
        self.root = None  # 루트

    def search(self, key: Any) -> Any:
        """키 key를 갖는 노드를 검색"""
        p = self.root           # 루트에 주목
        while True:
            if p is None:       # 더 이상 진행할 수 없으면(주목노드가 None이면)
                return None     # 검색 실패
            if key == p.key:    # key와 노드 p의 키가 같으면
                return p.value  # 검색 성공
            elif key < p.key:   # key 쪽이 작으면
                p = p.left      # 왼쪽 서브 트리에서 검색
            else:               # key 쪽이 크면
                p = p.right     # 오른쪽 서브 트리에서 검색

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고, 값이 value인 노드를 삽입(이진트리상태유지를주의)"""

        def add_node(node: Node, key: Any, value: Any) -> None:
            """node를 루트로 하는 서브 트리에 키가 key이고, 값이 value인 노드를 삽입"""
            if key == node.key:
                return False  # key와 같은 키를 갖는 노드가 존재하면 삽입하지 않음(False 반환)
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True

        if self.root is None:  # 트리가 빈 상태
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        """키가 key인 노드를 삭제"""
        p = self.root           # 스캔 중인 노드
        parent = None           # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:       # 더 이상 진행할 수 없으면
                return False    # 그 키는 존재하지 않음

            if key == p.key:    # key와 노드 p의 키가 같으면
                break           # 검색 성공
            else:
                parent = p                  # 가지를 내려가기 전에 부모를 설정
                if key < p.key:             # key 쪽이 작으면
                    is_left_child = True    # 여기서 내려가는 것은 왼쪽 자식
                    p = p.left              # 왼쪽 서브 트리에서 검색
                else:                       # key 쪽이 크면
                    is_left_child = False   # 여기서 내려가는 것은 오른쪽 자식
                    p = p.right             # 오른쪽 서브 트리에서 검색

        if p.left is None:                  # p에 왼쪽 자식이 없으면
            """자식노드가 없거나 1개인 경우"""
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right       # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right      # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:               # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left        # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴
            else:
                parent.right = p.left       # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            """자식노드가 2개인 경우"""
            parent = p
            left = p.left                   # 서브 트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key                # left의 키를 p로 이동
            p.value = left.value            # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left     # left를 삭제
            else:
                parent.right = left.left    # left를 삭제
        return True

    def dump(self, reverse=False) -> None:
        """덤프(모든 노드를 키의 오름차순/내림차순으로 출력)"""

        def print_subtree(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 오름차순으로 출력"""
            if node is not None:
                print_subtree(node.left)                # 왼쪽 서브 트리를 오름차순으로 출력
                print(f'{node.key}  {node.value}')      # node를 출력
                print_subtree(node.right)               # 오른쪽 서브 트리를 오름차순으로 출력

        def print_subtree_rev(node: Node):
            """node를 루트로 하는 서브 트리의 노드를 키의 내림차순으로 출력"""
            if node is not None:
                print_subtree_rev(node.right)           # 오른쪽 서브 트리를 내림차순으로 출력
                print(f'{node.key}  {node.value}')      # node를 출력
                print_subtree_rev(node.left)            # 왼쪽 서브 트리를 내림차순으로 출력

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        """가장 작은 키"""
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
        return p.key

    def max_key(self) -> Any:
        """가장 큰 키"""
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key
# bst.py 저장-----


# [Do it! 실습 9C-1] 이진 검색 트리 클래스 BinarySearchTree 사용하기(오름차순, 내림차순으로 덤프)
from enum import Enum
from bst import BinarySearchTree

Menu = Enum('Menu', ['삽입', '삭제', '검색', '오름차순덤프', '내림차순덤프', '키의범위', '종료'])


def select_Menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(' : '))
        if 1 <= n <= len(Menu):
            return Menu(n)


tree = BinarySearchTree()  # 이진 검색 트리를 생성

while True:
    menu = select_Menu()  # 메뉴 선택

    if menu == Menu.삽입:  # 삽입
        key = int(input('삽입할 키를 입력하세요.: '))
        val = input('삽입할 값을 입력하세요.: ')
        if not tree.add(key, val):
            print('삽입에 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        tree.remove(key)

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = tree.search(key)
        if t is not None:
            print(f'이 키를 갖는 값은 {t}입니다.')
        else:
            print('해당 데이터가 없습니다.')

    elif menu == Menu.오름차순덤프:  # 오름차순 덤프
        tree.dump()

    elif menu == Menu.내림차순덤프:  # 내림차순 덤프
        tree.dump(reverse=True)

    elif menu == Menu.키의범위:  # 키의 범위(최솟값과 최댓값)
        print(f'키의 최솟값은 {tree.min_key()}입니다.')
        print(f'키의 최댓값은 {tree.max_key()}입니다.')

    else:  # 종료
        break
