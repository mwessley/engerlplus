import numpy as np
names = ('ma','vicky','mischa','jaqueline','martin','anna','wolfi','maria','matti')
order = np.random.permutation(9)
i=0
while i<9:
    if int(order[i]/2) != int(order[(i+1)%9]/2):
        i+=1
    else:
        order = np.random.permutation(9)
        i=0
for i in range(9):
    print(names[order[i]] + ' -> ' + names[order[(i+1)%9]])
