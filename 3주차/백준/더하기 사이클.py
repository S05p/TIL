n = int(input())
cnt = 0
n_cycle = n

while True:
    n_cycle = (n_cycle%10)*10 + (((n_cycle//10) + (n_cycle%10))%10)
    cnt+=1
    if n_cycle == n:
        break;
    
    
print(cnt)