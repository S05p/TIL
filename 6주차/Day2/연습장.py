def fac(x):
    cnt = 0
    result = 0
    while True:
        if x == cnt:
            cnt += 1
            result += cnt
        return result
            
    
print(fac(10))