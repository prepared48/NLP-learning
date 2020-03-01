#coding=utf-8

import os
import time

import jieba
import re
from math import log

# 1、递归读取文件
# 2、读取到文件，文件内容转换成文本，使用jieba进行分词

class TraversalFun():
    '''
    这里使用到python数据处理工具项目中的TraverFiles.py
    项目地址：https://github.com/zhongsb/python-dataProcess-tools.git
    '''

    # 1 初始化
    def __init__(self, rootDir):
        self.rootDir = rootDir

    def TraversalDir(self):
        return TraversalFun.getCorpus(self, self.rootDir)

    def getCorpus(self, rootDir):
        corpus = []
        r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 用户也可以在此进行自定义过滤字符
        for file in os.listdir(rootDir):
            path  = os.path.join(rootDir, file)
            if os.path.isfile(path):
                # 打印文件地址
                #print(os.path.abspath(path))
                # 获取文章内容，fromfile主要用来处理数组 pass
                # filecontext = np.fromfile(os.path.abspath(path))
                with open(os.path.abspath(path), "r", encoding='utf-8') as file:
                    filecontext = file.read();
                    #print(filecontext)
                    # 分词 去掉符号
                    filecontext = re.sub(r1, '', filecontext)
                    filecontext = filecontext.replace("\n", '')
                    filecontext = filecontext.replace(" ", '')
                    seg_list = jieba.lcut_for_search(filecontext)
                    corpus += seg_list
                    #print(seg_list)
                    #print("[精确模式]：" + "/".join(seg_list))
            elif os.path.isdir(path):
                TraversalFun.AllFiles(self, path)
        return corpus


#构造词典，统计每个词的频率，并计算信息熵
def calc_tf(corpus):
    #   统计每个词出现的频率
    word_freq_dict = dict()
    for word in corpus:
        if word not in word_freq_dict:
            word_freq_dict[word] = 1
        word_freq_dict[word] += 1
    # 将这个词典中的词，按照出现次数排序，出现次数越高，排序越靠前
    word_freq_dict = sorted(word_freq_dict.items(), key=lambda x:x[1], reverse=True)
    # 计算TF概率
    word_tf = dict()
    # 信息熵
    shannoEnt = 0.0
    # 按照频率，从高到低，开始遍历，并未每个词构造一个id
    for word, freq in word_freq_dict:
        # 计算p(xi)
        prob = freq / len(corpus)
        word_tf[word] = prob
        shannoEnt -= prob*log(prob, 2)
    print(len(word_freq_dict))
    return word_tf, shannoEnt


if __name__ == "__main__":
    startTime = time.time()
    tra = TraversalFun("./1946年05月")
    corpus = tra.TraversalDir()
    print("数据集大小，size: " + str(len(corpus)))
    #print(corpus)
    word_tf, shannoEnt = calc_tf(corpus)
    print("信息熵：" + str(shannoEnt))
    print("TF: ")
    print(word_tf)
    endTime = time.time()
    print("total cost time(s)", (endTime-startTime), 's')