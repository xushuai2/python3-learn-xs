#coding=utf-8

'''
Created on 2019年4月7日

@author: 大懒和小懒
'''


# Python 截取字符串使用 变量[头下标:尾下标]，就可以截取相应的字符串，其中下标是从0开始算起，可以是正数或负数，下标可以为空表示取到头或尾。
str = '12345678'
print(str[0:1])
print(str[1:6])
# Python 替换字符串使用 变量.replace("被替换的内容"，"替换后的内容"[，次数])，替换次数可以为空，即表示替换所有。
# 要注意的是使用replace替换字符串后仅为临时变量，需重新赋值才能保存。
str = str.replace('23', 'xu')
print(str)

# Python 查找字符串使用 变量.find("要查找的内容"[，开始位置，结束位置])，开始位置和结束位置，
# 表示要查找的范围，为空则表示查找所有。
# 查找到后会返回位置，位置从0开始算，如果没找到则返回-1。  
strxu = 'xushuaishuaiyanqu';
temp = strxu.find('shu')
print(temp)
# 2

# Python 分割字符串使用 变量.split("分割标示符号"[分割次数])，分割次数表示分割最大次数，为空则分割所有。
str = 'a,b,c,d'
strlist = str.split(',')    # 用逗号分割str字符串，并保存到列表
for value in strlist:    # 循环输出列表值
    print(value)