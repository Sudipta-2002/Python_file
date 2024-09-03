a=[1,2]
b=[3,4]
c=[5,6]
d=[7,8]
l=[]
l1=[]
l.append(a)
l.append(b)
print(l)
l1.append(c)
l1.append(d)
print(l1)
print(len(l))
print(len(l1))
for i in range(len(l)):
    row=[]
    for j in range(len(l[0])):
        #row.append(l[i][j]+ l1[i][j])
        print(l[i]+ l1[j])
        #-print(row)

