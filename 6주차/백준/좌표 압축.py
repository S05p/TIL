import sys

N = int(sys.stdin.readline())

N_list = list(map(int,sys.stdin.readline().split()))
N_list_set = set(N_list)
N_list_zip = []

for i in N_list:
    cnt = 0
    for j in N_list_set:
        if i > j:
            cnt += 1
    N_list_zip.append(cnt)
    
print(*N_list_zip)