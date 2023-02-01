# 문제1

n_1 = int(input('# 정수를 출력하세요.'))
print(n_1)

# 문제2

n_2 = map(str,input('# 단어를 구분해서 출력하세요. ').split())
print(*n_2)

# 문제3

n_3 = int(input('# 테스트 케이스마다 입력 값을 그대로 출력하세요. '))

for i in range(n_3):
    n_3_0 = int(input())
    print(n_3_0)
    
# 문제4

n_4 = list(map(int,input('# 2개 이상의 정수를 출력하세요.').split()))

print(*n_4)

# 문제5

a_5, b_5 = map(int,input().split())

print(a_5,b_5)

# 문제6

n_6 = map(str,input('# 단어를 구분해서 출력하세요.').split())

print(*n_6)

# 문제7

n_7 = int(input('# 테스트 케이스 수'))

for _ in range(n_7):
    n_7_0 = list(map(int,input().split()))
    print(*n_7_0)
    
# 문제8

n_8 = int(input('# 테스트 케이스 수'))

for _ in range(n_8):
    n_8_0 = list(map(int,input().split()))
    print(*n_8_0)