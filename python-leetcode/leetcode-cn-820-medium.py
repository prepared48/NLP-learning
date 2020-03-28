from typing import List


# 方法：去重放在set中，碰到单词是另外单词的一部分的话，则删除该单词；最后留下的单词是不能再压缩的单词组合
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])
        return sum(len(word) + 1 for word in good)

A = ["time", "me", "bell"]
s = Solution()
gcd = s.minimumLengthEncoding(A)
print(gcd)
