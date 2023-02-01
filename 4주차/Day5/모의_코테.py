# 모의_코테 - 최빈수 구하기

from collections import Counter

T = int(input())                                # 테스트 갯수

for i in range(1,T+1):                          # T+1만큼 반복
    n = int(input())                                            
    T_list = list(map(int,input().split()))      # T_list 입력
    T_list_dict = Counter(T_list)
    T_list_cnt_max = []
    for key, values in T_list_dict.items():
        if values == max(T_list_dict.values()):
            T_list_cnt_max.append(key)
    print(f'#{n} {max(T_list_cnt_max)}')
    

# 모의_코테 - 직사각형 길이 찾기

from collections import Counter

T = int(input())

for i in range(1,T+1):
    a = list(map(int,input().split()))
    a_dict = Counter(a)
    for key,value in a_dict.items():
        if value == 3:
            wanted = key
        elif value == 1:
            wanted = key
        
    print(f'#{i} {wanted}')

# 모의_코테 - 소득 불균형

from collections import Counter

T = int(input())

for i in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    a_avr = (sum(a)/len(a))
    a_dict = Counter(a)
    p_c = 0
    
    for key, value in a_dict.items():
        if key <= a_avr:
            p_c += value
            
    print(f'#{i} {p_c}')

# 모의_코테 - 문자열의 거울상

# qppdb
# pqqbd

T = int(input())

for i in range(1,T+1):
    t_c = str(input())
    t_c_0 = t_c[::-1]
    t_c_1 = ''
    for j in t_c_0:
        if j == 'q':
            t_c_1 += 'p'
        elif j == 'p':
            t_c_1 += 'q'
        elif j == 'd':
            t_c_1 += 'b'
        elif j =='b':
            t_c_1 += 'd'
    print(f'#{i} {t_c_1}')    
    
# 모의 코테 - 신용카드 만들기 1

T = int(input())

for i in range(1,T+1):
    n = list(map(int,input().split()))
    cnt = 0
    for j in range(15):
        if (j+1)%2 == 1:
            cnt += n[j]*2
        else:
            cnt += n[j]
    
    if cnt % 10 == 0 :
        print(f'#{i} 0')
    else:
        print(f'#{i} {10-(cnt%10)}')

# 모의 코테 - 신용카드 만들기 2

T = int(input())

for i in range(1,T+1):
    n = str(input())
    n = n.replace('-','')
    n_able = ['3','4','5','6','9']
    if n[0] in n_able:
        if len(n) ==16:
            print(f'#{i} 1')
        else:
            print(f'#{i} 0')
    else:
        print(f'#{i} 0')