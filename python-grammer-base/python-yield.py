#coding=utf-8

# 生成斐波那契数列，输入钱N个数
def fab1(max):
    '''
    缺点：返回空，复用性差
    :param max:
    :return:
    '''
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1

def fab2(max):
    re = []
    n, a, b = 0, 0, 1
    re.append(a)
    while n < max:
        a, b = b, a+b
        re.append(a)


fab1(5)
re = fab2(5)
print(re)