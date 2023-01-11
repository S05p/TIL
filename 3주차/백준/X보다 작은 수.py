N, X = map(int,input().split())
test_list = list(map(int,input().split()))
test_list_2 = []

for i in test_list:
    if i<X:
        test_list_2.append(i)
        
print(*test_list_2)