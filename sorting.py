import numpy as np

#sort sorts array along given axis , it takes three arguments
#a : array , axis : axis to sort along (default = -1 , last axix) , Kind : sorting method


fake=np.random.choice(np.arange(9),size=9,replace=True)
print(fake)
fake_sort=np.sort(fake)
print(fake_sort)
print('-'*10)

#### Reverse sorting
# Method 1 : sort in asc , than reverse output
# Method 2 : Negate array , sort asc , negate output , doenst work on string arrays


fake_reverse=np.sort(fake)[::-1]
print(fake_reverse)
print('-'*10)
print(~np.sort(~fake))
print('-'*10)

####### NOTE
# np.sort uses quicksort which is not stable , i.e., it might swap the places of equal valued data
#For stable sor use parameter kind=stable  which uses radix sort or other techniques

print(np.sort(fake,kind='stable'))
print('-'*10)

## Sorting Multidimensional array , specify axis

fake_nd=np.random.randint(1,27,(3,3),dtype='int32')
print(fake_nd)

fake_nd_sort=np.sort(fake_nd,axis=1)
print(fake_nd_sort)
print('-'*10)


######Sorting a row based on certain row
# argsort sorts a row and then return new index of sorted elemnts , we can use it to sort other rows of array

get_indexes=np.argsort(fake_nd[0])
print(get_indexes)
print(fake_nd[:,get_indexes]) #the required effect
print('-'*10)

print(fake_nd[np.argsort(fake_nd[:,1]),:]) #sorted along column 2nd
print('-'*10)
