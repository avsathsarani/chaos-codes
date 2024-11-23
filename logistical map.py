import numpy as np
import matplotlib.pyplot as plt

#Logistical map function
def logistical_map (r,x):
    return r*x*(1-x)

#Get input value of r
inp = input("Input value of r: ")
r = float (inp)
x0 = 0.5
n = 100

#Initialize array to store sequence
x=np.zeros(n)
x[0]=x0

#Generate sequence
for i in range (1,n):
    x[i]= logistical_map(r,x[i-1])

#Plot a sequence
plt.plot(range(n),x,'-o')
plt.title(f'Logistical map for r = {r}')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.ylim(0,1)
plt.show()

