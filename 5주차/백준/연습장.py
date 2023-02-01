# import math

# print(math.sqrt(5))
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

from collections import deque

qedue = deque(range(1,10001))

prime_num_list = deque([])

for z in qedue:
    if prime_number(z) == True:
        prime_num_list.append(z)
        
print(prime_num_list)