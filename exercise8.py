"""#8 Gaussian probability given f(x) where phi is std_dev assuming phi=1, use
 np.trapz to find the probability of -2<x<2 by evaluating the integral: (given)
 Call your program exercise8.py Use a step-size no larger than .005. Print your
 result. Should be in the neighborhood of .95  (FWIW, I get .9543798194879075)

 TEST CODE blocks will be commented out in Final; they have been useful to 
 check functionality.


"""

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import norm #NORM! (sorry, old tv show joke...)


#Set parameters for Gaussian distribution
mean = 0
std_dev = 1 #given phi=1

# Generate x values 
x=np.linspace(-2, 2)  #-2 to +2,



def gaussian_distribution(x, mean, std_dev):
    
    #return norm.pdf(x, mean, std_dev) #This is test code. Real equation v2.0
    y=((1/((math.sqrt(2*np.pi))))*(np.e**((-x**2)/2)))
    return np.trapz(y, x, .05) #Implement trapz calculation

#Calculate Gauusian prababilities for each x value
y = gaussian_distribution(x, mean, std_dev)

print (y)

#TEST CODE Plot the Gaussian distribution (This is for inspection & practice)
#plt.plot(x, y)
#plt.title("Gaussian Probability Distribution")
#plt.xlabel("X")
#plt.ylabel("Probability Density")
#plt.show()
