class Solution:
    def __init__(self):
        pass

    def reverseLeftWords(self, strings: str, n: int):
        print(strings)
        for i in range(n):

            print("移动" + str(i) + "个字符之前：" + strings)
            strings = strings + strings[0]
            print(type(strings))
            strings = self.removeIndex(strings, 0)
            print("==" + strings)
            strings = str(strings)
            print("移动" + str(i) + "个字符之后：" + strings)

    def removeIndex(self, test_str:str, index:int):

        # 接收移除后的字符串
        new_str = ""
        for i in range(0, len(test_str)):
            if i != index:
                new_str = new_str + test_str[i]
        return new_str


s = Solution()
# test_str = "Runoob"
# s.removeIndex(test_str, 2)
s.reverseLeftWords("abcdefg", 2)