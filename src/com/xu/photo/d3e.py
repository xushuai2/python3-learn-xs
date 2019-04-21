#coding=utf-8

'''
Created on 2019��4��6��

@author: ������С��
'''
#ֻ����bs4������ҳ
#���̣߳��ٶ���
#ôô��
 
 
import requests
from bs4 import BeautifulSoup
import os
import os.path
import time
import random
import json
 
headers={'Referer':'http://www.mmjpg.com/',"User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"}
 
with open('proxies.json','r') as f:           #�������ȡ���б�
    proxy_pool = f.readlines()
proxies=json.loads(random.choice(proxy_pool))    #���ѡȡһ������
 
def get_text(url,cont = False,proxies=proxies):            #��ȡ��ҳ��text����content
    r = requests.get(url,headers=headers,proxies=proxies)
    r.encoding = 'utf-8'
    if cont == True:
        h = r.content
    else:
        h = r.text
    return h
  
 
        
def load_one_folder(url):                      #���ص���ϵ�е�����ͼƬ
    folder_text = get_text(url)
    folder_soup = BeautifulSoup(folder_text,'lxml')
    dirname = folder_soup.h2.string
    index = url[24:]                        #��ϵ�е�id
    print ('���ڱ��棺' + index + '��' +  dirname)
    print ('��ַΪ��' + url)
                                 
    if  not os.path.exists(index + '��' +  dirname):       #�ļ�����id+�������ʽ����
        os.mkdir(index + '��' +  dirname)
    else:
        pass
    page_num = folder_soup.find(id='page')
    a =  page_num.find_all('a')
    max=int(a[-2].string)                #��ϵ���µ�ҳ������
    print ('��ϵ��һ����' + str(max) +'��ͼ')
    for i in range(1,max+1):
        img_url = url + '/'+ str(i)             #���쵥��ͼƬ����ַ
        img_text = get_text(img_url)
        s = BeautifulSoup(img_text,'lxml')
        content =s.find_all(id='content')
        for c in content:
            img = c.find('img')
            src = img['src']           # ���������ͼ��ַ
            print ('���ڱ���' + src)
            content = get_text(src,True)   #��ȡͼƬ�������ļ� 
            with open(index + '��' +  dirname + '\\' +src.split('/')[-1],'wb')as f:
                f.write(content)
    print('����'*30)                   #�ָ���
 
 
def main(i=1):                        #����Ϊ��ʼ����ַID��Ĭ��Ϊ1
    base_url = 'http://www.mmjpg.com/mm/'
    try:
        while True:
            folder_url = base_url + str(i)
            load_one_folder(folder_url)
            i += 1
    except:
        with open('i.txt','w') as f:                 #�����ļ��б���ϵ㴦����ַID
            f.write(str(i))
        print ('������ȡ��' + folder_url + '���жϣ��ж�ԭ�����ΪIP���⣬����Ϊ���л�Uers-Agent����Ҳ�����ֶ������������´�����ʱ������жϴ�����ַ������ȡ��')
        proxies=json.loads(random.choice(proxy_pool))       #�������һ������
        print ('����ʹ�ô���Ϊ��' + str(proxies))
        main(i)
 
 
if __name__ == '__main__':
    if 'i.txt' in os.listdir('.'):                #�ڵ�ǰ�ļ�����Ѱ��i.txt�ļ�������еĻ�����ȡ�����ֵ�������ϴη����жϵ���ַ������ȡ
       with open('i.txt','r') as f:
            i = int(f.read())  
            main(i)
    else:                                         #���û�У���ôĬ�ϴӵ�һ����ַ��ʼ
        main()
