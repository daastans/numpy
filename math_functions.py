import numpy as np

fake=np.random.randint(1,29,(3,3))
fake_some=np.sum(fake) #sum of all elements in
print(fake_some)
print('-'*15)

fake_row_sum=np.sum(fake,axis=1)
print(fake_row_sum)
print('-'*15)

fake_col_sum=np.sum(fake,axis=0) #would collapse array into 1D array
print(fake_col_sum)
print('-'*15)

frs_without_collpase=np.sum(fake,axis=1,keepdims=True)
print(frs_without_collpase)
print('-'*15)

fcs_without_collpase=np.sum(fake,axis=0,keepdims=True) #keeps dimension of axis intact
print(fcs_without_collpase)
print('-'*15)

#if there is any nan value  , sum would be nan , to exclude them use where
fake_nan=np.random.uniform(1.0,2.0,(3,3))
fake_nan[0,0]=np.nan
print(np.sum(fake_nan))
print('-'*15)

print(np.sum(fake_nan,where=~(np.isnan(fake_nan))))
print('-'*15)
print(np.nansum(fake_nan)) #achieves same effect as above

