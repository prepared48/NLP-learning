
# 最长公共子序列
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 初始化
        n = len(text1)
        m = len(text2)
        C = [[0]*(m+1) for i in range(0, n+1)]
        # 记录是否相等
        rec = [[""]*(m+1) for i in range(0, n+1)]
        for i in range(0, n):
            C[i][0] = 0
        for j in range(0, m):
            C[0][j] = 0
        # 动态规划
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    C[i][j] = 1 + C[i-1][j-1]
                    rec[i][j] = "LU"
                elif C[i-1][j] >= C[i][j-1]:
                    C[i][j] = C[i-1][j]
                    rec[i][j] = "U"
                else:
                    C[i][j] = C[i][j-1]
                    rec[i][j] = "L"
        return C[n][m], rec

A = "cbaebabacd"
B = "abc"
s = Solution()
gcd,rec = s.longestCommonSubsequence(A, B)
print(gcd)
print(rec)

