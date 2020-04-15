from typing import List
import numpy as np

# 海洋陆地问题，1是陆地，0是海洋，判断有多少岛屿
# 注意事项：m，n 不要重复计算；dfs函数中，grid[i][j]不能重复和1比较
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        使用深度优先搜索
        :param grid:
        :return:
        '''
        # 获取行列数
        if len(grid) == 0:
            return 0
        m = np.shape(grid)[0]
        n = np.shape(grid)[1]
        numIslands = 0
        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    numIslands += 1
                    self.bfs(grid, i, j, m, n)
                    # i += 1
                    # j += 1
        return numIslands

    def dfs(self, grid: List[List[str]], i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
            return
        # 遍历过的元素都修改为 0
        grid[i][j] = 0
        self.dfs(grid, i-1, j, m, n)
        self.dfs(grid, i, j-1, m, n)
        self.dfs(grid, i+1, j, m, n)
        self.dfs(grid, i, j+1, m, n)


    def bfs(self, grid: List[List[str]], i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
            return
        # 遍历过的元素都修改为 0
        grid[i][j] = 0
        self.bfs(grid, i+1, j, m, n)
        self.bfs(grid, i, j+1, m, n)
        self.bfs(grid, i-1, j, m, n)
        self.bfs(grid, i, j-1, m, n)

# A = [[1,1,1,1,0],
#     [1,1,0,1,0],
#     [1,1,0,0,0],
#     [0,0,0,0,0]]
# A = [["1","1","1","1","0"],
#      ["1","1","0","1","0"],
#      ["1","1","0","0","0"],
#      ["0","0","0","0","0"]]
# A = [["1","1","1"],
#      ["0","1","0"],
#      ["1","1","1"]]
# A = [["1","1","0","0","0"],
#      ["1","1","0","0","0"],
#      ["0","0","1","0","0"],
#      ["0","0","0","1","1"]]
A = [["1","1","1"],
     ["0","1","0"],
     ["1","1","1"]]
s = Solution()

gcd = s.numIslands(A)
print(gcd)

