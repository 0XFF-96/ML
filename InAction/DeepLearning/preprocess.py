# created by wz on 17-3-23.
# encoding=utf-8 

import sys
from scipy import misc 
import numpy as np

def main():

	l = len(sys.argv)

	if l < 2:

		print 'eg: python img2pkl.py list.txt dst.npy\n'\
			'convert image to npy \n'

		return 

	src = sys.argv[1]
	
	dst = sys.argv[2] if l > 2 else 'data.pkl'

	with open(src, 'r') as f:
		list = f.readlines()

	data = []
	labels = []

	for i in list:

		name, label = i.strip('\n').split(' ')

		print name + ' processed'
		
		img = misc.imread(name)

		img /= 255
		img.resize((img.size, 1))

		data.append(img)
		labels.append(int(label))

	print 'write to npy'

	np.save(dst, [data, labels])

	print 'completed'

if __name__ == '__main__':

	main()


