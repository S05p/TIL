n = int(input())

for _ in range(n):
    cnt_s = list(map(str,input().split()))
    repeat_cnt = int(cnt_s[0])
    s_word = cnt_s[1]
    ww = []
    for j in s_word:
        ww.append(repeat_cnt*j)
    
    print(*ww,sep='')
    
