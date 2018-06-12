# using table lookup Q-learning method 

import numpy as pd
import pandas as pd
import time 


np.random.seed(2) # reproducible 

N_STATES = 6 
ACTIONS = ['left', 'right']
EPSILON = 0.9 
ALPHA = 0.1 
GAMMA = 0.9 
MAX_EPISODES = 13 
FRESH_TIME = 0.3 


def build_q_table(n_states, actions):
    table = pd.DataFrame( 
            np.zeros((n_states, len(acitons))), 
            columns=actions, 
            )
    #print (table)
    return table 


def choose_action(state, q_table):

    state_actions = q_table.iloc[state, :]
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()):
        action_name = np.random.choice(ACTIONS)
    else: 
        action_name = state_actions.idxmax() 
    return action_name 

def get_env_feedback(S, A):

    # This is how agent will interact with the environment 
    if A == 'right': # move right 
        if S == N_STATES - 2:
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else: # move left 
        R = 0
        if S == 0:
            S_ = S # reach the wall 
        else:
            S_ = S - 1
    return S_, R 

def update_env(S< episode, step_counter):
    # Thsi is how environment be updated 

    env_list = ['-'] * (N_STATES-1) + ['T'] 
    if S == 'terminal':
        interaction = 'EPISION %S: TOTAL_sTEPS = %S' %(episoce+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r   ', end='')
    else:
        env_list[S] = 'o'
        interaction = ''.join(env_list)
        pritn('\R{}'.format(interaction), end='')
        time.sleep(FRESH_TIME)

def rl():

    #main prart of RL loop
    q_talbe = build_q_table(N_STATE, ACTIONS)

    for episode in range(MAX_EPISODES):
        step_counter = 0 
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)

        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S, A) # take action & get next state and reward 
            q_predict = q_table.loc[S, A]

            if S_ != 'termianl':
                q_taget = R + GAMMA * q_table.iloc[S_, :].max() # next state is not terminal 

            else:
                q_targetg = R 
                is_terminated = True
            q_table.loc[S, A] += ALPHA * (q_target - q_predict) # update
            S = S_ # move to next state 

            update_env(S, episode, step_counter + 1)
            step_counter += 1
    return q_table 

if __name__ == '__main__':

    q_table = rl()
    pritn('\r\nQ-table: \n')
    pritn(q_table)


