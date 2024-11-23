import numpy as np
import matplotlib.pyplot as plt

#Parameters
n = 10000
r = np.linspace(2.5,4.0,n)     #Control parameters
iterations = 1000
last = 100

#Initial conditions
x = 1e-5*np.ones(n)

#Storage for the Lyapunov exponent
lyapunov = np.zeros(n)

#Simulations
for i in range(iterations):
    x=r*x*(1-x)     #Logistic map
    lyapunov+=np.log(abs(r-2*r*x))

    #Plotting the bifurcation diagram
    if i >= (iterations-last):
        plt.plot(r, x, ',k',alpha=.25)


plt. xlim(2.5,4)
plt.title("Bifurcation Diagram")
plt.axhline(0.5,color = 'b',linestyle = '--',label ='Stable Fixed Point at x = 0.5')
plt.xlabel("r")
plt.ylabel("x")
plt.show()