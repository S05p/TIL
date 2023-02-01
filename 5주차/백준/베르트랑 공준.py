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
while True:
    n = int(sys.stdin.readline())
    cnt = 0
    if n == 0:
        break
    elif n == 1:
        print(1)
        continue
    for j in range(n+1,2*n):
        if prime_number(j) == True:
            cnt += 1
            
    print(cnt)
    
## 아이디어는 모든 소수를 다 카운트해가면서 할 필요가 없다는 것
# 그래서 리스트에 추가를 해서 그 뒤로 모두 비교하면 되지 않을까? 하는 거시다

