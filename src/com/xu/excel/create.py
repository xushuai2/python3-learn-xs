#coding=utf-8

'''
Created on 2019年4月7日

@author: 大懒和小懒
'''


import openpyxl
 
# 新建一个空excel，表名为sheet，文件名为test
wb = openpyxl.Workbook()  # 创建新的excel文件，一个工作簿(workbook)在创建的时候同时至少也新建了一张工作表(worksheet)
wb.save('E:\\pythonWorkspace\\test.xlsx')

print('-------------------creatsed')
