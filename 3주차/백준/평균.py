n= int(input())
n_list=(list(map(int,input().split())))
n_list_max = max(n_list)
n_list_trict = []

for i in range(len(n_list)):
    new_n = (n_list[i]/n_list_max)*100
    n_list_trict.append(new_n)
    
print(sum(n_list_trict)/len(n_list_trict))