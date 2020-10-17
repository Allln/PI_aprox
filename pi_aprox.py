%matplotlib qt5
from numpy import random
import numpy as np
import matplotlib.pyplot as plt

N = 10000

circlex = []
circley = []

squarex = []
squarey = []

i = 1

for i in range(0,N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if(x**2 + y**2 <= 1):
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
        
pi = 4*len(circlex)/float(N)

print("numpy PI is: ", np.pi)
print("our aprox PI is: ", pi)
        
plt.plot(circlex,circley,"g.")
plt.plot(squarex,squarey,"y.")
plt.grid()
