# import heapq
# from heapq import heappop
# import sys

# N = int(sys.stdin.readline())
# heap = []

# for _ in range(N):
#     heapq.heappush(heap,int(sys.stdin.readline()))
    
# for _ in range(N):
#     print(heappop(heap))
    
# 야발.. 이것도 메모리 초과면 나는 뭘 할수가 없는데?

import sys

n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data] += 1

for i in range(10001):
    if array[i] != 0:
        for j in range(array[i]):
            print(i)
            
# 시간이 넉넉하고 메모리는 제한된 문제였다.
# 메모리는 함수를 많이 쓰면 올라가는듯? ex.append
# 그래서 처음부터 순회를하고
# 리스트의 위치를 지정하여 올리는 방식으로 한 것 같다. << 이 방식이 메모리를 덜 잡아먹는듯?
