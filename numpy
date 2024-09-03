#------->python libraries<----------
#numpy:numpy stands for numerical python and it used complex mathematical problem and scientific computing
#it consist of multi dimensional  arrays(eg.x,y,z)

#--------->single dimensional array<-----------
# import numpy as np
# n1=np.array([10,20,30])
# print(n1)

#--------->two dimensional array<-----------
# import numpy as np
# n1=np.array([[12,13,14],[15,16,17]])
# print(n1)
# print(type(n1))

#--------->numpy array intializing with zero<----------
# import numpy as np
# n1=np.zeros((10,10))    ##(row=10,col=10 and all values are zero)
# print(n1)

#--------->numpy array intializing row coloum are same vale<-----------
# import numpy as np
# n1=np.full((5,5),1)     ##((row=5,col=5),value=1)
# print(n1)

#--------->intializing numpy array with a range<-----------
# import numpy as np
# n1=np.arange(10,41,5)   ##(array element starting 10 & stop 40 & gap each element 5)
# print(n1)

# #-------->numpy array increment seris<----------
# import numpy as np
# n1=np.arange(10,51,10)
# print(n1)

#-------->numpy array decrement seris<----------
# import numpy as np
# n1=np.arange(50,9,-10)
# print(n1)

#-------->numpy array intializing random value<----------
# import numpy as np
# n1=np.random.randint(1,100,5)
# print(n1)

#-------->cheack numpy array shape<----------
# import numpy as np
# n1=np.array([[10,20,40],[50,30,60]])
# print(n1)
# print(n1.shape)
# n1.shape=(3,2)
# print(n1)
# print(n1.shape)

#------->numpy array joining or concatinnating two numpy array<--------
# import numpy as a
# n1=a.array([[10,20,30],[40,50,60]])
# n2=a.array([[12,13,14],[15,16,17]])
# print(a.vstack((n1,n2)))   ##two array join verticaly
# print(a.hstack((n1,n2)))   ## two array join horizentaly
# print(a.column_stack((n1,n2)))

# import numpy as a
# n1=a.array([10,20,30])
# n2=a.array([12,13,14])
# print(a.vstack((n1,n2)))   ##two array join verticaly
# print(a.hstack((n1,n2)))   ## two array join horizentaly

#--------->numpy array addition<-----------
# import numpy as np
# n1=np.array([10,20])
# n2=np.array([30,40])
# n3=np.array([50,60])
# print(np.sum([n1,n2,n3]))         ##sum function is add all the element of the matrix 
# print(np.sum([n1,n2,n3],axis=0))  ##axis=0 means coloumns value will be add
# print(np.sum([n1,n2,n3],axis=1))  ##axis=1 means row value 

#----->nupy array union & intersection<---------
# import numpy as np
# n1=np.array([10,20,30,50,34,23])
# n2=np.array([12,20,30,50,23])
# print(np.intersect1d(n1,n2))
# print(np.union1d(n1,n2))
# print(np.setdiff1d(n1,n2))   

#----->numpy array scalar operation<-------
# import numpy as np
# n1=np.array([10,20,30,50,34,23])
# n1=n1+1      ## n1 each element add 1
# print(n1)
# n1=n1-1      ## n1 each element subtract 1
# print(n1)
# n1=n1*2      ## n1 each element mutiply by 2
# print(n1)
# n1=n1/2      ## n1 each element devided by 2
# print(n1)
# n1=np.array([[10,20,30,50,34,23],[23,34,45,6,7,8]])
# n1=n1+1      ## 2d array all element add 1
# print(n1)

#----->function mean median standerd derivation<-------
# import numpy as np
# n1=np.array([12,13,14,15])
# print(np.max(n1))
# print(np.mean(n1))
# print(np.median(n1))
# print(np.std(n1))

#------>numpy array save & load<--------
# import numpy as np
# n1=np.array([12,13,14,15])
# np.save('my_numpy',n1)
# n2=np.load('my_numpy.npy')
# print(n2)

#------>function reshape<-------
# import numpy as np
# n1=np.array([[10,20,40],[50,30,60]])
# print(n1.shape)
# print(n1.ndim)    ##print the dimension of array
# print(n1)