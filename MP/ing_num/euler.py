import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# fonction y'=y
def f(y,t):
    return y
# Condition initiale
y0=1
# descritisation de l'intervale [a,b]
a=0
b=10
n=100
t=np.linspace(a,b,n)

# integration avec odeint

y=odeint(f,y0,t)

plt.plot(t,y,'r-*')

# tracer la fonction exp(x) sur [a,b]

x=np.linspace(a,b, 100)
plt.plot(x,np.exp(x),'g')
plt.grid()
plt.show()

