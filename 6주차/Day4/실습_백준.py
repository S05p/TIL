# 실습1 - 공

M = int(input())

M_dict = {1:1,2:0,3:0}

for _ in range(M):
    a,b = map(int,input().split())
    if M_dict[a] == 1:
        M_dict[a] = 0
        M_dict[b] = 1
    elif M_dict[b] == 1:
        M_dict[a] = 1
        M_dict[b] = 0

for k, v in M_dict.items():
    if v == 1:
        print(k)
        
# 실습2 - 콘테스트

w = []
k = []

for _ in range(10):
    w.append(int(input()))
    
for _ in range(10):
    k.append(int(input()))
    
w = sorted(w,reverse=True)
k = sorted(k,reverse=True)

w_s = sum(w[:3])
k_s = sum(k[:3])

print(w_s,k_s)

# 실습3 - 오르막길

N = int(input())
N_list = list(map(int,input().split()))
N_list_new = []
N_list_n = []

for i in range(N-1):
    N_list_new.append(N_list[i+1]-N_list[i])
   
cnt = 0
 
for j in range(len(N_list_new)):
    if N_list_new[j] >= 1:
        cnt += N_list_new[j]
        N_list_n.append(cnt)
    else:
        N_list_n.append(cnt)
        cnt = 0

print(max(N_list_n))

# 실습4 - 단어 나누기

N = str(input())
N = N
l = len(N)

N_list = []


for i in range(l-2):
    N_1 = N[:i+1][::-1]
    for j in range(i+1,l-1):
        N_2 = N[i+1:j+1][::-1]
        N_3 = N[j+1:][::-1]
        N_list.append(N_1+N_2+N_3)

print(sorted(N_list)[0])           
            
