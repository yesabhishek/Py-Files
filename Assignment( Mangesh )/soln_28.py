matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,1,1],[1,1,1],[1,1,1]]
result =[[0,0,0], [0,0,0], [0,0,0]]
print(" Matrix 1: ")

for i in matrix1:
    print((i),end=' ')
    print("\n")

print(" Matrix 2: ")
for i in matrix2:
    print((i),end=' ')
    print("\n")


print(" After adding of two matrix: ")
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])): 
        result[i][j] = matrix1[i][j] + matrix2[i][j] 
  
for r in result: 
    print(r)
