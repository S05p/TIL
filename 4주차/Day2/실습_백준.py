# 실습1

n = int(input())

for _ in range(n):
    n_case = int(input())
    n_list = list(map(int,input().split()))
    print(sum(n_list))

# 실습2

a, b, c, d = map(str,input().split())

ab_int = int(a+b)
cd_int = int(c+d)

print(ab_int+cd_int)

# 실습3

x_axis = []
y_axis = []

for i in range(3):
    a,b = map(int,input().split())
    x_axis.append(a)
    y_axis.append(b)
    
for j in x_axis:
    if x_axis.count(j) == 1:
        jump_x = j
        
for q in y_axis:
    if y_axis.count(q) == 1:
        jump_y = q

print(jump_x,jump_y)

# 실습4

a = None
b = None

while a != 0 or b != 0:
    a,b = map(int,input().split())
    if a==0 and b==0:
        break
    print(a+b)


# 실습5

n = int(input())
k = n
n = (n%10)*10 + (((n//10)+(n%10))%10)
cnt = 1

while n!=k:
    n = (n%10)*10 + (((n//10)+(n%10))%10)
    cnt += 1
    
    
print(cnt)