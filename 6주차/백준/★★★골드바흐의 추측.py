# import sys
# import math
# from collections import deque

# def prime_number(x):
#     if x >= 2:
#         for i in range(2,int(math.sqrt(x))+1):
#             if x%i == 0:
#                 return False
#     return True        
            
# qedue = deque(range(1,10001))

# prime_num_list = deque(set())

# for z in qedue:
#     if prime_number(z) == True:
#         prime_num_list.append(z)

# T = int(sys.stdin.readline())

# for _ in range(T):
#     n = int(sys.stdin.readline())
#     jk_list = []
#     for j in prime_num_list:
#         if j <= n:
#             for k in prime_num_list:
#                 if k <= n:
#                     if k >= j:
#                         if j+k == n:
#                             if len(jk_list) == 0:
#                                 jk_list.append(j)
#                                 jk_list.append(k)
#                             else:
#                                 if (jk_list[1]-jk_list[0]) > (j-k):
#                                     jk_list[0] = j
#                                     jk_list[1] = k
#     print(*jk_list)

# ==============================================================================
# 시간 초과가 어떻게 해결이 안된다.
# 기존에 내가 아는 방법으로는 해결이 안되는듯 싶다.
# 구글링 결과 기가막힌 답을 찾게 되었다.
# 주어진 숫자를 반갈죽해서 
# - +를 반복하면 된다는것... 그럼 계산도 훨씬 적어질테고
# 이걸 어떻게 생각하지...?

import sys
import math

def prime_number(x):
    if x >= 2:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
    return True        

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    a = n//2 
    b = n//2
    while a>0:
        if prime_number(a) == True and prime_number(b) == True:
            print(a,b)
            break
        else:
            a -= 1
            b += 1
    
    
    
    
