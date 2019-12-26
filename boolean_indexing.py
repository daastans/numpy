import numpy as np

fake=np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4]
])

#IN Boolean indexing an array of boolean values is used to subset an array

#Example
mask=(fake==3) #created a 4x3 boolean mask
print(mask)

fake[mask]=0
print(fake)

#Using indexing to select rows and columns
rows_1_and_3=np.array([True,False,True,False])
cols_1_and_3=np.array([True,False,True])

r13=fake[rows_1_and_3]
print(r13)

c13=fake[:,cols_1_and_3]
print(c13)

r13_c13=fake[rows_1_and_3,cols_1_and_3] # == [[0,2],[0,2]
print(r13_c13)


