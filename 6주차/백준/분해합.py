N = int(input())
N_min = []

for i in range(N,0,-1):
    i_s = str(i)
    i_l = len(i_s)
    i_w = 0
    i_w += i
    for j in range(i_l):
        i_w += int(i_s[j])
    if N == i_w:
        N_min.append(i)
        
if len(N_min) == 0:
    print(0)
else:
    print(min(N_min))