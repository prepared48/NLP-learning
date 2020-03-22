from typing import List


# 方法1：求最大值，看数组长度，如果最大值 > 数组长度，那么
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = [0] * 80000
        for x in A:
            count[x] += 1
        taken = 0
        ans = 0
        for x in range(80000):
            # 如果x出现超过 1 次
            if count[x] >= 2:
                # 需要移动的数的个数
                taken += count[x] - 1
                # 实际需要移动的次数 每次移动1 所以一个重复的数需要移动 x * (count[x] - 1)
                ans -= x * (count[x] - 1)
            # 如果有没出现过的数
            elif taken > 0 and count[x] == 0:
                # 空余一个位置，可以使一个数移动到这个位置， 也就是x
                taken -= 1
                # 移动次数增加x
                ans += x
        return ans



A = [3,2,1,2,1,7]
s = Solution()
gcd = s.minIncrementForUnique(A)
print(gcd)

