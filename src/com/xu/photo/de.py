#coding=utf-8
'''
Created on 2019��4��6��

@author: ������С��
'''
import urllib.request
import re
import urllib.parse
def crawling():
    req = urllib.request.urlopen('http://www.imooc.com/course/list?c=python')  #������ҳ
    html=req.read().decode("utf-8") #��ȡ����ҳ��html���룬ͬʱ����ת��Ϊutf-8����
    #html=req.read().decode("gbk")
    reg=r'src="(.+?\.jpg)"'  #������ʽ��ƥ�䵱ǰͼƬ���ַ�
    imgre=re.compile(reg)    #����������ʽ������
    imglist=imgre.findall(html)  #��html���ҵ�ƥ�����
    print(imglist)
    print('-----------------------')
    count=1
    for img in imglist:
        img_add=urllib.parse.urljoin(html,img)  #ͨ��������ƥ����ľ��Ե�ַ����Ϊ��ȡ����������λ�ã���Ҫ����ת��
        
        print(img_add)
        
        f=open("D:\\write\\"+str(count)+".jpg",'wb')
#         https://i.meizitu.net/2019/03/14b01.jpg
        img_html=urllib.request.urlopen("http:"+img_add)
#         img_html=urllib.request.urlopen("https://i.meizitu.net/2019/03/14b01.jpg")
        picture=img_html.read()
        f.write(picture)
        f.close()
        count+=1    
crawling()