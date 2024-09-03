mydic = {
    "First":"sudipta",
    "Second":"paul",
    "Third":"gita"
}

print(mydic['First'])
print(mydic['Second'])
mydic["Third"]="paul"
print(mydic["Third"])

#update dictonary
updatedict={
    "friend":"sujoy"
}
mydic.update(updatedict)
print(mydic)
print(list(mydic))
#nested dictonary

mydic2 = {
    "First":"sudipta",
    "Second":"paul",
    "Third":"gita",
    "anotherdict": {"gita":"ghosh",
                "sudip":"biswas"},
    1:2
}
print(mydic2)
print(mydic2['anotherdict'])
print(mydic2["anotherdict"]["gita"]) #print nested dictonary value
print(list(mydic2))  #typecasting dict to list
print(list(mydic2.values()))  #list of the dictonary values
print(mydic2['anotherdict'].values())  #print nested dictonary key values
print(list(mydic2)) #print list of dictonary key
print(mydic2.items()) #print(key,values) that means tuples form
print(mydic2.get("Third"))

'''#this method is same to print(mydic2["Third"] 
# but when this key not present in dictonary return none ,
# print(mydic2["Third"] it is return error
'''



