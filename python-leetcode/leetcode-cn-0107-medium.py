from typing import List

from numpy import shape


# 旋转90度
class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        1）交换行顺序，最后一行换到第一行，倒数第二行换到第二行，以此类推
        2）交换行列，行换成列，列转成行
        """
        size = shape(matrix)[0]
        for i in range(0, size//2):
            matrix[i], matrix[size-i - 1] = matrix[size-i - 1], matrix[i]
        # arr = list(map(list, zip(*matrix)))
        arr = [[row[i] for row in matrix] for i in range(size)]

        matrix = arr
        print(matrix)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        思路：
        1）行对换，最后一行换到第一行，倒数第二行换到第二行，以此类推
        2）对角线元素对换
        """
        size = shape(matrix)[0]
        for i in range(0, size//2):
            matrix[i], matrix[size-i - 1] = matrix[size-i - 1], matrix[i]
        for i in range(0, size):
            for j in range(1, size):
                if i < j:
                    tem = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tem
                # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)




s = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.rotate(matrix)
# size = 4
#
# b = [size//2+1 if size % 2 == 1 else size//2]
# print(int(b[0]))

# print(gcd)
# print(matrix[:, 0])
# matrix[0], matrix[2] = matrix[2], matrix[0]
# print(matrix)

# arr2 = list(map(list, zip(*matrix)))
# print(arr2)