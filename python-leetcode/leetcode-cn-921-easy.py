import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''
        调用库
        :param nums:
        :return:
        '''
        nums.sort()
        return nums

    def sortArray1(self, nums: List[int]) -> List[int]:
        '''
        快速排序
        选取标记位
        小于标记的放在标记位的左边，大于的放在标记位的右边
        :param nums:
        :return:
        '''
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid-1)
        self.randomized_quicksort(nums, mid+1, r)

    def randomized_partition(self, nums: List[int], l, r) -> List[int]:
        pivot = r
        i = l - 1
        for j in range(l, r):
            if nums[j] < nums[pivot]:
                i += 1
                # 交换j和i
                nums[j], nums[i] = nums[i], nums[j]
        # 交换标志位
        i += 1
        nums[pivot], nums[i] = nums[i], nums[pivot]
        return i


s = Solution()
A = [5,1,1,2,0,0]
gcd = s.sortArray1(A)
# gcd = s.randomized_partition(A, 1, len(A) - 1)
print(gcd)

