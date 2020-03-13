class Solution:

    def validPalindrome(self, s: str) -> bool:
        '''
        给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
        双指针的解法
        :param s: 输入的字符串
        :return: 是否boolean值
        '''

        i = 0
        j = len(s) - 1
        if s == s[::-1]:
            return True
        while (i <= j):
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                s1 = s[i:j]
                s2 = s[i + 1:j + 1]
                if (s1 == s1[::-1]) or (s2 == s2[::-1]):
                    return True
                else:
                    return False


s = Solution()
A = "abc"
gcd = s.validPalindrome(A)
print(gcd)

