#coding=utf-8

'''
Created on 2019��4��23��

@author: ������С��
'''


# 原文本:
#  ['阿萨德西安市', '', '按顺序擦德西擦', '', '德西', '德西德西']
# 
# 各单词出现的次数：
#  Counter({'': 2, '阿萨德西安市': 1, '按顺序擦德西擦': 1, '德西': 1, '德西德西': 1})
# 0


a = [1,4,2,3,2,3,4,2]  
from collections import Counter  
print(Counter(a)  )


line = 'Row, row, row your boat'

num = line.count('row')
print(num)


import collections
import os
 
with open('D://log.txt','r', encoding='UTF-8') as file1:#打开文本文件
    str1=file1.read().split(' ')#将文章按照空格划分开
 
print("原文本:\n %s"% str1)
print("\n各单词出现的次数：\n %s" % collections.Counter(str1))
print(collections.Counter(str1)['a'])#以字典的形式存储，每个字符对应的键值就是在文本中出现的次数
 