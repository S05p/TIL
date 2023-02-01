import heapq

numbers = [0,12345678, 1, 2,0,0,0,0,32]

heap = []

for n in numbers:
    if n != 0:
        heapq.heappush(heap,n)
    else:
        print(heapq.heappop(heap))
        
        