# -*- coding: utf-8 -*-
"""lec02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aNsgYH63B7emttHavxa8Ik6hcTwUHX_B
"""

#感性情報処理
#第1回課題

import numpy as np
n=4 #要素数
data = np.array([[9,5],[7,4],[4,2],[6,3]]) #x,yの行列
sum = np.sum(data,axis=0) #x,yの合計
x2 = data[:,0]@data[:,0]
y2 = data[:,1]@data[:,1]
print("平方和")
Sxx=x2-(sum[0]**2/n)
Syy=y2-(sum[1]**2/n)
print("国語(x):",Sxx)
print("英語(y):",Syy)
xy = data[:,0]*data[:,1] #xyの配列
xysum = np.sum(xy,axis=0)
Sxy=xysum-sum[0]*sum[1]/n #偏差積和
print("偏差積和:",Sxy)
print("共分散:",Sxy/(n-1))
print("相関係数:",Sxy/np.sqrt(Sxx*Syy))