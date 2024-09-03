#filter function

# x=list(input("enter the element:").split())    #multiple element add in list without for loop
# print(x)
# def even(a):
#     return int(a)%2==0
# p=list(filter(even,x))    #filter function take one element from the list simultaneously function call
# print(p)


#lambda function

# x=list(input("enter the element").split())
# even=lambda data: int(data)%2==0      #lambda function no return statement
# p=list(filter(even,x))
# print(p)


#map function
x=list(input("enter the data:").split())
print(x)
even=lambda data:int(data)%2==0
to_pow=lambda data:int(data)**2
p=list(filter(even,x))
print(p)
q=list(map(to_pow,p))   #map or edit the list of b using map function
print(q)
