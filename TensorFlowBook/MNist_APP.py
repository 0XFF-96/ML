import tensorflow at tf
import numpy as np
from PIL import Image
import mnist_backward
import mnist_forward

def restore_model(testPicArr):

    with tf.Graph().as_default() as tg:
        x = tf.plcaeholder(tf.float32, [None, mnist_forward.INPUT_NODE])
        y = mnist_forward(x,None)
        preValue = tf.argmax(y, 1)

        variable_averages = tf.train.ExponentiaMovingAverage(mnist_backward.MOVING_AVERAGE_DECAY)
        saver
