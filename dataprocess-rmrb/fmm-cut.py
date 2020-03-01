#coding=utf-8
import numpy as np

word_prob = {"北京": 0.03, "的": 0.08, "天": 0.005, "气": 0.005, "天气": 0.06, "真": 0.04, "好": 0.05, "真好": 0.04, "啊": 0.01,
             "真好啊": 0.02,
             "今": 0.01, "今天": 0.07, "课程": 0.06, "内容": 0.06, "有": 0.05, "很": 0.03, "很有": 0.04, "意思": 0.06, "有意思": 0.005,
             "课": 0.01,
             "程": 0.005, "经常": 0.08, "意见": 0.08, "意": 0.01, "见": 0.005, "有意见": 0.02, "分歧": 0.04, "分": 0.02, "歧": 0.005}

# N 是字典长度，这里是 word_prob 的长度
# M 是句子的长度，比如：“北京的天气真好啊” 长度为 8 
# 前向最大匹配算法，时间复杂度是 O(N * M * M)
def word_segment(input_str):
    '''
    加了权重的前向最大匹配算法
    :param input_str: 要分词的内容
    :return:
    '''
    str_len = len(input_str)
    seg_score = 0  # 存储当前切分的分数
    best_score = []  # 存储从第一个字符到该字符的最优路径分数
    pre_index = []
    for i in range(str_len):
        best_score.append(0)
        pre_index.append(0)
    graph = []
    best_segment = []
    flag = 0

    for index in range(str_len):
        flag1 = False
        flag2 = False
        for i in range(index + 1):
            seg_str = input_str[i:index + 1]
            # print(seg_str)
            if seg_str in word_prob.keys():  # 如果词典中存在这个短语
                flag1 = True
                seg_score = best_score[i - 1] - np.log(word_prob[seg_str])
            else:
                flag2 = True
                seg_score = best_score[i - 1] - np.log(0.00001)
            # print(seg_score)
            if index == 0:
                best_score[0] = seg_score
            if (flag1 and not flag2) or (not flag1 and flag2):
                best_score[index] = seg_score
            if seg_score <= best_score[index]:
                best_score[index] = seg_score
                if i - 1 < 0:
                    pre_index[index] = i
                else:
                    pre_index[index] = i - 1
    # print(best_score)
    # print(pre_index)
    start = str_len - 1
    while start > 0:
        end = start
        start = pre_index[end]
        if start == 0:
            seg_str = input_str[start:end + 1]
        else:
            seg_str = input_str[start + 1:end + 1]
        best_segment.append(seg_str)
    return best_segment


if __name__ == '__main__':
    print(word_segment("北京的天气真好啊"))
    print(word_segment("今天的课程内容很有意思"))
    print(word_segment("经常有意见分歧"))