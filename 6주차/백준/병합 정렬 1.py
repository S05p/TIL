

N, K = map(int,input().split())
N_list = list(map(int,input().split()))
N_list_s = sorted(N_list)
cnt = 0
cnt_n = 0
N_i = (N//2)            

N_f = sorted(N_list[:(N_i)+1])
N_b = sorted(N_list[(N_i)+1:])

N_dict = {}

for i in range(N_i):
    cnt += 1
    cnt_n = N_list[i]
    N_dict[cnt] = N_list[i]
    
for j in range(len(N_f)):
    cnt += 1
    cnt_n = N_f[j]
    N_dict[cnt] = N_f[j]
    
for k in range(len(N_b)):
    cnt += 1
    cnt_n = N_b[k]
    N_dict[cnt] = N_b[k]
    
for q in range(N):
    cnt += 1
    cnt_n = N_list_s[q]
    N_dict[cnt] = N_list_s[q]



if K > cnt:
    print(-1)
else:
    print(N_dict[K])