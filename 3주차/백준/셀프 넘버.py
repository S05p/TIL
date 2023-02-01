def d(n):
    
    sel_num = []
    q_list = []
    
    for i in range(1,n+1):
        k = 0
        for j in str(i):
            k += int(j)
            sel_num.append(k)
            
    for q in range(1,n+1):
        q_list[q] = [q]
        
    for y in range(len(sel_num)):
        if sel_num[y] in q_list:
            q_list.pop(sel_num[y])
            
    
    
    return d(n)

print(d(10000))