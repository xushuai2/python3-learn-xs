#coding=utf-8
from collections import Iterable

print ("xushuai hello yanqiong !")
print (abs(-33));
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x;
print(my_abs(-77))

def fact(n):
    if n==1:
        return 1;
    return fact(n-1)*n


result = fact(5)

print(result)

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
s = set([1,8,2])
print(s)
s.add(4)
print(s)
# 列表生成式
l = list(range(1,10))
print(l)
# 迭代器
isIterator = isinstance(l, Iterable)
# Python内置的sorted()函数就可以对list进行排序：
print(isIterator)
print(s)
ll = sorted(s,key=abs)
print(ll)