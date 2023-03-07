import sys

N, K = map(int,sys.stdin.readline().split())
i_cnt = 0
N_list = []

for i in range(1,N+1):
    if N%i == 0:
        N_list.append(i)
        i_cnt += 1
        

if K <= i_cnt:
    print(N_list[K-1])
else:
    print(0)