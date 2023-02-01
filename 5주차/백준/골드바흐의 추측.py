import sys
import math
from collections import deque

def prime_number(x):
    if x == 1:
        return False
    elif x >= 2:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
    return True        
            
qedue = deque(range(1,10001))

prime_num_list = deque(set())

for z in qedue:
    if prime_number(z) == True:
        prime_num_list.append(z)

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    jk_list = []
    for j in prime_num_list:
        if j <= n:
            for k in prime_num_list:
                if k <= n:
                    if k >= j:
                        if j+k == n:
                            if len(jk_list) == 0:
                                jk_list.append(j)
                                jk_list.append(k)
                            else:
                                if (jk_list[1]-jk_list[0]) > (j-k):
                                    jk_list[0] = j
                                    jk_list[1] = k
    print(*jk_list)
