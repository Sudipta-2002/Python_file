'''
#Q1
mydic={
    "pankha": "pakha",
    "dabba": "box",
    "vastu": "iteam"
}
print("option are: ", mydic.keys())
a=input("enter the hindi word in dictinorat:")
print(mydic[a])

#Q2
num1=int(input("enter the number 1: \n"))
num2=int(input("enter the number 2: \n"))
num3=int(input("enter the number 3: \n"))
num4=int(input("enter the number 4: \n"))
num5=int(input("enter the number 5: \n"))
num6=int(input("enter the number 6: \n"))
num7=int(input("enter the number 7: \n"))

s={num1,num2,num3,num4,num5,num6,num7}
print(s)

#Q3
s={18,"18"}
print(s)

#Q4
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

#Q5
s={}
print(type(s))  '''

#Q6
s={1,2,3,4,"sp",(1,2)}
print(s)