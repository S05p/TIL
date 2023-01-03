#1번 
n = int((input('점수를 입력해주세요 : ')))

if n >0:
    print(True)
else:
    print(False)
    
#2번
message = ' 번째 정수를 입력하세요 :'

a = int(input(f'첫{message}'))
b = int(input(f'두{message}'))

if a>b:
    print(a)
elif a<b:
    print(b)
else:
    print(False)

#3번
n = int(input('점수를 입력하세요 : '))

if 1<n<10:
    print(True)
else:
    print(False)

#4번
n = int(input('점수를 입력하세요 :'))

if n>0 and n%2==0:
    print(True)
else:
    print(False)

#5번
score = int(input('정수를 입력하세요 :'))

if (score>100) or (score<0):
    print('에러')
elif score>=60:
    print('합격')
else:
    print('불합격')

#6번
sen = str(input('문자열을 입력하세요 :'))
reversed_sen = sen[::-1]

for char in reversed_sen:
    print(char)
        
#7번
a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))

if a==b:
    print(False)
else:
    n = max(a,b) - min(a,b)
    z = min(a,b)
    for _ in range(n-1):
        z += 1
        print(z)

#8번
a = int(input('첫 번째 정수를 입력하세요 : '))
b = int(input('두 번째 정수를 입력하세요 : '))

if a==b:
    print(False)
else:
    n = max(a,b) - min(a,b)
    z = max(a,b)
    for _ in range(n-1):
        z -= 1
        print(z, end=' ')

#9번
n = int(input('정수를 입력하세요 :'))

a = -1

if n<1:
    print(False)
elif n>=1:
    for _ in range(0,n//2):
        a += 2
        print(a)

#10번
for i in range(2,10):
    for j in range(2,10):
        print(f'{i} X {j} = {i*j}')