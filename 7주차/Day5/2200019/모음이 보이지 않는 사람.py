T = int(input())

for i in range(1,T+1):
    n = str(input())
    n = n.replace('a','')
    n = n.replace('e','')
    n = n.replace('i','')
    n = n.replace('o','')
    n = n.replace('u','')
    print(f'#{i} {n}')
    