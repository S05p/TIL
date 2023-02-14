T = int(input())

for i in range(1,T+1):
    n= int(input())
    n_list = list(map(str,input().split()))
    n_list_shuffle = []
    
    if n%2 ==0:
        for j in range(n//2):
            n_list_shuffle.append(n_list[j])
            n_list_shuffle.append(n_list[j+(n//2)])
            
    else:
        for j in range(n//2):
            n_list_shuffle.append(n_list[j])
            n_list_shuffle.append(n_list[j+(n//2)+1])
        n_list_shuffle.append(n_list[n//2])
        
    print(f'#{i}',*n_list_shuffle)