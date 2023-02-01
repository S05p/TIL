# 실습1 - 이상한 곱셈

a, b = map(str,input().split())
n_1 = 0
for i in a:
    for j in b:
        n_1 += int(i)*int(j)

print(n_1)

# 실습2 - 별 찍기 -1

N = int(input())

for i in range(1,N+1):
    print('*'*i)

# 실습3 - 구구단

N = int(input())

for i in range(1,10):
    print(f'{N} * {i} = {N*i}')


# 실습4 - 나는 요리사다

n_4_final = []
n_4_final_sum = []

for i in range(5):
    n_4_list = list(map(int,input().split()))
    n_4_final.append(n_4_list)
    n_4_final_sum.append(sum(n_4_list))
    
if n_4_final_sum.count(max(n_4_final_sum)) == 1:
    print(n_4_final_sum.index(max(n_4_final_sum))+1, max(n_4_final_sum))
    
# 실습 5 - 직사각형 네개의 합집합의 면적 구하기

n_5_sum = []

for _ in range(4):
    n_5 = list(map(int,input().split()))
    x = n_5[0]
    for i in range(n_5[2]-n_5[0]):
        x += 1
        y = n_5[1]
        for j in range(n_5[3]-n_5[1]):
            y += 1
            n_new = [[x-1,y-1],[x-1,y],[x,y-1],[x,y]]
            if n_new not in n_5_sum:
                n_5_sum.append(n_new)

print(len(n_5_sum))