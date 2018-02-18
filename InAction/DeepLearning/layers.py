import numpy as np

class Data:

	def __init__(self, name, batch_size):

		with open(name, 'rb') as f:

			data = np.load(f)

		self.x = data[0]
			
		self.y = data[1]
		self.l = len(self.x)
		self.batch_size = batch_size

		self.pos =  0 


	def forward(self):

		pos = self.pos
		bat = self.batch_size
		l = self.l

		if pos + bat >= l:

			ret = (self.x[pos:l],self.y[pos:l])
			self.pos = 0 
			index = range(l)

			np.random.shuffle(index)
			self.x =self.x[index]
			self.y = self.y[index]

		else: 
			ret = (self.x[pos:pos + bat], self.y[pos:pos + bat])
			self.pos += self.batch_size

		return ret, self.pos

	def backward(self, d):
		pass


class FullyConnect:

	def __init__(self, l_x, l_y):

		self.weights = np.random.randn(l_y, l_x) / np.sqrt(l_x)

		self.bias = np.random.randn(l_y, 1)

		self.lr = 0

	def forward(self, x):

		self.x = x

		self.y = np.array([np.dot(self.weights, xx) + self.bias for xx in x])

		return self.y

	def backward(self, d):

		ddw = [np.dot(dd, xx.T) for dd, xx in zip(d, self.x)]

		self.dw = np.sum(ddw, axis=0) / self.x.shape[0]
		self.db = np.sum(d, axis=0)  / self.x.shape[0]
		self.dx = np.array([np.dot(self.weights.T, dd) for dd in d])

		self.weights -= self.lr * self.dw 
		self.bias -= self.lr * self.db

		return self.dx  


class Sigmoid:

	def __init__(self):
		pass

	def sigmoid(self, x):
		
		return 1 / (1 + np.exp(-x))

	def forward(self, x):

		self.x = x
		self.y = self.sigmoid(x)

		return self.x

	def backward(self, d):

		sig = self.sigmoid(self.x)
		self.dx = d * sig * (1- sig)

		return self.dx 

class QuadraticLoss:

	def __init__(self):

		pass

	def forward(self, x, label):

		self.x = x
		self.label = np.zeros_like(x)

		for a, b in zip(self.label, label):

			a[b] = 1.0 

		self.loss = np.sum(np.square(x - self.label)) / self.x.shape[0] / 2

		return self.loss

	def backward(self):

		self.dx = (self.x - self.label) / self.x.shape[0] 

		return self.dx

class Accuracy:

	def __init__(self):
		pass

	def forward(self, x, label):

		self.accuracy = np.sum([np.argmax(xx) == ll for xx, ll in zip(x, label)])

		self.accuracy = 1.0 * self.accuracy / x.shape[0]

		return self.accuracy


