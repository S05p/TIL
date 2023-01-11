max_i = 0
i_list= []

for i in range(9):
    i = int(input())
    i_list.append(i)
    
print(max(i_list))
print(i_list.index(max(i_list))+1)
