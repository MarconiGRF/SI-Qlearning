from utils.utils import Utils
from utils.connection import connect, get_state_reward
from classes.constants import Constants 
import random

#Aqui vocês irão colocar seu algoritmo de aprendizado
if __name__ == '__main__':
    matrix = Utils.get_matrix_from_file()
    
    socket = connect(2037)
    state, reward = get_state_reward(socket, "jump")
    
    platform = str(int(state[:-2],2))
    direction = Constants.DIRECTION[str(state[-2:])]

    print('New platform is -> ' + platform)
    print('Direction is -> ' + direction)
    print('Reward from LAST platform+action is -> ' + str(reward))
    # for element in matrix:
    #     print(str(element))
