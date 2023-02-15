from utils.utils import Utils
from utils.connection import connect

#Aqui vocês irão colocar seu algoritmo de aprendizado
if __name__ == '__main__':
    matrix = Utils.get_matrix_from_file()
    matrix[0].jump = 0.0
    Utils.write_matrix_to_file(matrix)
