matrix = []

for _ in range(9):
    line = list(map(int,input().split()))
    matrix.append(line)
    
mm = max(matrix[0])

for i in range(9):
    if max(matrix[i]) >= mm:
        need = i+1
        need_line = matrix[i]
        mm = max(matrix[i])
        need_2 = need_line.index(mm)
        
print(mm)
print(need, need_2 +1)