'''

the DQN improvement: Prioritized Experience Replay (based on )
View more on my turorial page :https://morvanzhou.github.io/tutorials/
Using:
Tensorflow:1.0
gym:0.80
'''

import numpy as np
import tensorflow as tf
tf.set_random_seed()

class SumTree(object):

    '''
    This SumTree code is modified version and the original code is form;
    https://github.com/jaara/Al-blog/blob/master/SumTree.py
    Stroy the data with it priority in tree and data framewrodks.   
    '''

    data_pointer = 0 

    def __init__(self, capacity):
        self.capacity = capacity # for all priority values 
        self.tree = np.zeros(2 * capacity - 1)

        self.data = np.zeros(capacity, dtype=object)  # for all transitions

    def add(self, p, data):
        
