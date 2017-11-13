import numpy as np
names = ('ma','vicky','mischa','jaqueline','martin','anna','matti','giulia','wolfi','maria')
order = np.random.permutation(10)
i=0
while i<10:
    if int(order[i]/2) != int(order[(i+1)%10]/2):
        i+=1
    else:
        order = np.random.permutation(10)
        i=0
for i in range(10):
    print(names[order[i]] + ' -> ' + names[order[(i+1)%10]])
