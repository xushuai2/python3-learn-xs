#coding=utf-8

'''
Created on 2019年4月23日

@author: 大懒和小懒
'''




# ('阿萨德西安市', 1)
# ('按顺序擦德西擦', 1)
# ('德西', 1)
# ('德西德西', 1)



import io
import re
class Counter:
     def __init__(self, path):
    # :param path: 文件路径
         self.mapping = dict()
         with io.open(path, encoding="utf-8") as f:
          data = f.read()
          words = [s.lower() for s in re.findall("\w+", data)]
          for word in words:
              self.mapping[word] = self.mapping.get(word, 0) + 1
     def most_common(self, n):
             assert n > 0, "n should be large than 0"
             return sorted(self.mapping.items(), key=lambda item: item[1], reverse=True)[:n]
     
     
if __name__ == '__main__':
 most_common_5 = Counter("D://log.txt").most_common(5)
 for item in most_common_5:
     print(item)