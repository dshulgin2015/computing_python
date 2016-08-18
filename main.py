from __future__ import division
from numpy import * 



def integrate(f, a, b,n):
	h = (b-a)/n
	range_ = array(range(1,n))
	return h/2 * (f(a) + f(b)) + sum(h*f(a + h*range_))




#Monte-Carlo integration

def intergate_MC(f,a,b, accuracy = 100):
	from numpy.random import uniform as uniform
	points = uniform(a,b,accuracy)
	return round(((b - a)/accuracy)* sum(f(points)))







	
if __name__ == '__main__':

	def f(x):
		return 2*x + 1

	print integrate(f,1,500,100)

	print intergate_MC(f,1,500,100000)