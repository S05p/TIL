n = int(input())

for i in range(1,n+1):
    r = map(int,input().split())
    print(f'#{i} {max(r)}')