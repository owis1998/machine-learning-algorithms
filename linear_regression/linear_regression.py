from numpy import *


def hypothesis(x, t0, t1):
	return t0 + t1 * x

def cost(points, t0, t1):
	sumition = 0

	for i in range(0, len(points)):
		x = points[i][0]
		y = points[i][1]

		sumition += (hypothesis(x, t0, t1) - y) ** 2
	
	return sumition / len(points)

def cost_for_minmiz(points, t0, t1, flag = 1):
	sumition = 0

	for i in range(0, len(points)):
		x = points[i][0]
		y = points[i][1]

		if flag:
			sumition += (hypothesis(x, t0 , t1) - y)
		else:
			sumition += (hypothesis(x, t0 , t1) - y) * x

	return (2*sumition) / len(points)

def gradient_descent(points, t0, t1, a):
	for i in range(0, 1000):
		tmp0 = t0 - (a * cost_for_minmiz(points, t0, t1))
		tmp1 = t1 - (a * cost_for_minmiz(points, t0, t1, 0))

		t0, t1 = tmp0, tmp1	

	return t0, t1


def main():
	points = genfromtxt('data_set.csv', delimiter = ',')
	t0 = 0
	t1 = 0
	learning_rate = 0.0001	

	t0, t1 = gradient_descent(points, t0, t1, learning_rate)
	print('t0 = {}, t1 = {}'.format(t0, t1))
	print('errors: {}'.format(cost(points, t0, t1)))

if __name__ == '__main__':
	main()
