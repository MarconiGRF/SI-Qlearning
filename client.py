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

    """
    NEXT STEPS:

    1- Escolher a ação a ser feita (se valores todos iguais, escolhe uma randomly)
    2- executar a ação
    3 - Atualizar o valor da coombinação [(estado = plataforma + direção) + ação] ANTERIOR.
    3.1 - Formula: (estado,ação) novo = (O valor que já existia) + alpha(arbitrario, talvez menor que 0.5) * [a recompensa retornada no passo 2 + (fator de desconto(arbitrário) * QMAX - (O valor que já existia)]

    3.1.1 Se houver mudança de plataforma o QMAX vai ser o maior valor entre ação/direção da plataforma atual, se não houver mudança de plataforma ler os melhores apenas do novo estado
    cada estado é uma linha em resultado
    """
