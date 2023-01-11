z_list = []

for i in range(10):
    n = int(input())
    n_0 = n%42
    if n_0 not in z_list:
        z_list.append(n_0)
    
print(len(z_list))