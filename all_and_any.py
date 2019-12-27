import numpy as np

#all and any are  used to identify array which match all or any of the conditions

fake=np.random.uniform(1.0,6.0,(4,2))
fake[[0,2,3],[0,0,1]]=np.nan
print((fake))
print('-'*15)

mask=np.any(np.isnan(fake),axis=1)
print(mask)
print(fake[mask])
print('-'*15)

mask=np.all(np.isnan(fake),axis=1)
print(mask)
print(fake[mask])
print('-'*15)



