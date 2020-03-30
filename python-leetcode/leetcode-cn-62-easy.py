from typing import List
import time
from datetime import timedelta


class Solution:

    def lastRemaining1(self, n: int, m: int) -> int:
        '''
        超出规定的时间限制。时间复杂度为O(N^2)
        :param n:
        :param m:
        :return:
        '''
        list = [i for i in range(n)]
        for i in range(n):
            if len(list) == 1:
                return list[0]
            list = self.getByIndex(list, m)
        return

    def getByIndex(self, list: List, m: int):
        '''
        :param list: 数组 数组长度
        :param m: 找 m 位
        :return: 返回删除该元素的数组
        '''
        if m <= len(list):
            list = list[m:] + list[0:m-1]
        else:
            # 找到m位元素
            # s = list[m%len(list)]
            if m%len(list) != 0:
                list = list[m % len(list):] + list[0:m % len(list)-1]
            else:
                list = list[0:len(list)-1]
        return list

s = Solution()
A = 70866
B = 116922
start_time = time.time()
gcd = s.lastRemaining(A, B)
end_time = time.time()
time_dif = end_time - start_time
print("耗时：" + str(timedelta(seconds=int(round(time_dif)))))
print(gcd)

# for i in range(10):
#     print(i)