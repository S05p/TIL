# # 박스가 내려와

# grid = [
#     [0, 0],
#     [1, 1],
#     [1, 0],
#     [0, 1],
#     [1, 0],    
# ]

# m = 5
# n = 2

# move_dis = 0

# for x in range(n):
#     for y in reversed(range(m)):
#         if grid[y][x] == 1:
#             while True:
                
#                 if y+1 >= m:
#                     break
                
#                 if grid[y+1][x] == 1:
#                     break
                
#                 grid[y][x] = 0
#                 grid[y+1][x] = 1
                
#                 y += 1
                
#                 move_dis += 1
                
                
# import pprint

# pprint.pprint(grid)

'++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'

# 누울자리를 찾아라

# . 이 나왔을때 빈 공간수를 +1하고
# x가 나왔을대 빈 공간수를 카운트
# 또는 끝까지 순회했을때 빈 공간수를 카운트하는 방식...
# 생각보다 쉽군
        