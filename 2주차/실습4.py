# # 문제1

# n = str(input('문자열을 입력하세요 : '))
# cnt=0

# for i in n:
#     if i == 'e':
#         cnt += 1
# print(cnt)

# # 문제2

# n = str(input('문자열을 입력하세요 : '))
# cnt = 0

# for z in n:
#     if z in ('a','e','i','o','u','A','E','I','O','U'):
#         cnt += 1
        
# print(cnt)

# # 문제3

# dict_variable = {
#     '이름':'정우영',
#     '생년':'2000',
#     '회사':'하이퍼그로스'
# }

# dict_variable['나이'] = '24세'

# print(dict_variable)

# # 문제4

# dict_variable ={}

# n = str(input('이름을 입력하세요 :'))
# t = str(input('전화번호를 입력하세요 : '))
# s = str(input('거주지를 입력하세요 : '))

# dict_variable['이름'] = n
# dict_variable['전화번호'] = t
# dict_variable['거주지'] = s

# print(dict_variable)
# for key in dict_variable:
#     print(key,':',dict_variable[key])

# # 문제5

# dict_variable={}

# n = str(input('이름을 입력하세요 :'))
# t = str(input('전화번호를 입력하세요 : '))
# e = str(input('이메일을 입력하세요 : '))
# s = str(input('거주지를 입력하세요 : '))

# dict_variable_정우영 = {}

# dict_variable_정우영['전화번호'] = t
# dict_variable_정우영['이메일'] = e
# dict_variable_정우영['거주지'] = s

# dict_variable[n] = dict_variable_정우영

# print(dict_variable)

# 문제6

sentence = input("문자열을 입력하세요 > ")
dictionary = {}

for i in range(0,len(sentence)):
    if sentence[i] not in dictionary.keys():
        dictionary[sentence[i]] = 1
    else:
        dictionary[sentence[i]] += 1

for i, j in dictionary.items():
    print("{} {}".format(i, j))