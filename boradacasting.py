import numpy as  np

fake=np.array([
    [1,1,1],
    [2,2,2],
    [3,3,3],
    [4,4,4]
])

bake=np.array([5,3,1])
baked=fake+bake #added 5 to 1st , 3-2nd , 1-3rd columnn

shaked=fake + 0.5 #shifting operation
maked=fake*1.3 #translation operation


######### How broadcasting works
# Supose we want to multiply A*B
# Moving backwards from  last dimension of each array ,we check if they are compatible
# Dimension are compatible if they are equal of either of them is 1
# If so they are compatible
## Example
# A=(3,4) B=(3,1) , Compatible B can be transformed by making four copy of B columns
# A=(3,1,4) B=( 2,1) , compatible , both arrays would be conceptually transformed
