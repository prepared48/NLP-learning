

# 机器人的运动范围
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j, si, sj):
            '''
            深度优先-递归实现
            :param i: 起始位
            :param j: 起始位
            :param si: i的位数和，比如i=19 si=1+9=10
            :param sj: j的位数和，比如j=19 sj=1+9=10
            :return:
            '''
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            print("i=" + str(i) + ", j=" + str(j))
            # 1 为当前位
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) +\
                   dfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount1(self, m: int, n: int, k: int) -> int:
        '''
        深度优先——非递归实现
        :param m:
        :param n:
        :param k:
        :return:
        '''


        return 0

    def movingCount2(self, m: int, n: int, k: int) -> int:
        def bfs(i, j, si, sj):
            '''
            广度优先-递归实现
            :param i: 起始位
            :param j: 起始位
            :param si: i的位数和，比如i=19 si=1+9=10
            :param sj: j的位数和，比如j=19 sj=1+9=10
            :return:
            '''
            if not 0 <= i < m or not 0 <= j < n or k < si + sj or (i, j) in visited:
                return 0
            visited.add((i, j))
            print("i=" + str(i) + ", j=" + str(j))
            # 1 为当前位
            return 1 + bfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + \
                    bfs(i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8) +\
                    bfs(i+1, j + 1, si + 1 if (i + 1) % 10 else si - 8, sj + 1 if (j + 1) % 10 else sj - 8)
        visited = set()
        return bfs(0, 0, 0, 0)

# s = Solution()
# m = 38
# n = 15
# k = 9
# count = s.movingCount2(m, n, k)
# print(count)

a = 1 if 10 % 10 else 1111
print(a)
print(10%10)