"""
Logistic Function: f(x) = 1 / (1+e ^(-x))

Created by: MJ

"""

"""
Ref Stack Overflow:

The sigmoid function is a special case of the Logistic function when L=1, k=1, x0=0.


- L is the maximum value the function can take. e−k(x−x0) is always greater or equal than 0, so the maximum point is achieved when it it 0, and is at L/1.

x0 controls where on the x axis the growth should the, because if you put x0 in the function, x0−x0 cancel out and e0=1, so you end up with f(x0)=L/2, the midpoint of the growth.

the parameter k controls how steep the change from the minimum to the maximum value is.
"""

import math
import numpy as np

def sigmoid(x,library="math"):
	if library=="math":
		return 1/(1+math.exp(-x))
	else:
		return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
	return x*(1-x)

if __name__ == "__main__":
	print(sigmoid(0.75))
	print(sigmoid_derivative(0.75))
