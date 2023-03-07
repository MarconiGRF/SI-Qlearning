from utils.utils import Utils
from utils.connection import connect, get_state_reward
from classes.constants import Constants 
from classes.platform_reward import PlatformReward
import random

state = '0000000'
platform = 0
reward = 0
action = ''
last_state = '0000000'
last_action = ''
#Aqui vocês irão colocar seu algoritmo de aprendizado
if __name__ == '__main__':
    matrix = Utils.get_matrix_from_file()
    socket = connect(2037)
    while True: 
        
        action = Utils.exploration(state, matrix)
        state, reward = get_state_reward(socket, action) 
        platform = (int(state[:-2], 2)) # -> last_state para atualizar o valor na plataforma que estava antes da ultima action
        direction = Constants.DIRECTION[str(state[-2:])]
        Utils.reward(reward, state, matrix, action, last_state) # -> A recompensa recebida sendo aplicada no estado/platforme anterior ao atual
        last_state = state  # -> last_state para atualizar o valor na plataforma que estava antes da ultima action
        
        print('action -> ', action)
        print('New platform is -> ' + str(platform))
        print('Direction is -> ' + direction)
        print('Reward from LAST platform+action is -> ' + str(reward))
        print(state[-2:])
        print(' ')

    """
    NEXT STEPS:

    1- Escolher a ação a ser feita (se valores todos iguais, escolhe uma randomly) V
    2- executar a ação V
    3 - Atualizar o valor da coombinação [(estado = plataforma + direção) + ação] ANTERIOR.
    3.1 - Formula: (estado,ação) novo = (O valor que já existia) + alpha(arbitrario, talvez menor que 0.5) * [a recompensa retornada no passo 2 + (fator de desconto(arbitrário) * QMAX - (O valor que já existia)]

    3.1.1 Se houver mudança de plataforma o QMAX vai ser o maior valor entre ação/direção da plataforma atual, se não houver mudança de plataforma ler os melhores apenas do novo estado
    cada estado é uma linha em resultado
    """
