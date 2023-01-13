C = int(input())

for i in range(C):
    test_list = list(map(int,input().split()))
    test_aver = (sum(test_list[1:])/test_list[0])
    j_list=[]
    for j in test_list[1:]:
        if j > test_aver:
            j_list.append(j)
            
    print('{:.3f}'.format((len(j_list)/(len(test_list)-1))*100,6),'%',sep='')