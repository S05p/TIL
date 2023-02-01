# 실습1 - 별 찍기 - 4

N = int(input())

for i in range(1,N+1):
    print((' '*(i-1)),end='')
    print(((N-i+1)*'*'))

# 실습2 - 대표값

from collections import Counter

N_list = [int(input()) for i in range(10)]

N_dict = Counter(N_list)

print(int(sum(N_list)/len(N_list)))
print(*[k for k, v in N_dict.items() if v == max(N_dict.values())])

# 실습3 - 세로읽기

N_5 = []
n = 0

for _ in range(5):
    N_list = list(map(str,input()))
    N_5.append(N_list)
    if len(N_list) > n:
        n = len(N_list)

for z in N_5:
    while n > len(z):
        z.append(' ')
    
for i in range(len(N_5[0])):
    for j in range(5):
        print(N_5[j][i].replace(' ',''),end='')
    
# 실습4 - 박스 못 품

T = int(input())

for _ in range(T):
    m, n = map(int,input().split())
    grid = [[] for _ in range(n)]
    for i in range(m):
        a = list(input().split())
        for j in range(n):
            grid[j].append(a[j])
        
# 실습5 -누울 자리를 찾아라     못 품