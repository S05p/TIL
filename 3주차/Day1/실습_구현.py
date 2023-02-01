# 문제 1

n = str(input('문자열을 입력하세요 > '))
cnt = 0

if 'e' not in n:
    cnt = -1
else:
    for i in n:
        if i != 'e':
            cnt +=1
        else:
            break;
        
print(cnt)

# 문제 2

n = list(map(str,input().split()))
n_dic = {}

for i in n:
    if i not in n_dic:
        n_dic[i] = 1
    else:
        n_dic[i] += 1

for k,v in n_dic.items():
    print(k,v)

# 문제 3

n = str(input())

for char in n:
    if char != 'e':
        print(char,end='')

# # print(n.replace('e',''))

# 문제 4

a, b = map(str,input().split())
cnt = 0

for char in a:
    if char == b:
        cnt += 1

print(cnt)

# print(a.count(b))

# 문제 5

a, b, c= map(int,input('문자열을 입력하세요 >').split())

print('0',a,'-',b,'-',c,sep='')

# list_0 = [str(a),str(b),str(c)]
# list_0_join = '-'.join(list_0)

# print(list_0_join)

# 문제 6

n = int(input('문자열을 입력하세요 >'))
total = 0

if n>0:
    while n//10 != 0:
            total += n%10
            n = n//10
        
total += n%10
if n>0:
    print(total)
else:
    print(-1)

