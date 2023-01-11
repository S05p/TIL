# 문제번호 2047 신문 헤드라인

n= str(input())

print(n.upper())

# 문제번호 2025 N줄 덧셈

n=int(input())
total = 0

for i in range(n+1):
    total+=i
print(total)

# 문제번호 1936 1대1 가위바위보

a,b = map(int,input().split())

if a+b==4:
    if a==1 and b==3:
        print('A')
    else:
        print('B')
        
if a+b!=4:
    if a>b:
        print('A')
    else:
        print('B')

# 문제번호 2027 대각선 출력하기

print('''#++++
+#+++
++#++
+++#+
++++#''')

# 문제번호 2058 자릿수 더하기

n = str(input())
total = 0

for i in n:
    total += int(i)
    
print(total)

# 문제번호 2019 더블더블

n = int(input())
n_list = []

for i in range(0,n+1):
    n_list.append(2**i)
    
print(*n_list)