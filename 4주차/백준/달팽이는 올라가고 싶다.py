import sys

a,b,v = map(int,sys.stdin.readline().split())

v_a = v-a
n = (v-a)//(a-b)


if a>=v:
    print(1)
elif n*(a-b)+a >= v:
    print(n+1)
elif n*(a-b)+a < v:
    print(n+2)
    
