def dfs(graph, start):
    visited, need_visit = [],[]
    
    need_visit.append(start)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                need_visit.extend(graph[node])
                
    return visited    

T = int(input())

for i in range(1,T+1):
    N, M = map(int,input().split())
    N_list= {i:[] for i in range(N)}
    N_solution = set()
    for _ in range(M):
        a, b = map(int,input().split())
        N_list[a-1].append(b-1)
        N_list[b-1].append(a-1)
        
    for q in range(N):
        N_solution.add(str(sorted(dfs(N_list,q))))
        
    print(f'#{i} {len(N_solution)}')
    
    