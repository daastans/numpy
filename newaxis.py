import numpy as np

fake=np.array([[1,2,3,4,5],
              [1,2,3,4,5]])


bake=np.array([5,0])

#print(fake-bake) #error

ake=fake-bake[:,np.newaxis] #adding new column axis
ake=fake-bake[:,None] #Same effect
print(ake)
