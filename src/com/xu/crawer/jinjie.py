#coding=utf-8

'''
Created on 2018年12月18日

@author: 大懒和小懒
'''
import os
import urllib.request
import re
import requests
from lxml import etree

# 通过url获取每个帖子链接
def getArticleLinks(url):
    html = requests.get(url)
    Selector = etree.HTML(html.text)
    # 通过Xpath 获取每个帖子的url后缀
    url_list = Selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
    # 在每个后缀前加上百度贴吧的url前缀
    for i in range(len(url_list)):
        url_list[i] = 'https://tieba.baidu.com' + url_list[i]
        print(url_list[i])
    return url_list

# 通过所给帖子链接，下载帖子中所有图片
def get_img(url):
    print('get_img(url)  url='+url)
    html = requests.get(url)
    Selector = etree.HTML(html.text)
    img_url_list = Selector.xpath('//img[@class="BDE_Image"]/@src')
    pic_name = 0
    print('---------------------')
    for each in img_url_list:
        print(each)
        urllib.request.urlretrieve(each, 'pic_%s.jpg' % pic_name)
        pic_name += 1

# 为每个帖子创建独立文件夹，并下载图片
def download_img(url_list,page):
    # 该目录下创建一个downloads文件夹存放下载图片
    if not os.path.exists('downloads'):
        os.mkdir('downloads')
    root_path = os.getcwd()
    print('root_path='+root_path)
    for i in range(page):
        img_dir = 'downloads/' + url_list[i][23:].replace("/", '')
        if not os.path.exists(img_dir):
            os.mkdir(img_dir)
        os.chdir(img_dir)
        get_img(url_list[i])
        os.chdir(root_path)

if __name__ == '__main__':
    print(u'-----贴吧图片爬取装置2.0-----') 
    print (u'请输入贴吧地址：')
    targetUrl = input('')
    if not targetUrl:
        print(u'---没有地址输入正在使用默认地址(baidu壁纸吧)---') 
        targetUrl = 'http://tieba.baidu.com/f?kw=%E5%A3%81%E7%BA%B8&ie=utf-8'
  
    page = ''
    while True:
        print(u'请输入你要下载的帖子数：') 
        page = input('')
        if re.findall(r'^[0-9]*[1-9][0-9]*$',page):
            page = int(page)
            break
    print(u'----------正在下载图片---------') 
    ArticleLinks = getArticleLinks(targetUrl)
    download_img(ArticleLinks,page)
    print(u'-----------下载成功-----------') 
    input('Press Enter to exit')

#     html = requests.get('https://tieba.baidu.com/p/5982266980')
#     Selector = etree.HTML(html.text)
#     img_url_list = Selector.xpath('//img[@class="BDE_Image"]/@src')
#     print('---------------------')
#     pic_name = 0
#     os.chdir('downloads/p4357276836')
#     for each in img_url_list:
#         print(each)
#         urllib.request.urlretrieve(each, 'pic_%s.jpg' % pic_name)
#         pic_name += 1


