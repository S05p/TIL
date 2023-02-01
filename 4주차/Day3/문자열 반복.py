n = int(input())
N_str = ''

for i in range(n):
    N = str(input())
    N_0 = N[0]
    for j in range(len(N)-2):
        N_str += N[j+2]*int(N_0)
        
    print(N_str)
    N_str = ''