# 실습1 - 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())

if a+b+c != 180:
    print('Error')
elif a==60 and b==60 and c==60:
    print('Equilateral')
elif a==b:
    print('Isosceles')
elif a==c:
    print('Isosceles')
elif b==c:
    print('Isosceles')
else:
    print('Scalene')
    
# 실습2 - 세탁소 사장 동혁

T = int(input())            #테스트 케이스

for _ in range(T):
    C = int(input())
    c_list = []
    c_list.append(C//25)
    C = C%25
    c_list.append(C//10)
    C = C%10
    c_list.append(C//5)
    C = C%5
    c_list.append(C)
    print(*c_list)

# 실습3 - 피시방 알바

n = int(input())                #손님의 수

n_list = list(map(int,input().split()))
n_list_set = set(n_list)

print(len(n_list)-len(n_list_set))

# 실습4 - 제로

k = int(input())
k_list = []

for i in range(k):
    n = int(input())
    if n != 0:
        k_list.append(n)
    else:
        k_list.pop()

print(sum(k_list))

# 실습5 - 카드1

from collections import deque

n = int(input())
n_range = deque(range(1,n+1))
n_discard = []

while len(n_range)>1:
    n_discard.append(n_range.popleft())
    n_range.append(n_range.popleft())
    
print(*n_discard, n_range[0])

# 실습6 - 괄호

T = int(input())

for i in range(T):
    test_case = str(input())
    while True:
        test_case = test_case.replace('()','')
        if '()' not in test_case:
            if len(test_case) == 0 :
                print('YES')
                break
            else:
                print('NO')
                break
