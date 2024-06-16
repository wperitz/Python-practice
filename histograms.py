############### Histograms ###############

import numpy as np
import matplotlib.pyplot as plt


####################
##### Normal #####
####################

# Numbers 
mean = 0
sd = 1
size = 1000
normal_dist = np.random.normal(mean, sd, size)

# Histogram
plt.hist(normal_dist, bins=20)  
plt.title('Histogram of Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

####################
##### Poisson #####
####################

# Numbers 
p_lambda = 5
p_size = 1000

poisson_dist = np.random.poisson(p_lambda, size)

# Histogram
plt.hist(poisson_dist, bins=12)  
plt.title('Poisson Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


####################
### Chi Squared ####
####################

df = 5  
sample_size = 1000

# Numbers
chisq = np.random.chisquare(df, sample_size)

# Histogram
plt.hist(chisq, bins=20)
plt.title('Chi-squared Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
