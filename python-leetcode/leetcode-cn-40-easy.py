from typing import List
import numpy as np



# 方法1： 排序，取前 k 个
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort(reverse=False)
        return arr[0:k]




s = Solution()
A = [1, 1, 3, 3]
gcd = s.getLeastNumbers(A, 2)
print(gcd)