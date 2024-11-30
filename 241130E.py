'''
3232, 是否能完成数字游戏
Alice 和 Bob 正在玩游戏。在游戏中，Alice 可以从 nums 中选择所有个位数 或 所有两位数，
剩余的数字归 Bob 所有。如果 Alice 所选数字之和 严格大于 Bob 的数字之和，则 Alice 获胜。

如果 Alice 能赢得这场游戏，返回 true；否则，返回 false。

思路：个位数之和s1!=两位数之和s2
'''
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        one = 0
        two = 0
        for num in nums:
            if num // 10 == 0:
                one += num
            else:
                two += num
        if one != two:
            return True
        else:
            return False
# 简洁版：转化为s1 - s2
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(x if x < 10 else -x for x in nums) != 0
'''
作者：灵茶山艾府
链接：https://leetcode.cn/problems/find-if-digit-game-can-be-won/solutions/1/jian-ji-xie-fa-pythonjavacgo-by-endlessc-i5b5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''