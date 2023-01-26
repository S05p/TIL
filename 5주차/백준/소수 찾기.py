import sys

n = int(sys.stdin.readline())
cnt = 0

def prime_number(x):
    if x == 1:
        return False
    else:
        for i in range(2,x):
            if x%i ==0 :
                return False
        return True
    
N_list = list(map(int,sys.stdin.readline().split()))

for i in N_list:
    if prime_number(i) == True:
        cnt += 1
        
print(cnt)