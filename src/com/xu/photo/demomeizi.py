#coding=utf-8
# 爬取
import requests
import os
import time
from bs4 import BeautifulSoup
import urllib
import ssl

header2s = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'Referer': 'http://www.mzitu.com'
            }

class MeiNv:
    def __init__(self,path):
        self.filePath = path
        self.headers = {"user-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}

    # 发起request请求
    def doRequest(self, url):
        html = requests.get(url, headers = self.headers)
        return html.text
    # 得到图片的信息
    def doSoup(self, content):
        count = 0
        con_soup = BeautifulSoup(content, "lxml")
        a_list = con_soup.find("div", class_="all").find_all('a')
        for item in a_list:
            count+=1;
            if count <= 1:
                continue
            
            if count > 50:
                break
            
            # 连接名字，作为文件夹名字
            title = item.get_text()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"+title)
            temppath = path+"//"+title +"//"
            self.mkdir(title)
            # 取出值中的图片位置
            page = item['href']
            if page in 'https://www.mzitu.com/old/':
                continue
            
            page_html = self.doRequest(page)
#             print(page_html)
            # 匹配图片的数目
            html_soup = BeautifulSoup(page_html,"lxml")
#             print(html_soup.contents)
            
            pagenavidiv = html_soup.find('div', class_='pagenavi')
            print(pagenavidiv)
            max_span = pagenavidiv.find_all('span')[-2].get_text()
#             print('----------------'+max_span)
            for i in range(1,int(max_span)+1):
                time.sleep(1)
                page_url = page + '/' + str(i)
                print('*****************'+page_url)
                # 读取图片的信息
                img_html = self.doRequest(page_url)
                imghtml_soup = BeautifulSoup(img_html, "lxml")
                img_url = imghtml_soup.find('div', class_ = 'main-image').find('img')['src']
                print(img_url)
                name = img_url[-9:-4]
                f=open(temppath+name+".jpg",'wb')
                #如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
                #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
                req = requests.get(url=img_url, headers=header2s)
                f.write(req.content)
                f.close()
                
                
    # 创建目录
    def mkdir(self, path):
        path = path.strip()
        isEXists = os.path.exists(os.path.join("E:\meinv\\", path))
        if not isEXists:
            print (u'创建了一个名为%s的文件夹'%(path))
            os.makedirs(os.path.join(self.filePath, path))
            os.chdir(os.path.join(self.filePath, path))
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def start(self, url):
        content = self.doRequest(url)
        self.doSoup(content)
        print('-------------------------over---------------')

ssl._create_default_https_context=ssl._create_unverified_context
url = "http://www.mzitu.com/all"
path = "E:\\meinv\\"
meinv = MeiNv(path)
meinv.start(url)


