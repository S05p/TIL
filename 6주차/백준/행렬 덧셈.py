
N, M = map(int,input().split())
matrix = []
matrix1 = []
matrix2 = []

for i in range(N):
    line = list(map(int,input().split()))
    matrix1.append(line)
    
for j in range(N):
    line = list(map(int,input().split()))
    matrix2.append(line)
    
for k in range(N):
    new_line = []
    for z in range(M):
        new_line.append(matrix1[k][z] + matrix2[k][z])
    matrix.append(new_line)

for q in range(N):
    print(*matrix[q])
        
