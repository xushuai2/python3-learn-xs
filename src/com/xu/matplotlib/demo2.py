#coding=utf-8

'''
Created on 2018年12月22日

@author: 大懒和小懒
'''
from tkinter import *
# 导入tkinter模块的所有内容

def callback():         # 定义一个 改变文本的函数 . 
    var.set("吹吧你，我才不信呢~")

root = Tk()     # 初始旷的声明 . 

frame1 = Frame(root)   # 在初始旷里面 声明两个模块 . 
frame2 = Frame(root)

# 创建一个文本Label对象
var = StringVar()           #声明可变 变量  . 
var.set("您所下载的影片含有未成年人限制内容，\n请满18岁后再点击观看！") # 设置变量 . 
textLabel = Label(frame1,           # 绑定到模块1
                  textvariable=var,  # textvariable 是文本变量的意思 .  
                  justify=LEFT)    # 字体 位置 
textLabel.pack(side=LEFT)   #  整体位置 

# 创建一个图像Label对象
# 用PhotoImage实例化一个图片对象（支持gif格式的图片）

imgLabel = Label(frame1)
imgLabel.pack(side=RIGHT)

# 加一个按钮
theButton = Button(frame2, text="已满18周岁", command=callback)  # 按下按钮 执行 callback函数
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)

mainloop()