import numpy as np

names=np.array(["Aman","Mickey","Ayesha"])
ages=np.array([22,22,69])
genders=np.array(['m','m','f'])

whos_24=names[ages>=24]
print(whos_24)

male_22=names[(genders=='m')&(ages>=22)]
print(male_22)

adults=names[~(ages<=18)]
print(adults)
