n_0 = str(input())
n = str(' '+ n_0 + '  ')
cnt = 0

for i in range(len(n)-2):
    cnt += 1
    if n[i] == 'c':
        if n[i+1] == '=':
            cnt -= 1
        elif n[i+1] == '-':
            cnt -= 1
    if n[i] == 'd':
        if n[i+1] =='z':
            if n[i+2] == '=':
                cnt -= 2
        elif n[i+1] == '-':
            cnt -= 1
    if n[i] == 'l':
        if n[i+1] == 'j':
            cnt -= 1
    if n[i] == 'n':
        if n[i+1] == 'j':
            cnt -= 1
    if n[i] == 's':
        if n[i+1] == '=':
            cnt -= 1
    if n[i] == 'z':
        if n[i-1] != 'd':
            if n[i+1] == '=':
                cnt -= 1
            
print(cnt-1)