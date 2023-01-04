# 실습1

n = int(input('정수를 입력하세요 : '))
if n>=0:
    print(n)
else:
    print(-n)

# 실습2

number_list = [1, 2, 3, 4, 5]
cnt = 0

for _ in number_list:
    cnt += 1

print(cnt)

# 실습3

number_list = [1,2,3,4,5]
number_list_sum = 0

for i in number_list:
    number_list_sum += i
    
print(number_list_sum)

# 실습4

number_list = [2,4,6]
cnt = 0
result = 0
for _ in number_list:
    cnt += 1

for i in number_list:
    result += i

print(result/cnt)
    
# 실습5

number_list=[1,2,3,4,5]
result = 1

for i in number_list:
    result = i*result

print(result)

# 실습6

number_list=[1,1,1]
maximof = 0

for i in number_list:
    if i>maximof:
        maximof = i
        
print(maximof)

# 실습7

number_list = [5,5,5,2]
minimerize = number_list[0]

for i in number_list:
    if i<minimerize:
        minimerize = i
        
print(minimerize)