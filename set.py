a={1,2,3,4,5}
print(type(a))
b={1,2,3,'sudipta','gita',7} #that is also same as first one
print(type(b))
print(a)

b= set()  #empty set
print(type(b))
b.add(4)   #add the data in the set
b.add(1)
print(b)
print(type(b))
print(list(b)) #typecasting
b.add((2,2,7,8)) #tuple add to the sets
# b.add([1,2,3,4,5,6])  #cannot add list or dictonnary to sets
print(b)
b.add(7)
b.add(8)
b.add(9)
print(b)
b.remove((2,2,7,8))  #remove element from the set
b.remove(9)
print(b)
print(len(b))   #calculate length of the set
print(b.pop())   #pop the first element in the set
print(b)
c={5,6,7}
print(c)
c.pop()
print(c)
#print(b.union(c))  #union of b & c set
#@print(b.intersection(c))  #intersection of b & c set
#c.remove(7)
#print(c)
d=b.union(c)
print(d)


s=set()   #creating set with user element
n=int(input())
for i in range(n):
    a=int(input())
    s.add(a)
print(s)



