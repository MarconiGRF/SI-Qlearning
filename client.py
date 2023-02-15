from utils.utils import Utils

#Aqui vocês irão colocar seu algoritmo de aprendizado
if __name__ == '__main__':
    matrix = Utils.get_matrix_from_file()
    matrix[0].right = 0.132345
    Utils.write_matrix_to_file(matrix)
