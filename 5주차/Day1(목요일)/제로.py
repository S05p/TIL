K = int(input())

k_list=[]

for i in range(K):
    k = int(input())
    if k !=0:
        k_list.append(k)
    else:
        k_list.pop()
        
print(sum(k_list))