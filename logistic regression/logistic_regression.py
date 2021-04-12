import math 
from numpy import *


def hypothesis(x, t0, t1):
	return 1 / (1 + math.e ** -(t0 + t1 * x))	

def cost(points, t0, t1):
	total = 0

	for i in range(0, len(points)):
		if points[i][1]:
			total += -math.log(hypothesis(points[i][0], t0, t1), 10)

		else:
			total += -math.log(1 - hypothesis(points[i][0], t0, t1), 10)


	return total / len(points)

def minmize_cost(points, t0, t1, flag):
	total = 0

	for i in range(0, len(points)):
		if flag:
			total += (hypothesis(points[i][0], t0, t1) - points[i][1]) * points[i][0]
		else:
			total += hypothesis(points[i][0], t0, t1) - points[i][1]

	return total 

def gradient_descent(points, t0, t1, a):
	for _ in range(0, 110):
		tmp0 = t0 - (a * minmize_cost(points, t0, t1, 0))
		tmp1 = t1 - (a * minmize_cost(points, t0, t1, 1))

		t0, t1, = tmp0, tmp1

	return t0, t1

def main():
	points = genfromtxt('dataset.csv', delimiter = ',')
	t0 = 1
	t1 = 1
	learning_rate = 0.0001	

	t0, t1 = gradient_descent(points, t0, t1, learning_rate)
	print('t0 = {}, t1 = {}'.format(t0, t1))
	print('errors: {}'.format(cost(points, t0, t1)))

if __name__ == '__main__':
 	main()
