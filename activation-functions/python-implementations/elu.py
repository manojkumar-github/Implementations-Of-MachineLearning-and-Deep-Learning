"""
elu Function: f(x) = x if x ≥ 0 (identity function)
			  dy/dx = 1

			  f(x) = α.( ex – 1) if x < 0
			  dy/dx = α.ex – α + α = (α.ex – α) + α = y + α
Created by: MJ

"""
import math

def elu(x,alpha =1):
	return x if x>0 else alpha * (math.exp(-x) -1)

def elu_derivative(x,alpha=1):
	return 1 if x > 0 else elu(x)+alpha 

if __name__=="__main__":
	print("elu: ",elu(-0.6))
	print("elu: ",elu(0))
	print("elu: ",elu(0.6))

	print("elu_derivative: ", elu_derivative(-0.6))
	print("elu_derivative: ", elu_derivative(0))
	print("elu_derivative: ", elu_derivative(0.6))

