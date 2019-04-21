import urllib

# 网络上图片的地址
img_src = 'https://img-my.csdn.net/uploads/201212/25/1356422284_1112.jpg'

# 将远程数据下载到本地，第二个参数就是要保存到本地的文件名
urllib.urlretrieve(img_src,'D:/1.jpg')
