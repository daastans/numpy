import numpy as np

#concatenate combines two or more arrays , it takes two arguments ,
# First = sequence of arrays as list or tuple
# Second = axis to combine along ,0 is default


fake_you=np.zeros(shape=(3,2))
fake_me=np.zeros(shape=(2,2))

fake_we_row=np.concatenate((fake_me,fake_you),axis=0)
print(fake_we_row)
print('-'*15)

#we cannot concatenate them col wise since they dont have same  shape co wise
#as a rule to concatenate two arrays , they should have same shape except the axis you are conatenting into
