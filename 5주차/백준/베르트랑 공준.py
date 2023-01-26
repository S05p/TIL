import sys
import math

def prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True
prime_number_list=[]
while True:
    n = int(sys.stdin.readline())
    cnt = 0
    if n == 0:
        break
    for j in range(n+1,2*n):
        if prime_number(j) == True:
            cnt += 1
            prime_number_list.append(j)
            
    print(cnt)