m=int(input("Enter the size of m:"))
n=int(input("Enter the size of n:"))
mat1=[]
for i in range(m):
    row=[]
    for j in range(n):
        inp=int(input("ente the matrix1  input mat1[{i}][{j}]:"))
        row.append(inp)
    mat1.append(row)
print("The matrix1 :")
print(mat1)
mat2=[]
for i in range(m):
    row=[]
    for j in range(n):
        inp=int(input("ente the matrix2 input mat2[{i}][{j}]:"))
        row.append(inp)
    mat2.append(row)
print("The matrix2 :")
print(mat2)

mat3=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(mat1[i][j] + mat2[i][j])
    mat3.append(row)

print("Result:")
print(mat3)