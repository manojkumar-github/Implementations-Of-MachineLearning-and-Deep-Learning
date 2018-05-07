"""

Tanh Function: f(x) = 2g(2x)-1
                    = (e^x - e^-x)/(e^x + e^-x)

Created by: MJ

"""

"""
The tanh function, a.k.a. hyperbolic tangent function, is a rescaling of the logistic sigmoid, such that its outputs range from -1 to 1. (There’s horizontal stretching as well.)

Yes it matters for technical reasons. Basically for optimization. It is worth reading Efficient Backprop by LeCun et al.

There are two reasons for that choice (assuming you have normalized your data, and this is very important):

Having stronger gradients: since data is centered around 0, the derivatives are higher. To see this, calculate the derivative of the tanh function and notice that its range (output values) is [0,1].
The range of the tanh function is [-1,1] and that of the sigmoid function is [0,1]

Avoiding bias in the gradients. This is explained very well in the paper, and it is worth reading it to understand these issues.
"""
import numpy as np
import math

def tanh(x,library ="math"):
	if library == "math":
		return math.tanh(x)
	else:
		return np.tanh(x)

def tanh_derivative(x,library="math"):
	if library == "math":
		return 1- math.tanh(x)**2
	else:
		return 1-np.tanh(x)**2

if __name__ == "__main__":
	print("tanh value is: ",tanh(0.75))
	print("tanh derivative is: ",tanh_derivative(0.75))