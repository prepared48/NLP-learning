class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s :
            if s == "":
                return ""
            s_freq = dict()
            for i in s:
                if i in s_freq:
                    s_freq[i] += 1
                else:
                    s_freq[i] = 1
            for i in s_freq:
                if s_freq[i] == 1:
                    return i
            return " "
        else :
            return " "



s = Solution()
A = ""
gcd = s.firstUniqChar(A)
print(gcd)

