# encoding = utf-8

from layers import * 


def main():

	datalayer1 = Data('train.npy', 1024)

	datalayer2 = Data('validate.npy', 10000)

	inner_layers = []

	inner_layers.append(FullyConnect(17 * 17 , 26))
	inner_layers.append(Sigmoid())
	losslayer = QuadraticLoss()

	accuracy = Accuracy()

	for layer in inner_layers:

		layer.lr = 1000.0

	epochs = 20

	for i in range(epochs) :

		print 'epochs:', i
		
		losssum = 0
		iters = 0 

		while True:

			data, pos = datalayer1.forward()

			x, label = data

			for layer in inner_layers:

				x = layer.forward(x)

			loss = losslayer.forward(x, label)

			losssum += loss

			iters += 1
			d = losslayer.backward()

			for layer in inner_layers[::-1]:

				d = layer.backward(d)

			if pos == 0:

				data, _ = datalayer2.forward()
				x, label = data

				for layer in inner_layers:
					x = layer.forward(x)
				accu = accuracy.forward(x, label)

				print 'losss:', losssum / iters
				print 'accuracy:', accu 

				break
if __name__ == '__main__':
	main()


