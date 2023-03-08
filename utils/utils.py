import os.path
from classes.platform_reward import PlatformReward
from random import randint
from classes.constants import Constants
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
                platform = PlatformReward(float(values[0]), float(values[1]), float(values[2]), index + 1)#tinha um zero no lugar do 2
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
            
    @staticmethod
    def exploration(state, matrix):
        action = ''
        factor_exploration = randint(0, 10)
        line_specifies = (int(state[:-2], 2) + 1) * 4 - (int(state[-2:]) % 4) # -> definindo a linha que eu quero manipular
        if factor_exploration >= 6:
            for i, line in enumerate(matrix): 
                if i+1 == line_specifies: 
                    action = max(line.left, line.right, line.jump)
                    print(line.left, ' ', line.right, ' ', line.jump)
                    break 
            if action == line.left:
                action = 'left'
                
            elif action == line.right:
                action = 'right'
            
            else:
                action = 'jump'
                    
        else:
            action = Constants.ACTIONS[randint(0, 2)]
        return action
    
    @staticmethod
    def reward(reward: int, state: str, matrix: list, action: str, last_state: str):
        q_max = 0
        line_anterior = (int(last_state[:-2], 2) + 1) * 4 - (int(last_state[-2:]) % 4) #linha que recebe recompensa.
        actualy_platform = int(state[:-2], 2) # Usando a plataforma que ele esta agora.
        actualy_line = (actualy_platform + 1) * 4 - (int(state[-2:]) % 4) #Linha atual  
        for i, line in enumerate(matrix): 
            if i+1 == actualy_line: 
                q_max = max(line.left, line.right, line.jump) #encontrando na matrix
                break
            
        for i, line in enumerate(matrix): 
            if i+1 == line_anterior: 
                if action == 'jump':      
                    line.jump += 0.48 * ((reward + 0.45 * q_max) - line.jump)
                    
                elif action == 'left':   
                    line.left += 0.48 * ((reward + 0.45 * q_max) - line.left)
                    
                elif action == 'right': 
                    line.right += 0.48 * ((reward + 0.45 * q_max) - line.right)
                    
                break
            
        Utils.write_matrix_to_file(matrix)
    #explorar aleatoriamente a princípio, apois algum treinamento começar a levar em consideração a melhor opção.
    #Criar uma função para decrescer o valor das variaveis arbitrarias. 