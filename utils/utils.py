import os.path
from classes.platform_reward import PlatformReward

class Utils:
    """
    Defines utils for usage on the project, making chore tasks easier.
    """
    
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

    @staticmethod
    def write_matrix_to_file(matrix):
        with open(os.path.dirname(__file__) + '/../resultado.txt', "r+") as text_file:
            text_file.truncate(0)
        
            text = ''
            for platform in matrix:
                text += str(round(platform.left, 6)) + ' ' + str(round(platform.right, 6)) + ' ' + str(round(platform.jump, 6)) + '\n'

            text_file.write(text)
