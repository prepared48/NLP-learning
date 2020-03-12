class Solution:
    def rotatedDigits(self, N: int) -> int:
        '''
        0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方；6 和 9 同理
        :param N:
        :return:
        '''
        def rotatedDigits(self, N: int) -> int:
            ans, d = 0, [0] * (N + 1)
            d[: 10] = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
            for i in range(N + 1):
                d[i] = -1 if d[i // 10] == -1 or d[i % 10] == -1 else d[i // 10] | d[i % 10]
                ans += 1 if d[i] == 1 else 0
            return ans


s = Solution()
print(s.rotatedDigits(20))

