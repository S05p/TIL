N = int((input()))
N_ = 1

if N == 0:
    N_1 = 1
else:
    for i in range(1,N+1):
        N_ *= i

print(N_)