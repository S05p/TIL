def n_1(x):
    if len(x)==1:
        return x
    
    mid = (len(x)+1)//2
    left = n_1(x[:mid])
    right = n_1(x[mid:])
    
    n_2 = []
    i = 0
    j = 0
    
    if left[0] > i and right[0] > j:
        if left[0]> right[0]:
            n_2.extend(left)
        else:
            n_2.extend(right)
            
    if left[i] > i 
    
            
            
            
            
            
            
            
            
