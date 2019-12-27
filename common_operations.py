import numpy as np

fake=np.random.randint(1,19,5)
bake=np.random.randint(0,6,5)
print(fake)
print(bake)


#follows vecotirsation ,since using loop induces latency as it has to call C function on low level
bake=np.where((bake==0),fake*2.0,fake/2.0)
print(bake)
