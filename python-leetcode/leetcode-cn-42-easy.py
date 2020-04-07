from typing import List
import math
import numpy as np


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        暴力法优化而来，时间复杂度O(N^2)==>超出时间限制
        循环起点，循环终点
        :param nums:
        :return:
        '''

        smax = -math.inf
        for l in range(len(nums)):
            s = 0
            for r in range(l, len(nums)):
                s = s + nums[r]
                smax = max(s, smax)
        return smax

    def maxSubArray1(self, nums: List[int]) -> int:
        return self.maxSubArrayCommon(nums, 0, len(nums)-1)

    def maxSubArrayCommon(self, nums: List[int], low, high) -> int:
        '''
        分而治之
        :param nums:
        :return:
        '''
        if low == high:
            return nums[low]
        mid = (low + high) // 2
        S1 = self.maxSubArrayCommon(nums, low, mid)
        S2 = self.maxSubArrayCommon(nums, mid+1, high)
        S3 = self.crossSubArray(nums, low, mid, high)
        S = max(S1, S2, S3)
        return S

    def crossSubArray(self, nums: List[int], low, mid, high):
        sleft = -math.inf
        s = 0
        for i in range(mid, low-1, -1):
            s += nums[i]
            sleft = max(sleft, s)
        sright = -math.inf
        s = 0
        for j in range(mid+1, high+1):
            s += nums[j]
            sright = max(sright, s)
        return sleft + sright

    def maxSubArray2(self, nums: List[int]) -> int:
        '''
        动态规划解法
        :param nums:
        :return:
        '''
        d = np.zeros(len(nums))
        rec = np.zeros(len(nums))
        for i in range(0, len(nums)):
            d[i] = nums[i]
            rec[i] = i

        for i in range(len(nums)-2, -1, -1):
            if d[i+1] > 0:
                d[i] = nums[i] + d[i+1]
                rec[i] = rec[i+1]
            else:
                d[i] = nums[i]
                rec[i] = i
        # 找最大
        smax = -math.inf
        for i in range(0, len(nums)):
            if d[i] > smax:
                smax = d[i]
        return int(smax)

# s = Solution()
# # A = [-2,1,-3,4,-1,2,1,-5,4]
# A = [1,2]
# gcd = s.maxSubArray2(A)
# print(gcd)

# a = max(1, -math.inf)
# print(a)

# for i in range(10, 0, -1):
#     print(i)

A = []
for i in range(0, 10) :
    A[i] = i