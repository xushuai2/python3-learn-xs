#coding=utf-8

'''
Created on 2018年12月17日

@author: 大懒和小懒
'''
import urllib.request
import re
# 页面获取
def get_html(url):
    file=urllib.request.urlopen(url)
    html=file.read()    #读取全部
    return html.decode('utf-8')




# 图片(目标)的提取
def get_image(html_code):
    # 解释下吧——匹配以src="开头然后接一个或多个任意字符(非贪婪)，以.jpg" width结尾的字符串。比如图中红框内src后 双引号里的链接就是一个匹配的字符串。
    reg = r'src="(.+?\.jpg)" width'#正则表达式
    reg_img = re.compile(reg)#编译一下，运行更快
    # 这个时候如何data的数据类型为bytes，时，就会包这个错误，因为它需要的是字符串。
    imglist = reg_img.findall(html_code)#进行匹配
    x=0
    for img in imglist:
        urllib.request.urlretrieve(img, 'D://logs/qq%s.jpg' %x)
        x+=1
        print(str(x)+'---------'+img)
    
print(u'-------网页图片抓取-------') 
# 交互的添加
print (u'请输入url:') 
# python3将raw_input和input进行了整合，只有input
# 在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
url = input()
# 指定链接抓取
if url:
    pass
else:
    url = 'http://tieba.baidu.com/p/1753935195'
print(u'-------正在获取网页-------') 
html_code = get_html(url)
print(u'-------正在下载图片-------') 
get_image(html_code)
print(u'-------下载成功-------')    
    
    
    
    
    
# dataline=file.readline()    #读取一行内容

# fhandle=open("D://1.html","wb")    #将爬取的网页保存在本地
# fhandle.write(data)
# fhandle.close()
# print('over')
