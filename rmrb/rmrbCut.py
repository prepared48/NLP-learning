#coding=utf-8

import jieba
import jieba.posseg as pseg
import jieba.analyse as anls
import numpy as np

import  os,time

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
                    # 分词,先去除空格
                    filecontext = filecontext.strip("\n").replace(" ", "")
                    seg_list = jieba.lcut_for_search(filecontext)
                    corpus += seg_list
                    #print(seg_list)
                    #print("[精确模式]：" + "/".join(seg_list))
            elif os.path.isdir(path):
                TraversalFun.AllFiles(self, path)
        return corpus


#构造词典，统计每个词的频率
def build_dict(corpus):
    pass


if __name__ == "__main__":
    startTime = time.time()
    tra = TraversalFun("./1946年05月")
    corpus = tra.TraversalDir()
    print("数据集大小，size: " + str(len(corpus)))
    #print(corpus)
    build_dict(corpus)
    endTime = time.time()
    print("total cost time(s)", (endTime-startTime), 's')