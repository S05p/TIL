# 실습1 - 오븐 시계

h, m = map(int,input().split())
t = int(input())

if m+t < 60:
    print(h, m+t)
elif m+t >= 60:
    h_t = (m+t)//60
    m_t = (m+t)%60
    if h + h_t >= 24:
        print(h+ h_t - 24, m_t)
    else:
        print(h+h_t,m_t)

# 실습2 - 블랙잭

N, M = map(int,input().split())

N_list = list(map(int,input().split()))
N_assum_list = []

for i in range(0,N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (N_list[i] + N_list[j] + N_list[k]) <= M:
                N_assum_list.append((N_list[i] + N_list[j] + N_list[k]))
                
print(max(N_assum_list))

# 실습3 - 점수집계

T = int(input())

for _ in range(T):
    n = list(map(int,input().split()))
    n = sorted(n)
    if (n[3] - n[1]) >= 4:
        print('KIN')
    else:
        print(sum(n[1:4]))

# 실습4 - 가장 큰 금민수

N = int(input())
n_4 = ['4','7']

for i in range(N,-1,-1):
    minsu_str = str(i)
    for j in minsu_str:
        if j in n_4:
            result = True
        else:
            result = False
            break
    if result == True:
        print(i)
        break

# 실습5 - 영화감독 숌


N = int(input())
N_list = []

for i in range(666,2666800):
    li = len(str(i))
    si = str(i)
    for j in range(li-2):
        if si[j] == '6':
            if si[j+1] == '6':
                if si[j+2] == '6':
                    N_list.append(i)

N_list = sorted(list(set(N_list)))

print(N_list[N-1])
        
