# Viusal Demo

import numpy as np
import matplotlib.pyplot as plt


########################
######## Normal distribution with a small n value ########
########################
mean = 0
sd = 1
size = 50
normal_dist = np.random.normal(mean, sd, size)

# Histogram
plt.hist(normal_dist, bins=15)  
plt.title('Normal Distribution (small n)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


####################
######## Normal distribution with a large n value ########
####################
mean = 0
sd = 1
size = 50000
normal_dist = np.random.normal(mean, sd, size)

# Histogram
plt.hist(normal_dist, bins=30)  
plt.title('Normal Distribution (large n)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


########################
######## Binomial distribution with a small n value ########
########################
n = 20
p = 0.5 
size = 100  
binomial_dist = np.random.binomial(n, p, size)

# Histogram
plt.hist(binomial_dist, bins=10)  
plt.title('Binomial Distribution (small n)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


########################
######## Binomial distribution with a large n value ########
########################
n = 200000
p = 0.5 
size = 100000  
binomial_dist = np.random.binomial(n, p, size)

# Histogram
plt.hist(binomial_dist, bins=15) 
plt.title('Binomial Distribution (large n)')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
