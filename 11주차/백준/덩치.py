N = int(input())
N_list = []
N_list_score = []
score = 0

for i in range(1,N+1):
    a, b = map(int,input().split())
    N_list.append([a,b,i])
    
N_list.append([0,0,0])
N_list = sorted(N_list,reverse=True)

for i in range(1,N+1):
    N_list[i-1].append(i)
    
for j in range(N):
    if N_list[j][0] > N_list[j+1][0]:
        if N_list[j][1] > N_list[j+1][1]:
            N_list[j][3] == N_list[j][3]
        else:
            N_list[j+1][3] = N_list[j][3]

for q in range(N):
    N_list_score.append(N_list[q][2:4])
    
N_list_score = sorted(N_list_score)

for p in range(N):
    print(N_list_score[p][1],end=' ')