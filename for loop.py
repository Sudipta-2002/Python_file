
fruit=["mango","banana","grapes","litchi"]

for item in fruit:
    print(item)

#print 1 to 10

for i in range(1,11):
    print(i)
#print 1 t0 10 and step size is 1

for i in range(1,11,2):   #(start vale,end value,step size)
    print(i)              #end=(end-1),stepsize=(stepsize-1)

#for loop with print else condition
for i in range(1,6):
    print(i)
else:
    print("done")

#for loop using break
for i in range(1,11):
    print(i)
    if i==5:    #print 1 to 5 then break the loop
       break
    else:
        print("done")    #do not print else part because for loop is break

#for loop using continue
for i in range(1,11):

    if i==5:    #continue statements skeep the value in the loop
                #in the example 5 is skeep
       continue
    print(i)

#print even number within 10
for i in range(0,11):
    if i%2==1:
       continue
    print(i)


#factorial number
fact=1
n=4
for i in range(n):
    fact=fact * (i+1)
print(fact)

