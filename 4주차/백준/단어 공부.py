n = str(input())
n_upper = n.upper()
n_dic={}

for i in n_upper:
    if i in n_dic:
        n_dic[i] += 1
    else:
        n_dic[i] = 1
        
n_dic_max = max(n_dic.values())
n_dic_max_list = []

for j in n_dic.keys():
    if n_dic[j] == n_dic_max:
        n_dic_max_list.append(j)
        

if len(n_dic_max_list) >= 2:
    print('?')
else:
    print(*n_dic_max_list)