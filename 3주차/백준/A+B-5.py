A,B = None, None

while A!=0 or B!=0:
    A,B=map(int,input().split())
    if A == 0 or B == 0:
        break;
    print(A+B)