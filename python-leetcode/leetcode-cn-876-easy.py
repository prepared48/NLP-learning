
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

A = [1,2,3,4,5,6]
s = Solution()
gcd = s.middleNode(A)
print(str(gcd))

