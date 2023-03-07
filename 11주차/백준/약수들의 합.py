while True:
    
    N = int(input())
    if N == -1:
        break
    
    N_list = []
    
    for i in range(1,(N//2)+1):
        if N%i == 0:
            N_list.append(i)
    
    if sum(N_list) != N:
        print(f'{N} is NOT perfect.')
    else:
        print(N,'= ',end='')
        print(*N_list,sep=' + ')