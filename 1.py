# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt#调用matplotlib的库
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50

x = np.linspace(0, 3 * np.pi, 100)#x范围以0到3π，分隔总数为100
y = np.sin(x)#y轴正弦波

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#在画布的第一行第二列显示图片
plt.title(r'$f(x)=sin(x)$') #左侧图像的标题
plt.plot(x, y)#以坐标（x，y）为坐标绘制并显示
#plt.show()

x1 = [t*0.375*np.pi for t in x]#x1范围的设定，从0到3π（3/8）*π
y1 = np.sin(x1)#y1范围设定，为sin（x1）
plt.subplot(1,2,2)#在画布的第一行第二列显示图片
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #右侧图像的标题
plt.plot(x, y1)#绘制图片
plt.show()#输出波形