total = int(input())

n = int(input())

check = 0

for i in range(n):
    a, b = map(int,input().split())
    check += a*b
    
if check == total:
    print('Yes')
else:
    print('No')