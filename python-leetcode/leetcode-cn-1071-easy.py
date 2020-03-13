
class Solution:
    def gcdOfStrings(self, str1: str, str2: str):
        if len(str1) < len(str2):
            strtem = str1
            str1 = str2
            str2 = strtem
        lastLen1 = len(str1)
        lastLen2 = len(str2)
        if str1[0: len(str2)] != str2:
            return ""
        str1 = str1.replace(str2, "")
        if str1 == '':
            return str2
        else:
            if len(str1) == lastLen1 | len(str1) > lastLen2:
                return ""
            else:
                print("str2: " + str2 + "\nstr1: " + str1)
                return self.gcdOfStrings(str2, str1)



A = "TAUXXTAUXXTAUXXTAUXXTAUXX"
B = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
s = Solution()
gcd = s.gcdOfStrings(A, B)
print(gcd)

