# members = [
#     'jay', 'jay','jay','jay','jay', 'john','john','john','john',]

# count = {}

# for member in members:
#     if member not in count:
#         count[member] = count.get(member,1)
#     else:
#         count[member] += 1
    
# print(count)

# from collections import Counter
# new_count_itmes = Counter(members)
# print(new_count_itmes)
# print(new_count_itmes.most_common())

n = int(input())
att = {}

att['a'] = 'b'

print(att.get('c',1))