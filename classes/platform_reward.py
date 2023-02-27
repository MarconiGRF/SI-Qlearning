import math
from classes.constants import Constants

class PlatformReward:

    def __init__(self, left_reward, right_reward, jump_reward, file_line):
        self.line = file_line
        self.left = left_reward
        self.right = right_reward
        self.jump = jump_reward
        self.direction = self.determinate_direction()
        self.platform = math.ceil(self.line / 4)

    def determinate_direction(self):
        if (self.line-1) % 4  == 0:
            return Constants.DIRECTION["00"]
        elif (self.line-1) % 4 == 1:
             return Constants.DIRECTION["01"]
        elif (self.line-1) % 4 == 2:
            return Constants.DIRECTION["10"]
        else:
            return Constants.DIRECTION["11"]

    def __str__(self) -> str:
        return 'Line - ' + str(self.line) + ' Left - ' + str(self.left) + ' Right - ' + str(self.right) + ' Jump - ' \
               + str(self.jump)
