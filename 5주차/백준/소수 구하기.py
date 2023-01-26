import sys

a,b = map(int,sys.stdin.readline().split())

import math

def prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(x))+1):
            if x%i == 0:
                return False
        return True
    
for j in range(a,b+1):
    if prime_number(j) == True:
        print(j)