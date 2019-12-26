import numpy as np

fake=np.array([[10,2,23,42],
              [2,3,42,53],
              [2,553,455,66]])

#stored internally as contiguous block of memory
#np gives it two axis for access
#we can subset numpy array using two indices

fake[0] #returns row1
fake[0,None] #returns row1
fake[:1] #returns row1

fake[1:3,[-2,-2]] #returns 2nd-3rd row and 2nd to last column

#Modifying Elements

fake[0,0]=0
fake[1]=fake[2]
fake[[0,1,2],[0,1,2]]=[0,0,0] #zeros at diagonal
