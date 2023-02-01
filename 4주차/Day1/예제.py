# 예제1

a, b=  map(int,input().split())

print(a+b)

# 예제2

a = int(input())
b = int(input())

print(a+b)

# 예제3

n = int(input())

for _ in range(n):
    a, b = map(int,input().split())
    print(a,b)

# 예제4

n = int(input())
for _ in range(n):
    a, b = map(int,input().split(','))
    print(a+b)

# 예제5

n = int(input())
for i in range(1,n+1):
    a, b = map(int,input().split())
    print(f'Case #{i}: {a+b}')
    
# 예제6

n = int(input())
for i in range(1,n+1):
    a, b = map(int,input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')
