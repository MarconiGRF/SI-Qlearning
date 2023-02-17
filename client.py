from utils.utils import Utils
from utils.connection import connect, get_state_reward

#Aqui vocês irão colocar seu algoritmo de aprendizado
if __name__ == '__main__':
    matrix = Utils.get_matrix_from_file()
    for element in matrix:
        print(str(element))
