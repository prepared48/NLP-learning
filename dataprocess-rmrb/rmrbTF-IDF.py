#coding=utf-8

import os
import time
from collections import Counter,defaultdict
import math
from collections import defaultdict

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

        r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:：;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'  # 用户也可以在此进行自定义过滤字符
        listdir = os.listdir(rootDir)
        corpus = []
        i = 0
        for file in listdir:
            path = os.path.join(rootDir, file)
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
                    seg_list = jieba.lcut(filecontext, cut_all=True)
                    # corpus[i] = seg_list
                    # print(seg_list)
                    corpus.append(seg_list)
                    #print("[精确模式]：" + "/".join(seg_list))
            elif os.path.isdir(path):
                TraversalFun.AllFiles(self, path)
            i += 1
        # print(corpus)
        return corpus

#构造词典，统计每个词的频率
def calc_tf(corpus):
    #   统计每个词出现的频率
    tf = []
    for doc in corpus:
        tf.append(Counter(doc))
    return tf


def calc_idf(word_freq_dict):
    idf = defaultdict(int)
    i = 0
    for doc in word_freq_dict:
        for word in doc:
            idf[word] += 1
    for word in idf:
        idf[word] = math.log(len(idf)/(idf[word]+1))
    return idf

def gettfidf(doc_id):
    tra = TraversalFun("./1946年05月")
    # calc_idf("./1946年05月")
    corpus = tra.TraversalDir()
    tf = calc_tf(corpus)
    idf = calc_idf(tf)
    if doc_id > len(tf):
        print("超出文件个数")
    else:
        id_tf = tf[doc_id - 1]
        for word in id_tf:
            id_tf[word] = id_tf[word] * idf[word]
        return id_tf

def save(idf_dict, path):
    '''
    保存TF-IDF成文件
    :param idf_dict:
    :param path:
    :return:
    '''
    f = open(path, 'a+')
    # f = os.mknod(path, "a+")
    f.truncate()
    for key in idf_dict.keys():
        f.write(str(key) + " " + str(idf_dict[key]) + "\n")
    f.close()

if __name__ == "__main__":
    startTime = time.time()

    tfidf = gettfidf(1)
    print(tfidf)
    save(tfidf, "./tfidf.txt")
    endTime = time.time()
    print("\ntotal cost time(s)", (endTime-startTime), 's')
