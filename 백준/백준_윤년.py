n = int(input())

if n%4==0:
    n_1=n
    if n_1%400==0:
        print(1)
    elif n_1%100==0:
        print(0)
    else:
        print(1)
else:
    print(0)