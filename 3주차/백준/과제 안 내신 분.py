c_list = []

for i in range(1,29):
    c = int(input())
    c_list.append(c)

    
for j in range(1,31):
    if j not in c_list:
        print(j)

