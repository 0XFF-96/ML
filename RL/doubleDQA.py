import gym 
from RL_brain import DoubleDQN
# Pendulum example 


import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf 


env = gym.make('Pendulum-v0')
env = env.unwrapped
env.seed(1)

MEMORY_SIZE = 3000
ACTION_SPACE = 11

sess = tf.Session()

with tf.variable_scope('Natural_DQN'):
    natural_DQN = DoubleDQN(
            n_actions=ACTION_SPACE,n_features=3, 
            memory_size = MEMORY_SIZE,
            e_greedy_increment=0.001, double_q = False,sess=sess
            )

with tf.variable_scope('Double_DQN'):
    double DQN = DoubleDQN(
            n_actions=ACTION_SPACE, n_features=3,
            memroy_size=MEMORY_SIZE,
            e_greedy_increment=0.001, double_q=True,sess=sess,
            output_graph=True)
sess.run(tf.globla_variables_initializer())


def trian(RL):
    
    total_steps = 0
    observation = env.reset()
    
    while True:
        # if total_steps - MEMORY_SIZE > 8000: env.render()

        action = RL.choose_action(observation)

        f_action = (action - (ACTION_SPACE-1)/2)/((ACTION_SAPCE-1)/4) 
        
        convert to [-2 ~2] float actions 
        observation_, reward, done , info = env.step(np.array([f_action]))

        reward /= 10 # normalize to a range of (-1, 0) r = 0 when get upright
        RL.store_trainsition(observation, action, reward, observation)

        if total_steps > MEMEORY_SIZE : 
            RL.learn()

        if total_steps - MEMORY_SIZE > 200000: # stop game 
            break 

        observation = oservation_

        total_steps += 1

    return RL.q

q_natrual = train(natural_DQN)
q_double = train(double_DQN)

