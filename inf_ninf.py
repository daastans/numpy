import numpy as np

#inf and NINF , like nan they are also floating point constants

fake_inf=np.array(([np.inf,np.NINF]))
print(fake_inf)

#division by zero
np.array([1,2,3,4])/0 # [-inf,inf]

#special behaviour is reserved in numpy
np.inf*22    #inf
np.inf+np.inf #inf
np.inf-np.inf #inf
np.inf/np.inf #inf

#Equivalency
np.inf==np.inf #True
np.NINF==np.NINF #True

#Locating infinite values

fake_inf=np.array([4.4,np.inf,1.0,np.NINF])
fake_inf==np.inf #[False,True,False,False]
fake_inf==np.NINF #[False,False,False,True]

print(np.isposinf(fake_inf))
np.isneginf(fake_inf)
np.isinf(fake_inf) #[False,True,False,True]
