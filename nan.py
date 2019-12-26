import numpy as np

#nan is a floating point constant , np treats it specially
# np.nan==np.nan returns false in numpy
# np.nan!=nan returns true
# This is because missing values have unknown value

fake=np.ones(shape=(3,4))
fake[0,2]=np.nan

bol_fake=(fake==np.nan) #all false values would be here
print(bol_fake)

#faker=np.array([1,2,3],dtype="int64")
#faker[1]=np.nan #Would thrown an Error
### nan only works with floating valules

