n = int(input())

for i in range(1,n+1):
    aver_test = list(map(int,input().split()))
    
    print(f'#{i} {round(sum(aver_test)/len(aver_test))}')