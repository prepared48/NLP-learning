from typing import List


# 总结：最大子数组，循环，current
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 当前所有数字相加 如果比之前的最大还大 最大就是current
        current = nums[0]
        # 最大
        s = nums[0]
        for i in nums[1:]:
            if current < 0:
                current = i
            else:
                current += i
            if current > s:
                s = current
        return s


s = Solution()
A = [-2,1,-3,4,-1,2,1,-5,4]
# for i in A:
#     print(i)
# print(A[0:len(A)//2])
# print(A[len(A)//2:])
strings = s.maxSubArray(A)
print(strings)