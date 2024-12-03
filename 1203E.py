'''
3274. 棋盘格颜色是否相同
'''
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x = [0, 0, 0]
        y = [0 ,0, 0]
        x[1]  = ord(coordinate1[0]) - 96
        y[1] = int(coordinate1[1])

        x[2] = ord(coordinate2[0]) - 96
        y[2] = int(coordinate2[1])

        c = [1, 1, 1]
        i = 2
        while i > 0:      
            if x[i] % 2 != 0:
                if y[i] % 2 != 0:
                    # 奇数行奇数列 黑色
                        c[i] = 0
            else:
                if y[i] % 2 == 0:
                    # 偶数行偶数列 黑色
                    c[i] = 0 
            i -= 1
        return c[1] == c[2]
#############################################
"""
官方题解：
由于棋盘上的黑白格是间隔排列的，因此：
当行数变化 1 时，格子的颜色会发生变化；
当列数变化 1 时，格子的颜色会发生变化。
因此，如果两个格子之间行数的差值，与列数的差值，二者的和为偶数，就说明它们的颜色相同，否则颜色不同。
"""
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (ord(coordinate1[0]) - ord(coordinate2[0]) + ord(coordinate1[1]) - ord(coordinate2[1])) % 2 == 0



