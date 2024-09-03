#string slicing syntax
#start 0 index to end 5 index

#name="sudiptaisagoodboy"
word='''python is a popular programming language\nPython\tcan be used on a server to create web applications'''
print(word[0:5])
print(word[2:5])
print(word[2:])
print(word[:7])
print(word[0::2])
print(word[0:10:3])

#string function

print(len(word))
print(word.endswith("applications"))
print(word.endswith("server"))
print(word.capitalize())
print(word.find("is"))
print(word.count("s"))
print(word.upper())
print(word.lower())
print(word.replace("python","c"))
print(word.count("python"))
print(word.isalnum())
print(word.isalpha())
print(word.islower())
print(word.isprintable())  #all string print that is true other wise false

str1=" "
print(str1.isspace())

str2="sudipta is a good boy"
print(str2.istitle()) #every word first letter is capital that is print true otherwise false
print(str2.upper())
print(str2.swapcase())
print(str2.title())   #sentence every word capitalized

