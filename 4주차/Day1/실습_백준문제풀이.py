# 실습1

n_score = []
n_score.append(int(input()))
n_score.append(int(input()))
n_score.append(int(input()))
n_score.append(int(input()))
n_score.append(int(input()))

for i in range(len(n_score)):
    if n_score[i] < 40:
        n_score[i] = 40
        
print(int(sum(n_score)/len(n_score)))

# 실습2

n, x = map(int,input().split())

n_list = list(map(int,input().split()))
n_list_new = []

for i in range(len(n_list)):
    if n_list[i] < x:
        n_list_new.append(n_list[i])
        
print(*n_list_new)

# 실습3

a,b,c = map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)

# 실습4

N = int(input())
N_list = []


for i in range(N):
    a = int(input())
    N_list.append(a)
    
if sum(N_list) > len(N_list)/2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')

# 실습5

N = int(input())

N_list = list(map(int,input().split()))

cnt = 0
total = 0

for i in range(len(N_list)):
    if N_list[i] == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0
        
print(total)
    