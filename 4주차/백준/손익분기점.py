a, b, c = map(int,input().split())
n = 0

c_b = c-b

if b>=c:
    print(-1)
else:
    print((a//c_b)+1)