import numpy as np

fake=np.array([10,2,23,42,42,53])
bake=np.array([10,2,23,42,42,53])

#following operation happen elementwise
fbake= fake+bake #addition
print(fbake)

ake=fake-bake #subtraction
print(ake)

_bfake=bake*fake #multiplication
print(_bfake)

b_fake=fake/bake #division
print(b_fake)

#matrix_multiplication
mat_mul=fake@bake
print(mat_mul)
