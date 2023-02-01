# 실습1 - 시험 성적

n = int(input())

if n >= 90:
    print('A')
elif n >= 80:
    print('B')
elif n >= 70:
    print('C')
elif n >= 60:
    print('D')
else:
    print('F')
    
# 실습2 - 단어 뒤집기

T = int(input())

for _ in range(T):
    test_case = list(map(str,input().split()))
    test_case_2 = []
    for i in range(len(test_case)):
        
        test_case_2.append(test_case[i][::-1])
        
    print(*test_case_2)
    
# 실습3 - 열 개씩 끊어 출력하기

S = str(input())

while True:
    if len(S) < 10:
        print(S)
        break
    else:
        print(S[:10])
        S = S[10:]
    
# 실습4 - 나무 조각

W = list(map(int,input().split()))
W_0 = sorted(W)

while True:
    if W[0] > W[1]:
        w_0 = W[0]
        w_1 = W[1]
        W[0] = w_1
        W[1] = w_0
        print(*W)
        
    if W[1] > W[2]:
        w_1 = W[1]
        w_2 = W[2]
        W[1] = w_2
        W[2] = w_1
        print(*W)

    if W[2] > W[3]:
        w_2 = W[2]
        w_3 = W[3]
        W[2] = w_3
        W[3] = w_2
        print(*W)
        
    if W[3] > W[4]:
        w_3 = W[3]
        w_4 = W[4]
        W[3] = w_4
        W[4] = w_3
        print(*W)
        
    if W == W_0:
        break