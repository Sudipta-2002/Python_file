#list creating
a=[1,2,3,4,5,6]

#list print
print(a)

#access using index using
print(a[2])

#change the value of list
a[0]=19
print(a)
#we can creat list iteam from different type
# noinspection PyInterpreter
c=[1,2,"sudipta",0.2,True]
print(c[2])
print(c)

#list slicing
friend=["ram","sham","sudipta","gita","sudip",45,32]
print(friend[0:2])
print(friend[3:7])

#list function
L1=[7,2,9,3,5,1,8,2]
print(L1)
L1.sort()  #sorts the list
L1.reverse() #reverse the list
L1.append(45) #add data end of the list
L1.insert(2,23)  #insert 23 at 2 index
L1.pop(2) #pop data in index 2
L1.remove(5) #remove 5 from the list
L1.remove(45)
print(L1.count(2))
print(L1)
