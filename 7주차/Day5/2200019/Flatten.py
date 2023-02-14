for i in range(1,11):
    n = int(input())
    Fla_list = list(map(int,input().split()))
    for _ in range(n):
        Fla_list.append((Fla_list.pop(Fla_list.index(max(Fla_list))))-1)
        Fla_list.append((Fla_list.pop(Fla_list.index(min(Fla_list))))+1)
        
    print(f'#{i} {max(Fla_list)-min(Fla_list)}')
    