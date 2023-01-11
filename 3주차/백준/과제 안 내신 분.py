c_list = []
i_list = []
for i in range(1,29):
    c = int(input())
    c_list.append(c)
    c_list = sorted(c_list)
    
for j in range(1,31):
    i_list.append(j)

for k in range(30):
    if i_list[k] not in c_list:
        print(k+1)