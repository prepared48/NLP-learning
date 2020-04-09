# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        '''
        递归方法
        :param number:
        :return:
        '''
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        return self.jumpFloor(number - 2) + self.jumpFloor(number - 1)

    def jumpFloor1(self, number):
        '''
        动态规划方法
        :param number:
        :return:
        '''
        # write code here
        if number == 1:
            return 1
        elif number == 2:
            return 2
        pre2 = 1
        pre1 = 2
        pre = 0
        for i in range(3, number+1):
            pre = pre2 + pre1
            pre2 = pre1
            pre1 = pre
            # pre1, pre2 = pre2, pre

        return pre1

s = Solution()
n = s.jumpFloor1(4)
print(n)