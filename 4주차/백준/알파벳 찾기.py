s = str(input())

for i in range(97,123):
    try:
        print(s.index(chr(i)))
    except:
        print(-1)
    