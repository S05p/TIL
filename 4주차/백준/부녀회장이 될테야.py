T = int(input())                # 테스트 케이스 

for _ in range(T):
    one_base = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    k = int(input())            # k층
    n = int(input())            # n호
    if n == 1:
        print(1)
    elif k == 0:
        print(n)
    else:
        for i in range(k):
            for j in range(n):
                one_base[0] = 1
                one_base[j] = one_base[j-1] + one_base[j]
                
        print(one_base[j])
        
        