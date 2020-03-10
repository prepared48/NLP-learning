class Solution:
    def __init__(self):
        pass

    def reverseLeftWords(self, strings: str, n: int):
        return strings[n:len(strings)] + strings[0:n]


s = Solution()
strings = s.reverseLeftWords("abcdefg", 2)
print(strings)