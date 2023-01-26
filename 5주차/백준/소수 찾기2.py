import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime_list=[]

def prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True

    
for j in range(M,N+1):
    if prime_number(j) == True:
        prime_list.append(j)
        
if len(prime_list) == 0:
    print(-1)
else:
    print(sum(prime_list))
    print(min(prime_list))
    