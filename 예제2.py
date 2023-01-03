# a = 1
# b = 1
# print(a<b) # False
print('==================')
# a = bool('')
# b = False
# print(a == b) # False
print('==================')
# a = 1
# result = ''
# if a==1:
#     result = True
# else:
#     result = False
    
# print(result) # True
print('==================')
# a = 90

# if a == 90:
#     a = a + 10
    
# elif a == 100:
#     a= a + 10
    
# elif a == 110:
#     a = a + 10
# else:
#     a = a + 10
    
# a = a + 10

# print(a) # 110
print('==================')
# string = "hello world!"

# for element in string:
#     print(element)
    
# # h e l o w r d

# for문이 반복이고, element가 요소를 꺼낸다고 생각해서 중복되는 문자가 안 나오지 않을까 생각했습니다.
# 그러나 element는 dictionary형이 아닌 list형입니다. 모든 자료는 중복되서 나올수 있습니다.
# 게다가 for문이 반복이기 때문에 한 문자 이후로 줄바꿈을 할 것입니다.
print('==================')
# list_variable = [0, 1, 2, 3, 4, 5, 6]

# for element in list_variable:
#     print(element, end ="")
    
# # 0123456

print('==================')

# n = 10

# for element in range(-n,n):
#     print(element, end = " ")
    
# # -10 -9 -8 .... 9

print('==================')

# list_variable = [6, 5, 4, 3, 2, 1, 0]

# for index, element in enumerate(list_variable):
#     print(index,element)
    
# # 0, '6'
# # 1, '5'
# # 2, '4'
# # ...
# # 6, '0'

# print('==================')

# n = 10
# for element in range(n,-n,-1):
#     print(element,end=' ')
#     if n <0:
#         break
    
# 10 9 8 7 6 5 4 3 2 1 0
# if 문이 더 위에 있어야지 break 가 작동합니다.

print('==================')

# list_variable = [-1, 3, 5, -2, 1, 9, 21, -3, -5]

# for element in list_variable:
#     if element < 0:
#         continue
    
#     print(element, end=" ")
    
# # 3 5 1 9 21

print('==================')

# N = 3
# M = 4

# for n in range(N):
#     for m in range(M):
#         print(f"{n}, {m}")
        
# # 0, 0
# # 0, 1
# # 0, 2
# # 0, 3
# # 1, 0
# # ...
# # 2, 3