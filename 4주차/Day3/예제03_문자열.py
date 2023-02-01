# 예제1 - 유학금지

n = str(input())

n_table = n.maketrans({
    'C' : '',
    'A' : '',
    'M' : '',
    'B' : '',
    'R' : '',
    'I' : '',
    'D' : '',
    'G' : '',
    'E' : '',
})

print(n.translate(n_table))

# 예제2 - 문자열 반복

T = int(input())

for i in range(T):
    N = str(input())
    N_0 = N[0]
    result = ''
    for j in range(len(N)-2):
        result += int(N_0)*N[j+2]
    
    print(result)  

# 예제3 - 팰린드롬인지 확인하기

n = str(input())

if n[::-1] == n:
    print(1)
else:
    print(0)

# 예제4 - 태보태보 총난타

n = str(input())

left_jap = n.index(('(^0^)'))
right_jap = left_jap + 4

left_jap_count = n[:left_jap].count('@')
right_jap_count = n[right_jap:].count('@')

print(left_jap_count, right_jap_count)

# 예제5 - 크로아티아 알파벳

n = str(input())

n = n.replace('c=','1')
n = n.replace('c-','2')
n =n.replace('dz=','3')
n =n.replace('d-','4')
n =n.replace('lj','5')
n =n.replace('nj','6')
n =n.replace('s=','7')
n =n.replace('z=','8')

print(len(n))

# 예제6 - 알파벳 찾기

S = str(input())
S_list = []

for i in range(97,123):
    if chr(i) in S:
        S_list.append(S.index(chr(i)))
    else:
        S_list.append(-1)
            
            
print(*S_list)