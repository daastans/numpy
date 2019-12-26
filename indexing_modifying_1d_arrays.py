import numpy as np

fake=np.array([10,2,23,42,42,53])

fake[4] #accessing ith element
fake(len(fake)-1) #last element
fake[-1] #last element

fake[[1,2,5]] #multiple elements

fake[:2] #ever element before index 2
fake[2:] #every element index 2 onwards
fake[::2] #every second element

fake[[1,2,5]]=[122,333,555] #modifying multiple values
