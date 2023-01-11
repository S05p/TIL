C = int(input())

for i in range(C):
    test_list = list(map(int,input().split()))
    test_aver = (sum(test_list[1:])/test_list[0])
    for j in test_list[1:]:
        