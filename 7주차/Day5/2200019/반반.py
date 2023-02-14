TC = int(input())
    
for i in range(1,TC+1):
    S = str(input())
    S_l = len(S)
    if S == S[0]*4:
        S = 'ABCD'
    for j in range(((len(S))//2)):
        k = S[0]
        S = S.replace(k,'',2)
    if len(S) != 0:
        print(f'#{i} No')
    else:
        print(f'#{i} Yes')