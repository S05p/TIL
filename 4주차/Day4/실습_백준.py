# 실습1 - 홉수

n_1 = []

for i in range(7):
    n = int(input())
    n_1.append(n)

n_1_odd = []
    
for j in n_1:
    if j % 2 == 1:
        n_1_odd.append(j)
        
if len(n_1_odd) == 0:
    print(-1)
else:
    print(sum(n_1_odd))
    print(min(n_1_odd))
    
# 실습2 - 더하기

n_2 = list(map(int,input().split(',')))

print(sum(n_2))

# 실습3 - 학점계산

score_dict = {
    'A+' : 4.3,
    'A0' : 4.0,
    'A-' : 3.7,
    'B+' : 3.3,
    'B0' : 3.0,
    'B-' : 2.7,
    'C+' : 2.3,
    'C0' : 2.0,
    'C-' : 1.7,
    'D+' : 1.3,
    'D0' : 1.0,
    'D-' : 0.7,
    'F' : 0.0,    
}

n_3 = str(input())

print(score_dict[n_3])

# 실습4 - 다이얼

n_4 = str(input())
cnt = 0

for j in n_4:
    if 65 <= ord(j) <= 67:
        cnt += 1
    elif 68 <= ord(j) <= 70:
        cnt += 2
    elif 71 <= ord(j) <= 73:
        cnt += 3
    elif 74 <= ord(j) <= 76:
        cnt += 4
    elif 77 <= ord(j) <= 79:
        cnt += 5
    elif 80 <= ord(j) <= 83:
        cnt += 6
    elif 84 <= ord(j) <= 86:
        cnt += 7
    elif 87 <= ord(j) <= 90:
        cnt += 8
        
print(cnt + len(n_4)*2)

# 실습5 - 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

a_b_c = str(a*b*c)

for i in range(10):
    cnt = a_b_c.count(str(i))
    print(cnt)        

# 실습6 - 회사에 있는 사람

n = int(input())
att = {}

for _ in range(n):
    a, b = map(str,input().split())
    if a in att.keys():
        att[a] = b
    else:
        att[a] = b
        
att_att = []

for key, values in att.items():
    if values == 'enter':
        att_att.append(key)

att_att.sort(reverse=True)

print(*att_att,sep='\n')