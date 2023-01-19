
# 존내 어렵다 ㅁㄴ아ㅓㄹ;ㅏㅁ널;ㅣㅏㅓㅁㄴ;어ㅏㄹ;미나ㅓㅇㄹ;ㅣㅏㅓㄴㅁㅇ러ㅏㅣㄴ머ㅣㅏㄹㅇ
# 겨우 풀었어

T = int(input())
T_list = []
g_c = 0


for _ in range(T):
    s = str(input())
    s = s + ' '
    for i in range(len(s)-2):
        if s[i] == s[i+1]:
            s = ' ' + s[:i] + s[i+1:]  
    s = s.strip()
    s = ' ' + s + ' '
    cnt = 0
    
    for j in range(1,len(s)-1):
        if s[j] in s[:j-1] and s[j+1:]:
            cnt -= 100000
        else:
            cnt += 1
    if cnt >= 0:
        g_c += 1
            
print(g_c)

