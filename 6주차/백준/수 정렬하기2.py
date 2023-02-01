import sys

N_list = []

for _ in range(int(sys.stdin.readline())):
    N_list.append(int(sys.stdin.readline()))
    
N_list = sorted(N_list)

for i in N_list:
    print(i)

    