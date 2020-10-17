%matplotlib qt5
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import time

cap = 10
ten_pow = 6
for i in range(0,ten_pow):
    start_time = time.time()
    circlex = []
    circley = []

    squarex = []
    squarey = []

    for i in range(0, cap):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if(x**2 + y**2 >= 1):
            squarex.append(x)
            squarey.append(y)
        else:
            circlex.append(x)
            circley.append(y)

    pi = (4*len(circlex))/float(cap)
    print("Computational time", "--- %s seconds ---" % (time.time() - start_time))

    print("numpy PI is: ", np.pi)
    print("our aprox PI is: ", pi, "for", cap, "samples")
    print("")
    cap = cap*10
    
plt.plot(circlex,circley,"g.")
plt.plot(squarex,squarey,"y.")
plt.grid()
