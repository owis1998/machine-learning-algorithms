from numpy import *


def hypothesis(inputs, t):
	total = t[0]

	for i in range(0, len(inputs)):
		total += inputs[i] * t[i]
		
	return total


def cost(points, t):
	total = 0

	for i in range(0, points.shape[0]):
		total += (hypothesis(points[i][:-1], t) - points[i][-1]) ** 2

	return total / (2 * points.shape[0])

def minmize_cost(points, t, flag):
	total = 0
	for i in range(0, points.shape[0]):
		if flag:
			total += (hypothesis(points[i][:-1], t) - points[i][-1]) * points[i][flag]
		else:
			total += hypothesis(points[i][:-1], t) - points[i][-1]

	return total / points.shape[0]

def gradient_descent(points, t, a):
	for j in range(0, 1000):
		tmp = []
		for i in range(0, len(t)):
			k = t[i] - (a * cost_for_minize(points, t, i))
			tmp.append(k)
		t = tmp.copy()

	return t


def main():
	points = genfromtxt('data_set.csv', delimiter = ',')
	t = [0 for _ in range(0, points.shape[1])]
	learning_rate = 0.0001

	t = gradient_descent(points, t, learning_rate)

	print('the coefficients {}'.format(t))
	print('errors {}'.format(cost(points, t)))


if __name__ == '__main__':
	main()
