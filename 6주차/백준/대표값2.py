n = []

for _ in range(5):
    n.append(int(input()))
    
print(int(sum(n)/len(n)))
n = sorted(n)
print(n[2])