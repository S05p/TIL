N = int(input())

N_list = list(range(1,N+1))
N_list_new = []

for i in range(N):
    if len(N_list) > 1:
        N_list_new.append(N_list[0])
        N_list.pop(0)
        N_list.append(N_list[0])
        N_list.pop(0)
    else:
        N_list_new.append(N_list[0])
        
print(*N_list_new)
    
    
