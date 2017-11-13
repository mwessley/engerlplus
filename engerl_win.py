import numpy as np
names = ('ma','vicky','mischa','jaqueline','martin','anna','matti','giulia','wolfi','maria')
order = np.random.permutation(10)
cont = (np.append(order,order[0])/2).astype(int)
i=0
while i<10:
    if cont[i] != cont[i+1]:
        i+=1
    else:
        order = np.random.permutation(10)
        cont = (np.append(order,order[0])/2).astype(int)
        i=0
order = np.append(order,order[0])
for i in range(10):
    print(names[order[i]] + ' -> ' + names[6])
