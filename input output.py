f=open("sudipta.txt.txt","r") #open the file
data=f.read()    #read the file
#data=f.read(5)  #print only five char
print(data)    #print the data
f.close()     #close the file


f=open("sudipta.txt.txt","r")
#print first line
data=f.readline()
print(data)
#print second line
data=f.readline()
print(data)
f.close()


#a = open for appending mode
#r = reading mode
#w = writing mode
#+ = udating mode
#'rb' = will open read in binary mode
#'rt' = will open read in text mode


f=open("sudipta.txt.txt","w")
f.write("write in file")    #write the data in file
f.close()


f=open("sudipta.txt.txt","a")
f.write(" \ni am appending")    #append the data in file
f.close()


with open("sudipta.txt.txt","r") as f:
    a=f.readline()      #another way to open the file and also raed
print(a)