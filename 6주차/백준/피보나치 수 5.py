N = int(input())

N_list = [0,1]

for i in range(20):
    N_list.append(N_list[i]+N_list[i+1])
    
print(N_list[N])