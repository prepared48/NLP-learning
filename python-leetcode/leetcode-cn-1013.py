from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum = 0;
        for i in A:
            print(i)
            sum += i
            print("sum == " + str(sum))
        result = sum % 3
        print("result == " + str(result))
        isFlag = False
        if result == 0:
            isFlag = True
        return isFlag

s = Solution()
A = [0,2,1,-6,6,7,9,-1,2,0,1]
print(type(A))
flag = s.canThreePartsEqualSum(A)
print(flag)