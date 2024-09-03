#------->class and object creat<--------

# class Employee:
#     company="google"  #class atribute
# obj=Employee()     #creat object
# print(obj.company)
# Employee.company="youtube"   #change class atribute
# print(obj.company)


# class employee:
#     company="google"     #class atribute
#     salary="100000"
# sudipta=employee()
# gita=employee()
# sudipta.salary=1000000    #instence atribute
# gita.salary=200000
# print(f"sudipta salary= {sudipta.salary}")  ##f means using f sting eg.print(f"salary:{sudipta.salary}')
# print(f"gita salary= {gita.salary}")


# class  Number:          #class name can be pascale case
#     def sum(self):      #function name name can be camelcase
#         return self.a+self.b
# num=Number()
# num.a=10
# num.b=20
# s=num.sum()
# print(s)


#---->input data and print the data<------
# class railway:
#     type="RailwayForm"
#     def printdata(self):
#         print("Name= ",self.name)
#         print("Train= ",self.train)
#         print("Formtype= ",self.type)
#
# obj=railway()
# #obj.name="sudipta"
# obj.name=input("enter the passenger name= ")
# obj.train=input("enter the train name= ")
# #print(obj.type)
# obj.printdata()


#------>change class atribute & instance atribute print<------
# class sum:
#     number=30    ###preference instance atribute over class atribute
# a=sum()
# b=sum()
# #a.number=int(input("enter the first number:"))
# b.number=int(input("enetr the second number"))
# print(a.number)  #print class atribute
# print(b.number)  #print instance atribute



#------>addition two number in the class<-------
# class sum:
#     def add(self):
#         return self.a+self.b
# num=sum()
# num.a=int(input("enter the first number:"))
# num.b=int(input("enetr the second number"))
# s=num.add()
# print(s)

#----->why use self in function<-----
# class sum:
#     def add(self):    ## self catch the parameter of num & self accept own data
#         return self.a+self.b
# num=sum()
# num.a=5
# num.b=5
# s=num.add()   ##num.add() means sum.add(num)
# print(s)


#---->>>instance artribute<<<----
# class employe:
#     company="google"
# sudipta=employe()
# gita=employe()
# sudipta.salary=200
# gita.salary=400
# print(sudipta.company)
# print(sudipta.salary)
# print(gita.company)
# print(gita.salary)

#---->function static method<------
# class employe:
#     def greet(self):  #greet is static method
#         print("Good morning")
# sudipta=employe()
# sudipta.greet() ##that means eg. employe.greet()
#
#
# class employe:
#     def greet(self,s): #s is accept "thanks"
#         print("Good morning \n",s)
# sudipta=employe()
# sudipta.greet("thanks") #pass the parameter


#------>constructor<-------
# class a:
#     # init function is special type of function that is work without call
#     # it is called constructor
#     # init function is initialize with the object
#     def __init__(self):
#         print("class is created")
# obj=a()


#---->consturctor<------
# class a:
#     def __init__(self,name,salary,company):
#         self.name=name
#         self.salary=salary
#         self.company=company
#     def getdetails(self):
#         print(f"Name:{self.name}")
#         print(f"Salary:{self.salary}")
#         print(f"Company:{self.company}")
# obj=a("sudipta",100000,"youtube")
# obj.getdetails()


#------->inheritence<---------
# class parent:
#     company="google"
#     def putdetails(self):
#         print("i am child parent class")
# class child(parent):
#     def getdetails(self):
#         print("i am child class")
# p=parent()
# p.putdetails()
# c=child()
# c.getdetails()
# print(c.company)   #inherit class atribute because child class dont have class atribute


#----->function override<------
# class parent:
#     company="google"
#     def getdetails(self):    #$over ride condition beacuse two class name is aame
#         print("i am child parent class")
# class child(parent):
#     def getdetails(self):
#         print("i am child class")
# p=parent()
# p.getdetails()
# c=child()
# c.getdetails()
# print(c.company)   #inherit class atribute because child class dont have class atribute

#------>single inheritence<-------
##Defination:when child class inherit only one parent class it is called single inheritence.

#class parent:
#     company="google"
#     def putdetails(self):
#         print("i am child parent class")
# class child(parent):
#     def getdetails(self):
#         print("i am child class")
# p=parent()
# p.getdetails()
# c=child()
# c.getdetails()
# print(c.company)


#------->multiple inheritence<---------
##Defination:when child class inherit two parent class it is called multiple inheritence

class employe:
    company="visa"
    eode=120
class freelancer:
    company="nikon"
class programmer(employe,freelancer):
    name="sudipta"
    level=1
