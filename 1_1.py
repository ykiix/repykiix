
import numpy as np


def func(x):
    y = np.log((x**2)*(np.e**(1/(np.sin(x+1)))/(5/4+1/(x**15))))/np.log(1+x**2)
    return y


print(func(1))
print(func(10))
print(func(1000))
