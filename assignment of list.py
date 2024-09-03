'''
Q1>

n=int(input("enter the range:"))
l=[]
for i in range(n):
    a=int(input("enter the data:"))
    l.append(a)
l.reverse()
print(l)

Q2>

n=int(input("enter the range:"))
l=[]
for i in range(n):
    a=int(input("enter the data:"))
    l.append(a)
for i in range(n-1,-1,-1):
    print(l[i])

Q3>

n=int(input("enter the range:"))
l=[]
for i in range(n):
    a=int(input("enter the data:"))
    l.append(a)
max=0
for i in range(n):
    if max<l[i]:
        max=l[i]
print("the greatest value of list is:",max)

Q4>

n=int(input("enter the range:"))
l=[]
for i in range(n):
    a=int(input("enter the data:"))
    l.append(a)
l.insert(0,l[n-1])
l.pop()
print(l)

Q5>

s = input("Enter string: ")
st = input("Enter substring: ")
n = len(st)
m = len(s)
res = ""

for i in range(0, m-n):
    temp = s[i:i+n]
    if temp == st:
        res = s[:i] + s[i+n:]
        break

print(res)

Q6>

s=input("enter the date (mm/dd/yy) this format:")
l = ["", "January", "February", "March",
     "April", "May", "June", "July",
     "August", "September", "October",
     "November", "December"]
print("the date is:")
month=s[:2]
month=int(month)
print(l[month] ,s[3:5] ,s[6:10])

Q7>

s=input("enter the sentence:")
print(s.title())   '''

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
    a=0
    for j in range(n):

        a=a+mat[i][j]
        #row.append(a)
    mat2.append(a)
    print("row",i ,"=",mat2[i])




