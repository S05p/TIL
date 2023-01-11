# 문제1

n_1 = list(map(int,input().split()))
print(*n_1)

# 문제2

n_2 = list(map(str,input().split()))
print(*n_2)

# 문제3

n_3 = int(input())
n_3_1 = []

for i in range(n_3):
    n_3_0 = int(input())
    n_3_1.append(n_3_0)
    
for j in range(n_3):
    print(n_3_1[j])

# 문제4

n_4 = int(input())
n_4_1 = []

for i in range(n_4):
    n_4_0 = map(int,input().split())
    n_4_1.append(n_4_0)
    
for j in range(n_4):
    print(*n_4_1[j])

# 문제5

n_5 = int(input())
n_5_list = []

for i in range(n_5):
    n_5_t = int(input())
    for j in range(n_5_t):
        n_5_list.insert(j,map(str,input().split()))
    for k in range(n_5_t):
        print(*n_5_list[k])
        
# 문제6

n_6 = int(input())
n_6_list = []

for i in range(n_6):
    n_6_t = int(input())
    for j in range(n_6_t):
        n_6_list.insert(j,map(int,input().split()))
    for k in range(n_6_t):
        print(*n_6_list[k])

# 문제7

c, n = map(int,input().split())

for i in range(c):
    for j in range(n):
        k = map(int,input().split())
        print(*k)

# 문제8

c, n = map(int,input().split())

for i in range(c):
    for j in range(n):
        k = map(int,input().split())
        print(*k)
        
# 문제9

c, n = map(int,input().split())

for i in range(c):
    for j in range(n):
        k = map(int,input().split())
        print(*k)