# 실습1 - 세 수

import sys

a = list(map(int,sys.stdin.readline().split()))

a = sorted(a)

print(a[1])

# 실습2- 고무오리 디버깅

N = str(input())
q_list = []


while True:
    n = str(input())
    if n == '문제':
        q_list.append(1)
    elif n == '고무오리':
        if len(q_list) == 0:
            q_list.append(1)
            q_list.append(1)
        else:
            q_list.pop()
    elif n == '고무오리 디버깅 끝':
        if len(q_list) == 0:
            print('고무오리야 사랑해')
            break
        else:
            print('힝구')            
            break

# 실습3 - 대칭 차집합

import sys

a, b = map(int,sys.stdin.readline().split())

a_set = set(map(int,sys.stdin.readline().split()))
b_set = set(map(int,sys.stdin.readline().split()))

cnt = len(a_set - b_set)
cnt += len(b_set - a_set)

print(cnt)

# 실습4 - 나머지

n_4_list = []

for _ in range(10):
    n = int(input())
    n = n%42
    n_4_list.append(n)
    
n_4_set = set(n_4_list)

print(len(n_4_set))

# 실습5 - 단어 정렬

n = int(input())
n_list = []

for _ in range(n):
    n_str = str(input())
    n_list.append(n_str)

n_list = set(n_list)
n_list = sorted(n_list)
n_list_len = []

for i in n_list:
    n_list_len.append(len(i))
    
n_list_len = set(n_list_len)
n_list_len = sorted(n_list_len)

for j in n_list_len:
    for k in n_list:
        if j == len(k):
            print(k)

# 실습6 - 절대값 힙

import sys
import heapq
from heapq import heappush
from heapq import heappop

N = int(sys.stdin.readline())
n_list=[]

for i in range(N):
    n = int(sys.stdin.readline())
    if n != 0:
        heappush(n_list,(abs(n),n))
    else:
        if len(n_list) == 0:
            print(0)
        else:
            print(heappop(n_list)[1])


            
