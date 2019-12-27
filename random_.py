import numpy as np
from numpy import random

fake_rand=np.random.randint(low=2,high=6,size=5)
print(fake_rand)

np.random.seed(1237) #it would produce same results in different machines
fake_seeded_rand=np.random.randint(low=1,high=7,size=5)
print(fake_seeded_rand)
print('-'*10)

#Using np.random.choice to select without replacement
#a=1D array , size= size of output array, replace=replacement,p=1D array of probabilities of a

fake_choice=np.random.choice( #without replacement , meaning reouccerence of digits
    a=np.arange(1,7),
    size=5,
    replace=False,
    p=None
)

print(fake_choice)
print('-'*10)

fake_choice=np.random.choice(
    a=np.arange(1,7),
    size=5,
    replace=True,
    p=None
)
print(fake_choice)
print('-'*10)

##Trick of choosing 2D array rows using choice
fake_2D=np.random.randint(1,22,(4,2))
fake_2D_rows=np.random.choice(
    a=np.arange(len(fake_2D)),
    size=2,
    replace=False,
    p=None
)
print(fake_2D)
print(fake_2D[fake_2D_rows])
print('-'*10)

##Permutations of given 2D array
fake_2D_permutation=np.random.permutation(fake_2D)
print(fake_2D_permutation)
print('-'*10)


###probability distributions

np.random.uniform(low=1.0,high=3.0,size=(2,2))
np.random.normal(loc=0.0,scale=1.0,size=2)
np.random.binomial(n=10,p=0.25,size=(3,2))
