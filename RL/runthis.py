'''

Sara is a online updating method ofr Reinforcement learning 
Unline Q learning which is a offline updating method, Sarsa is updating which in the current tarjectory

'''

from maze_env import Maze
from RL_brain import SarsaTable

def update():

    for episode in range(100):
        # initial observaion 
        observation = env.reset()

        #RL choose action based on observation 
        action = RL.choose_action(str(observation))

        while True:
            #freash env 

            env.render()

            # RL take action and get next observation and reward 
            observation_, reward, done = env.step(action)

            actions_ = RL.choose_action(str(observation_))

            RL.learn(str(obsercation), action, reward, str(observation_), action_)

            observation = observation_
            action = action 

            if done:
                break 

    #end of game 
    print('game over')
    env.destropy()

if __name__=='__main__':

    env = Maze()
    RL = SarasTable(actions=list(range(env.n_actions)))

    env.after(100, update)
    env.mainloop()


