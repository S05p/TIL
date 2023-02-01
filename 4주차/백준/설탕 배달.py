N = int(input())

if N%5 ==0:
    print(N//5)
elif (N-3)%5 ==0:
    if N == 3:
        print(1)
    else:
        print(((N-3)//5) + 1)
elif (N-6)%5 ==0:
    if N == 6:
        print(2)
    else:
        print(((N-6)//5) + 2)
elif (N-9)%5 ==0:
    if N == 9:
        print(3)
    elif N ==4:
        print(-1)
    else:
        print(((N-9)//5) + 3)
elif (N-12)%5 ==0:
    if N == 12:
        print(4)
    elif N == 7:
        print(-1)
    else:
        print(((N-12)//5) + 4)
elif (N%3) == 0:
    print(N//3)
else:
    print(-1)