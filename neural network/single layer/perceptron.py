def NN(x1, x2, y, w1, w2):
	tehta = 0.2		
	a = 0.1

	epoch = 1
	while epoch < 100:
		total_error = 0
		epoch += 1

		for i in range(0, len(x1)):
			step_fun = 1 if ((x1[i] * w1) + (x2[i] * w2) - tehta) >= 0 else 0
			error = (y[i] - step_fun)
			total_error += abs(error)

			w1 += a * x1[i] * error
			w2 += a * x2[i] * error

		if total_error == 0:
			return w1, w2
      
	return w1, w2

def main():
	x1 = [0, 1, 0, 1]
	x2 = [0, 0, 1, 1]
	y = [0, 0, 0, 1]

	w1 = 0.2
	w2 = -0.3

	w1, w2 = NN(x1, x2, y, w1, w2)
	print(w1, w2)

if __name__ == '__main__':
	main()
