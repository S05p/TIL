import sys

n = int(sys.stdin.readline())
n_list = list(range(2,n+1))

while n>1:
    for i in n_list:
        if n%i == 0:
            print(i)
            n = n//i
            break