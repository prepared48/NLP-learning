import numpy as np

# 动态规划问题-除数博弈
# 构造一棵树，除数，选择最下层是爱丽丝操作的层数（偶数层），如果存在则为true，否则为false。
class Solution:
    def divisorGame1(self, N: int) -> bool:
        '''
        神奇的归纳法
        :param N:
        :return:
        '''
        return N%2==0

    def divisorGame2(self, N: int) -> bool:
        '''
        动态规划
        1、统计出所有的解getDivisors
        2、如果当前i的约数存在为False的情况，则当前i为True
        思路有了？怎么实现呢？

        :param N:
        :return:
        '''
        target = [0 for i in range(N+1)]
        target[1] = 0
        if N <= 1:
            return False
        else:
            # 抽到2的赢
            target[2] = 1
            for i in range(3, N+1): # 可选 3 4
                for j in range(1, i//2): # 3--1; 4 ---1,2
                    # 如果j是i的余数，并且target[i-j]==0的话，则当前为真
                    if i % j == 0 and target[i-j] == 0:
                        target[i] = 1
                        break
            return target[N] == 1

    def getDivisors(self, N: int):
        re = np.zeros(N, dtype=int)
        j = 0
        for i in range(1, N+1):
            if N % i == 0:
                re[j] = i
                j += 1
        return re[0:j]

s = Solution()
A = 4
gcd = s.divisorGame2(A)
print(gcd)

