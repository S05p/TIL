import sys

N = int(sys.stdin.readline())
N_list = []

for _ in range(N):
    n = list(map(str,sys.stdin.readline().split()))
    N_list.append([int(n[0]),n[1]])
    
    
N_list = sorted(N_list, key=lambda x: (x[0]))

for i in range(N):
    print(*N_list[i])