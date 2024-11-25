'''
3233. 统计非特殊数字的数量
给你两个 正整数 l 和 r。对于任何数字 x，x 的所有正因数（除了 x 本身）被称为 x 的 真因数。

如果一个数字恰好仅有两个 真因数，则称该数字为 特殊数字。例如：

数字 4 是 特殊数字，因为它的真因数为 1 和 2。
数字 6 不是 特殊数字，因为它的真因数为 1、2 和 3。
返回区间 [l, r] 内 不是 特殊数字 的数字数量
'''
import math
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(math.sqrt(r))
        v = [0] * (n + 1)
        res = r - l + 1
        for i in range(2, n + 1):
            if v[i] == 0:
                if l <= i * i <= r:
                    res -= 1
                for j in range( i * 2, n + 1, i):
                    v[j] = 1
        return res
'''
###注意###
题中的“特殊数字”不是平方数（例：16），
而是质数的平方
=>埃氏筛
'''