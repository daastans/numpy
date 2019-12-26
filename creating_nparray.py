import numpy as np

np.array(['s','s','s']) #from list
np.array([['s','s','s'], #from list of lists
          ['s','s','s'],
          ['s','s','s']])

np.zeros(shape=(3,5)) #3x5 array of zeros

np.full(shape=(3,5),fill_value="cat")

sa=np.arange(start=1,stop=5,step=1) #sequence array [1,2,3,4]
print(sa)

ra=np.random.randint(1,7,size=(3,3)) #random int in some range
print(ra)
