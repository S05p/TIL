import sys

T = int(input())

for _ in range(T):
    h,w,n = map(int,sys.stdin.readline().split())
    ACM = []
    for i in range(1,w+1):
        if i < 10:
            i = '0' + str(i)
        else:
            i = str(i)
        for j in range(1,h+1):
            j = str(j)
            room_num = j + i
            ACM.append(room_num)
    print(ACM[n-1])
            

            
            
                