import random
from typing import List
import numpy as np



# 方法1： 排序，取前 k 个
class Solution:
    def quicksort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        # 获取随机索引
        pivot = random.randint(0, size)
        # 交换索引位置数和最后数
        arr[pivot], arr[len(arr)-1] = arr[len(arr)-1], arr[pivot]

        for i in range(0, arr):
            pass




s = Solution()
A = [13,6,10,10,50,75,1,73,41]
gcd = s.quicksort(A)
print(gcd)