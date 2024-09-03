'''
def sum(a,b):
    return a+b
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
s=sum(a,b)
print("sum= ",s)

def greet(name):
    print("good day "+name)
name= "sudipta"
greet(name)  '''

#default parameter value

def greet(name="gitashree"):
    print("hello "+name)

greet("sudipta")
greet()

# #recursion
# def fact_recursive(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n * fact_recursive(n-1)
# f= fact_recursive(5)
# print(f)