
#Q1
name=input("enter the name : ")
print("good afternoon "+name)


#Q2
letter='''dear <name>
         you are selected
         <date>'''
name=input("enter the name:")
date=input("enter the date:")
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter) 


#Q3
str = "she is girl  name is rupu"
print(str.find("  "))


#Q4
str = "she is girl  name is rupu"
str=str.replace("  "," ")
print(str)


#Q5
letter2="Dear Harry,  This Python course is nice.  Thanks"
letter_format="Dear Harry,\tThis Python course is nice.\tThanks"
print(letter_format)