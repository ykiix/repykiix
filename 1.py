
import numpy as np
x=float(input())
a=(x**2)*(np.e**(1/(np.sin(x)+1))/(5/4+1/(x**1*5)))
y=np.log(a)/np.log(1+x**2)
print(y)