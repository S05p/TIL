N = int(input())
N_list = []

for _ in range(N):
    N_list.append(int(input()))
    
N_list = sorted(N_list)
    
for i in N_list:
    print(i)