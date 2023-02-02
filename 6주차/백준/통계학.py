from collections import Counter
import sys

N = int(sys.stdin.readline())
N_list = []

for _ in range(N):
    N_list.append(int(sys.stdin.readline()))
    
print(round(sum(N_list)/N))
N_list = sorted(N_list)

print(N_list[int(N/2)])

N_dict = Counter(N_list)
N_dict_wanted = []
for k,v in N_dict.items():
    if v == max(N_dict.values()):
        N_dict_wanted.append(k)
        N_dict_wanted = sorted(N_dict_wanted)

if len(N_dict_wanted) == 1:
    print(N_dict_wanted[0])
else:
    print(N_dict_wanted[1])
            
print(N_list[N-1] - N_list[0])
        
        