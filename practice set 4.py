#Q1
l1=input("enter the fruit name: ")
l2=input("enter the fruit name: ")
l3=input("enter the fruit name: ")
l4=input("enter the fruit name: ")
l5=input("enter the fruit name: ")
list=[l1,l2,l3,l4,l5]
print(list)


#Q2
s1=input("enter the marks: ")
s2=input("enter the marks: ")
s3=input("enter the marks: ")
s4=input("enter the marks: ")
s5=input("enter the marks: ")
s6=input("enter the marks: ")
marks=[s1,s2,s3,s4,s5,s6]
marks.sort()
print(marks);


#Q3
a=(1,2,3,4,5)
print(a)
#a[2]=6  tupple cannot change in python
#print(a)


#Q4
l=[1,2,3,4,5,6]
print(l)
sum=l[0]+l[1]+l[2]+l[3]
print("sum of four number in the list is: ",sum)


#Q5
t=(7,0,8,0,0,9)
print(t.count(0))
print(t.index(8))