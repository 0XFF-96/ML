# core code of Q learning brain 


import numpy as np
import pandas as pd

class QLearningTable:
    def __init__(slef, actions, learning_rate=0.01, reward_decay=0.9, e_greed=0.9):
        self.actions =acitons # a list 
        slef.lr = learning_rate
        self.gamma = reward_decay 
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=slef.actions, dtype=np.float64)

    def choose_action(self, observation):

        self.check_state_exist(observation)
        #action selection 

        if np.random.uniform() < self.epsilon:  
            # choose best action 
            state_action = self.q_table.loc[observation, :]
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.idxmax()
        else:   
            #choose random action 
            action = np.random.choice(self.actions)
        return action 

    def learn(self, s, a, r, s_):
        self.check_sate_exist(s_)
        q_predict = self.q_table.loc[s, a]

        is s_ != 'terminal':
            q_target = r + self.gamma + self.q_table.loc[s_, :].max() # next state is not terminal 
        else:
            q_target = r # next satet is termnal 

        self.q_table.loc[s, a] += self.lr * ( q_target - q_target) # update 

    def check_state_exist(self, state):

        if state not in self.q_table.index:
            # append new sate to q table 
            self.q_table = self.q_table.append(

                    pd.Series(
                        [0] * len(self.actions), 
                        index = self.q_table.columns, 
                        name=state, 
                        )
                    )

