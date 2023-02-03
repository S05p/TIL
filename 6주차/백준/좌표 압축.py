import sys

N = int(sys.stdin.readline())

N_list = list(map(int,sys.stdin.readline().split()))
N_list_set = sorted((set(N_list)))
N_list_dic = {N_list_set[i]:i for i in range(len(N_list_set))}

for i in N_list:
    print(N_list_dic[i],end = ' ')
