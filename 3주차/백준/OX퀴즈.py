n= int(input())


for i in range(n):
    quiz = str(input())
    cnt=0
    cnt_z=0
    for j in quiz:
        if j == 'O':
            cnt_z += 1
            cnt += cnt_z
        else:
            cnt_z=0
    print(cnt)     
        
