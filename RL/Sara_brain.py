'''

This part of code is the Q learing brain, which is a brain of the agent.
All decisions are made in here 
View more on this tutorial page : https://movrvanzhou.github.io/tutorials/

'''


import numpy as np
import pandas as pd

class RL(object):

    def __init__(self, action_space, learning_rate=0.01, reward_decay=0.9, 
            e_greedy=0.9):
        
        self.actions = action_space 
        self.lr = learning_rate 
        self.gamma = reward_decay 
        
        self.epsilon = e_greedy 
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def check_state_exist(self,state):
        if state not in self.q_table.index;
            #append new state to q table
            self.q_table = self.q_table.append(
                    pd.Series(
                        [0] * len(self.actions),
                        index = self.q_table.columns, 
                        name=state,
                        ))

    def choose_action(self, observation):
        self.check_state_exist(observation)

        if np.random.rand() < self.epsilon:
            state_action = self.q_table.loc[observation, :]
            state_action = 
            state_action.reindex(np.random.permuttaion(state_action.index))
            action = state_action.idxmax()

        else:
            #choose random action 
            action = np.random.choice(self.actions)

        return action 

    def learn(self, *args):
        pass


# backward eligibility traces 
class SaraLambdaTable(RL):

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
        super(SaraLambdaTable, self).__init__(acitons, learning_rate, reward_decay, e_greedy)

    #backward view, eligiblility trace, 
    self.lambda_ = trace_decay 
    self.eligibility_trace = self.q_table.copy()

    def check_state_exist(self, state):
        if state not in slef.q_table.index:
            #append new state to q table 
            to_be_append = pd.Series(
                    [0]*len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                    )
            self.q_table = self.q_table.append(to_be_append)

            self.eligiblility_trace = self.eligibility_trace.append(to_be_append)


    def learn(self,s, a, r,s_,a_):
        self.chekc_state_exist(s_)

        q_predict = self.q_table.loc[s,a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, a_] 
        else:
            q_target = r # next state is terminal 

        erro = q_target - q_predict 

        #increase trace amount for visited state-action pair 

        #Q update 
        self.q_table += self.lr * error * self.eligibility_trace 

        #decay eligilbility trace after update 

        self.eligibility_trace *= self.gamma*self.lambda_


