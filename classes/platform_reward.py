class PlatformReward:

    def __init__(self, left_reward, right_reward, jump_reward, file_line):
        self.line = file_line
        self.left = left_reward
        self.right = right_reward
        self.jump = jump_reward

    def __str__(self) -> str:
        return ('Line - ' + str(self.line) + ' Left - ' + str(self.left) + ' Right - ' + str(self.right) + ' Jump - ' + str(self.jump))
