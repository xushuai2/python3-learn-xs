#coding=utf-8

'''
Created on 2019年4月23日

@author: 大懒和小懒
'''
from functools import reduce
from multiprocessing import Pool
from collections import Counter


file_name = 'D://log.txt';
def read_inputs(file):
    for line in file:
        line = line.strip()
        yield line.split()

def count():
    file = open(file_name,'rb')
    lines = read_inputs(file)
    c = Counter()
    for words in lines:
        for word in words:
            c[word] += 1
    return c

def do_task():
    job_list = ['D://log.txt'] * 10000
    pool = Pool(8)
    return reduce(lambda x, y: x+y, pool.map(count(), job_list))

if __name__ == "__main__":
    rv = do_task()
