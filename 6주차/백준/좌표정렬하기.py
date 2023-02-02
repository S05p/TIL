import sys

N = int(sys.stdin.readline())

N_list = []

for _ in range(N):
    n = list(map(int,sys.stdin.readline().split()))
    N_list.append(n)
    
N_list = sorted(N_list, key=lambda x : (x[0],x[1]))

for i in range(N):
    print(*N_list[i])


        