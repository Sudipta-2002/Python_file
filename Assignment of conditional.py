'''
Q1>

high=2700
low=1500
for i in range(low,high+1):
    if i%5==0 and i%7==0:
        print(i)

Q2>

def to_celcius(f):
    return 5/9*(f-32)
def to_fahrenheit(c):
    return (5/9*c)+32
inp=float(input("enetr the temperature celcius or fahrenheit:"))
print("press 1 to fahrenheit")
print("press 0 to celcius")
choice=int(input())
if choice==0:
    print(to_celcius(inp))
elif choice==1:
    print(to_fahrenheit(inp))
else:
    print("wrong choice")

Q3>

s=input("Enter the string: ")
dupstr=""
for i in s:
    dupstr=i + dupstr
print(dupstr)

Q4>

l=[]
count=0
count1=0
r=int(input("enter the range: "))
for i in range(r):
    inp=int(input("enter the list element"))
    l.append(inp)
print(l)
for i in range(r):
    if l[i]%2==0:
        count+=1
    else:
        count1+=1
print("Total even number= ",count)
print("Total odd number= ",count1)

Q5>

for i in range(1,6):
    if i==3:
        continue
    elif i==6:
        continue
    print(i)

Q6>

a=0
b=1
print("the fibonaaci series:")
print(a)
print(b)
c=a+b
while c<50:
    print(c)
    a = b
    b = c
    c = a + b

Q7>

for i in range(1,50):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%5==0:
        print("buzz")
    elif i%3==0:
        print("fizz")

Q9>

digit=0
letter=0
s=input("enter the string:")
for i in s:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        letter+=1
print("Total number of digit= ",digit)
print("Total number of letter= ", letter)

Q10>

import math

for i in range(100,401):
    ec=0   #ec=even counter
    j=i
    while j>0:
        rem=j%10
        if rem%2==0:
           ec+=1
        j=math.floor(j/10)
    if(ec==3):
        print("even numbe and shuld be each digit is even= ",i)

Q11>

age=float(input("enter the age:"))
def dogage(age):
    res=0
    if age<2:
       res=age*5.25
    else:
        res=2*5.25
        res+=(age-2)*4
        return res
totalage=dogage(age)
print("dogs year= ",totalage)

Q12>

vl=['a','e','i','o','u']
alpha=input("enetr the alphabet:")
for i in range(5):
    if alpha==vl[i]:
        print("it is vowel")
        break
else :
        print("it is consonant")


Q13>
dict = {"January": "31",
        "February": "28",
        "March": "31",
        "April": "30",
        "May": "31",
        "June": "30",
        "July": "31",
        "August": "30",
        "September": "31",
        "October": "30",
        "November": "31",
        "December": "30"
        }
month=input("enetr the month name:")
print("total number of day this month:",dict.gat(month))

Q14>

a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
sum=a+b
if sum>15 and sum<20:
    print("20")
else:
    print(sum)

Q15>

s=input("enter the string:")
print(s.isalnum())

Q16>

a=int(input("entert riangle first edge:"))
b=int(input("enter triangle second edge:"))
c=int(input("enter triangle third edge:"))
if a==b and a==c:
    print("the triangle is equilateral")
elif a!=b!=c:
    print("the triangle is scalene")
else:
    print("the triangle is isosceles")

Q18>

a=int(input("entert first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
l=[]
l.append(a)
l.append(b)
l.append(c)
l.sort()
print("the mid value is=",l[1])

Q19>

n=int(input("enter the range:"))
result=0
average=0
for i in range(1,n):
    result+=i
average=result/n
print("sum of nth number= ",result)
print("average of nth number= ",average)

Q20>

for i in range(1, 11):
    for j in range(1, 11):
        print(str(i) +" x "+ str(j) +"="+str(i*j))
    print()  '''






















