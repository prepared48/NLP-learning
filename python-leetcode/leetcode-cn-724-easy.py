# 724. 寻找数组的中心索引
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1

s = Solution()
A = [-1,-1,-1,0,-1,-1]
a = s.pivotIndex(A)
print(str(a))

