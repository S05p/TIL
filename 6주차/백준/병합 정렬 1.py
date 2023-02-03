N, K = map(int,input().split())
N_list = list(map(int,input().split()))

while True:
    N_1 = []
    if N_list != N_list.sort():
        for i in range(len(N_list)-1):
            N_1.append(N_list[i+1]-N_list[i])
            