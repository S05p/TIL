# 블랙잭  ___ 틀렸다... 이유가 뭐지..?

a, b = map(int,input().split())

a_list = list(map(int,input().split()))

assum_list = []

for i in range(0,a-2):
    for j in range(i+1,a-1):
        for k in range(i+2,a):
            assum = a_list[i]+a_list[j]+a_list[k]
            if assum <= b:
                assum_list.append(assum)
            
assum_list = list(set(assum_list))
minum_list = []
      
for i in assum_list:
    minum_list.append(abs(i-b))
    
want_index_i = minum_list.index(min(minum_list))

print(assum_list[want_index_i])




