def alg(x):
    
    y = len(x)
    front_list = x[:(y+1//2)]
    back_list = x[(y+1//2):]
    alg(front_list)
    
    
    
    
    
    
    
N, K = map(int,input().split())