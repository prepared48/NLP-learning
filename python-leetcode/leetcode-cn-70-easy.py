import numpy as np

# 动态规划问题-爬楼梯
# 分析：爬上了n阶梯，怎么爬上n+1层。1）直接爬一级阶梯；2）上层阶梯是一级，则可以跨2级，到n+1
# 最后一级是 1 或 2 个台阶，1个台阶的方法是多少种，2个台阶的方法是多少种
# n阶台阶，1 + （f(n-1)）
class Solution:
    def climbStairs1(self, n: int) -> int:
        '''
        暴力破解法
        :param n:
        :return:
        '''
        return self.climb_Stairs(0, n)

    def climbStairs2(self, n: int) -> int:
        '''
        动态规划
        第 ii 阶可以由以下两种方法得到：
        在第 (i-1)(i−1) 阶后向上爬一阶。
        在第 (i-2)(i−2) 阶后向上爬 22 阶。
        :param n:
        :return:
        '''
        dp = np.zeros(n + 1)
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            dp[1] = 1
            dp[2] = 2
            if n == 1:
                return 1
            elif n == 2:
                return 2
            for i in range(3, n + 1):
                dp[i] = dp[i - 2] + dp[i - 1]
            return int(dp[n])

    def climb_Stairs(self, i:int, n:int):
        if (i > n):
            return 0
        if (i == n) :
            return 1
        return self.climb_Stairs(i + 1, n) + self.climb_Stairs(i + 2, n)



s = Solution()
A = 4
gcd = s.climbStairs2(A)
print(gcd)

