##1

#mydic = {
#     "First":"sudipta",
#     "Second":"paul",
#     "Third":"gita"
# }
# print(mydic['First'])

##2

# l=[('sudipta',1),('sumit',2),('sujit',3)]
# mydic=dict(l)
# print(mydic)

##3

# mydic = {
#     "First":"sudipta",
#     "ASecond":"paul",
#     "Third":"sumit"
# }
# for key in sorted(mydic):
#     print(key , mydic[key])

##4

# mydic = {
#     "First":"mango",
#     "Second":"apple",
#     "Third":"orange"
# }
# mydic2 = {
#     "Fouth":"rose",
#     "Fifth":"lotus",
#     "Sixth":"sunflower"
# }
# mydic.update(mydic2)
# print(mydic)

##5

# mydic = {
#     "First":"mango",
#     "Second":"apple",
#     "Third":"orange"
# }
# l=[]
# l=list(mydic)
# print(l)
# key=input("enter the key:")
# flag=False
# for i in l:
#     if i==key:
#         flag=True
#         break
# if flag:
#     print("key is presnt in dictionary")
# else:
#     print("key is not presnt in dictionary")

##6

# mydic = {169: "sumit",
#      167: "sujit",
#      166: "sudipta",
#      159: "srinjoy",
#      154: "souvik_s",
#      150: "souvik_k",
#      162: "subhadip"
#      }
# l=[]
# l=list(mydic)
# print(l)
# sum=0
# for i in l:
#     sum+=i
# print(sum)

##8

# mydic = {169: "sumit",
#      167: "sujit",
#      166: "sudipta",
#      159: "srinjoy",
#      154: "souvik_s",
#      150: "souvik_k",
#      162: "subhadip"
#      }
# l=[]
# l=list(mydic)
# print(l)
# print("the max value is: ",max(l))
# print("the max value is: ",min(l))

##9

s = input()
d = {}
for i in range(len(s)):
    d.update({s[i]: s[-i-1]})
print(d)

##10

n = int(input("Enter the range:"))
d = {}
for i in range(1, n+1):
    d.update({i: i*i})
print(d)