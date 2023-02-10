'''
N, K= map(int,input().split())
cnt = 0

N_list = list(map(int,input().split()))
N_list_new = []


if N%2 == 1:
    N_list_left = (N//2)+1
    # 0 1 2 3
    N_list_right = (N//2)+1
    # 4 5 6 7
else:
    N_list_left = (N//2)
    N_list_right = (N//2)
        
if N_list_left%2 == 1:
    for i in range(0,(N//2),2):
        N_list_new.append(N_list[i:i+2])
    N_list_new.append([N_list[(N//2)]])
    for j in range((N//2)+1,N,2):
        N_list_new.append(N_list[j:j+2])
else:
    for i in range(0,N,2):
        N_list_new.append(N_list[i:i+2])
    
# print([N_list_new[0]+N_list_new[1]])

for k in range(len(N_list_new)):
    cnt += 1
    
### 진짜 모르겠다 진짜 진짜 모르겠음

## 그냥 풀이보고 해석하자
# 이건 안된다.

'''

import sys
input = sys.stdin.readline


def mergeSort(L):
    if len(L) == 1:
        return L
    
    mid = (len(L) + 1)//2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    
    L2 = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1
    
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1
        
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1
        
    return L2

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
mergeSort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1) 