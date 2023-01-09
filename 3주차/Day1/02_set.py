# set_test = {1,2,3,1,2}

# print(set_test)
# print(type(set_test))

my_list=['서울','서울','대전','광주','서울','대전','부산','부산']
my_list_2=[]

for i in my_list:
    if i not in my_list_2:
        my_list_2.append(i)
        
print(my_list_2)