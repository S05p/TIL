list=list(map(int,input().split()))

list_dic = {list[i]:list.count(list[i]) for i in range(len(list))}

for k,v in list_dic.items():
    if v==3:
        print(10000+k*1000)
    elif v==2:
        print(1000+k*100)
        break
    else:
        print(max(list)*100)
        break
    
# 맞는데...?

