# 1 > 2 > 3 > 4 > 5

N = int(input())
n = 0

while True:
    n += 1
    if (((n+1)*n)/2) >= N:
        k = n
        N = N-(((n-1)*n)/2)
        break

N = int(N)
    
if k%2 == 1:
    print(k+1-N,'/',N,sep='')
else:
    print(N,'/',k+1-N,sep='')