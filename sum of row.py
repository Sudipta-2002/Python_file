
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
mat=[]
for i in range(m):
    row=[]
    for j in range(n):
        inp=int(input("enter the matrix element m[i][j]:"))
        row.append(inp)
    mat.append(row)
print(mat)
mat2=[]

for i in range(m):
    row=[]
    a=0
    for j in range(n):

        a=a+mat[i][j]
        #row.append(a)
    mat2.append(a)
    print("row",i ,"=",mat2[i])
#print(mat2)
