N = int(input())

total = []

for _ in range(N):
    a, b = map(int,input().split())
    x = a
    for i in range(10):
        x += 1
        y = b
        for j in range(10):
            y += 1
            xy_list = [[x-1,y-1],[x,y]]
            if xy_list not in total:
                total.append(xy_list)
            
print(len(total))
    