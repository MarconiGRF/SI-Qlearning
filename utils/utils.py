import os.path
from classes.platform_reward import PlatformReward

class Utils:
    """
    Defines utils for usage on the project, making chore tasks easier.
    """
    def __init__(self) -> None:
        self.matrix = self.get_matrix_from_file()
    
    @staticmethod
    def get_matrix_from_file():
        matrix = []
        with open(os.path.dirname(__file__) + '/../resultado.txt') as text_file:
            lines = text_file.readlines()
            for (index, line) in enumerate(lines):
                values = line.replace('\n', '').split(' ')
                platform = PlatformReward(float(values[0]), float(values[1]), float(values[0]), index + 1)
                matrix.append(platform)

        return matrix

    def write_matrix_to_file(self):
        with open(os.path.dirname(__file__) + '/../resultado.txt') as text_file:
            text_file.truncate(0)
        
        text = ''
        for platform in self.matrix:
            text += str(platform.left) + ' ' + str(platform.right) + ' ' + str(platform.jump) + '\n'
        text += '\n'

        with open(os.path.dirname(__file__) + '/../resultado.txt') as text_file:
            text_file.write(text)

        # 1.  Apagar o arquivo inteiro
        # 2.  Pra cada item da matrix
          # 2.1 Construir a linha da forma -> "platform.left platform.right platform.jump\n"
        # 3.  Concatenar os valores anteriores em uma string
        # 4.  Escrever o resultado no arquivo novamente
        # 5.  Escrever uma linha em branco (97)