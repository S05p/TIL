n = str(input())
cnt = 0

for i in n:
    if i == 1:
        cnt += 0
    elif 65<=ord(i)<=67:
        cnt += 1
    elif 68<=ord(i)<=70:
        cnt += 2
    elif 71<=ord(i)<=73:
        cnt += 3
    elif 74<=ord(i)<=76:
        cnt += 4
    elif 77<=ord(i)<=79:
        cnt += 5
    elif 80<=ord(i)<=83:
        cnt += 6
    elif 84<=ord(i)<=86:
        cnt += 7
    elif 87<=ord(i)<=90:
        cnt += 8

print(cnt+len(n)*2)
        