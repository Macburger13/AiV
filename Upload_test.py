#Victor Rodriguez Franco
#Anàlisis i visualització de dades

#We create different random numbers and calculate the mean and plot them.
import numpy as np
import matplotlib.pyplot as plt
import random
np.random.seed(2)

a = [1,3,1,5,-1,2,1]
b = [random.randint(0,100) for _ in range(100)]


print(np.mean(b))


plt.plot(b)
plt.show()