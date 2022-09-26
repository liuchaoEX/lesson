'''import jieba,wordcloud
text='刘超，余天，韩建华，王倩，徐双，胡长扬，李少坤，韩湘湘'
str_1=jieba.lcut(text)
str_2=' '.join(str_1)
# print(str_2)
cloud=wordcloud.WordCloud(font_path='C:\Windows\Fonts\SIMYOU.TTF').generate(str_2)
cloud.to_file('D:\\Code\\Python\\ciyun\\test3_cloud.jpg')'''

# 词云图
# wordcloud
# import wordcloud
# 核心：Wordcloud类 gengrate()
# wordcloud.WordCloud()
# 生成英文词云
# text='Love is like a butterfly. It goes where it pleases And it pleases where it goes.'
# cloud=wordcloud.WordCloud(font_path='C:\Windows\Fonts\ITCEDSCR.TTF').generate(text)
# cloud.to_file('D:\\Code\\Python\\ciyun\\test_cloud.jpg')

# 生成中文词云
'''
import jieba,wordcloud,cv2
text='中文分词应该先分词，然后将其使用空格或逗号连接成字符串，在调用函数来生成词云'
str_1=jieba.lcut(text)
str_2=' '.join(str_1)
img=cv2.imread('D:\Code\Python\ciyunsucai\hudie.jpg')
# print(str_2)
cloud=wordcloud.WordCloud(font_path='C:\Windows\Fonts\SIMYOU.TTF',background_color='white',mask=img,height=400).generate(str_2)
cloud.to_file('D:\\Code\\Python\\ciyun\\test2.1_cloud.jpg')
# img2=cv2.imread('D:\\Code\\Python\\ciyun\\test2.1_cloud.jpg')
# cv2.imshow('wordcloud',img2)
'''

import wordcloud,jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
file=open('D:\\Code\\Python\\txt\\红楼梦.txt',encoding='utf-8')
words=file.read()
file.close()
txts=jieba.lcut(words)
# print(txts)
txts=' '.join(txts)
maskPic=np.array(Image.open('D:\Code\Python\ciyunsucai\hudie.jpg'))
params=dict(font_path='C:\Windows\Fonts\SIMYOU.TTF',background_color='white',width=400,height=400,max_words=50,mask=maskPic)
wcloud=wordcloud.WordCloud(**params)
wordPic=wcloud.generate(txts)
wcloud.to_file('D:\\Code\\Python\\ciyun\\test4_cloud.jpg')
plt.imshow(wordPic)
plt.axis('off')
plt.show()


# import jieba,wordcloud
# txt=open('D:\\Code\\Python\\txt\\红楼梦.txt'.encode('GBK').decode('UTF-8')).read()
# str_1=jieba.lcut(txt)
# str_2=' '.join(str_1)
# # print(str_2)
# cloud=wordcloud.WordCloud(font_path='C:\Windows\Fonts\SIMYOU.TTF').generate(str_2)
# cloud.to_file('D:\\Code\\Python\\ciyun\\test4_cloud.jpg')

# 使用云形状
# numpy.ndarray()
# opencv-python
