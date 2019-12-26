import numpy as np

fake=np.arange(1,9)

rake=fake.reshape(2,4) #class method
rake=np.reshape(a=fake,newshape=(2,4)) #same effect
print(rake)

#reorder last axis first
crake=rake.reshape((4,2),order='C') #C-Style  orders last axis first
print(crake)

frake=rake.reshape((4,2),order='F') #Fortan Style reorders first axis
print(frake)

#Transpose
fake.T
np.transpose(fake)

fake.reshape(2,2,2) #new dimension should have same number of elements
fake.reshape(-1,2) # auto-fit a dimension
