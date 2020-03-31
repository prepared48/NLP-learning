from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] < rec2[0] < rec1[2] and rec1[1] < rec2[1] < rec1[3]:
            return True


        # 没解决呢


        pass

s = Solution()
A = [0,0,2,2]
B = [1,1,3,3]
gcd = s.isRectangleOverlap(A, B)
print(gcd)

