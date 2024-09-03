##1> cheack sequence number is different to each other

# def test(data):
#     if len(data)==len(set(data)):
#         print("True")
#     else:
#         print("False")
# data=list(input("enter the number:"))
# print(test(data))



##2> all possible string using vowel(possible means permunation)

# from itertools import permutations
# char_list=['a','e','i','o','u']
# comb=permutations(char_list)
# for i in comb:
#     print(i)



##3> remove and print every third number in list

# l=list(input("enter the list element"))
# index=2
# for i in range(len(l)):
#     print(str(i)+"ietaration deleteing element = "+l.pop(index))
#     if i==len(l):
#         breaK



##4> all possible string using 3 digit

# from itertools import permutations
# l=list(input("enter the digit:"))
# comb=permutations(l)
# for i in comb:
#     print(i)

      #another process

# def comb(l):
#     for i in range(3):
#         for j in range (3):
#             for k in range(3):
#                 if (i!=j and j!=k and i!=k):
#                     print(l[i],l[j],l[k])
# l=list(input("enter the 3 digit:"))
# comb(l)



##5> check the value present in list

# l=[1,2,3,4,5,6,7,8,9,10]
# value=int(input("enter the value: "))
# for i in l:
#     if i==value:
#         print("Value is presnt in list")
#         break
# else:
#         print("Value is not present in list")



##7> sum of two number between 15-20 print 15

# a=int(input("enetr the first number:"))
# b=int(input("enetr the second number:"))
# c=a+b
# if c>=15 and c<=20:
#     print("20")
# else:
#     print(c)



##6> find the list even number when list occure 237 then stop

# l=[386,342,47,418,907,344,236,823,345,237,742,717,956,
#     958,743,527]
# for i in l:
#      if i==237:
#         break
#      if i%2==0:
#         print(i)




