#coding=utf-8


# 计算一个句子有多少分词候选

def cut_num(input_str_len):
    '''
    :param input_str_len: 句子长度
    :return:
    '''

    if(input_str_len == 1):
        return 1
    elif(input_str_len == 2):
        return 2
    else:
        return 2 * cut_num(input_str_len-1)

print(str(cut_num(4)))