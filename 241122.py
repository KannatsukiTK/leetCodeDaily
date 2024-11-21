#3248.矩阵中的蛇
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = j = 0
        for step in commands:
            # if step == 'UP': i -= 1
            # if step == 'RIGHT': j += 1
            # if step == 'DOWN': i += 1
            # if step == 'LEFT': j -= 1
            match step[0]:
                case'U': 
                    i -= 1
                case'R': 
                    j += 1
                case'D': 
                    i += 1
                case'L': 
                    j -= 1
        
        return i * n + j


        