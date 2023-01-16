n = int(input())

cnt = 0

if n <= 99:
    cnt += n
    print(cnt)
elif n >= 100:
    cnt += 99
    for i in range(100,n+1):
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            cnt += 1
            
    print(cnt)       

    
    

