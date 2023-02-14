T = int(input())

for i in range(1,T+1):
    N, K = map(int,input().split())
    N_list = [[] for _ in range(N)]
    N_dict = {}
    hill_point = []
    # 행 N개 만들어짐
    for j in range(N):
        N_list[j] = list(map(int,input().split()))
    for p in range(N):
        for q in range(N):
            
            N_dict[p+q] = 
    hill = 0
    for q in range(N):
        if hill <= max(N_list[q]):
            hill = max(N_list[q])
    # hill = 9
    for y in range(N):
        for x in range(N):
            if N_list[y][x] == hill:
                hill_point.append([y,x])
    
    
# 포기 포기
    
        

    
