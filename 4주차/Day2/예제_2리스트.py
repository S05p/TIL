# 예제1

N= int(input())

n = list(map(int,input().split()))

print(min(n),max(n))

# 예제2

N= int(input())
n = map(int,input())

print(sum(n))

# 예제3

N = int(input())
N_list = []


for i in range(N):
    n = int(input())
    N_list.append(n)
    
N_list = sorted(N_list)

for j in N_list:
    print(j)

# 예제4

N = []

for i in range(9):
    n = int(input())
    N.append(n)
    
print(max(N))
print(min(N))
