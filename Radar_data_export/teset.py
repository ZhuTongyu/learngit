# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 23:29:31 2018

@author: TongYu
"""

import numpy as np
#xxx = np.arange(16)
xxx = np.array([[1,2,3],[4,3,6],[7,8,9]])
print(xxx)
#a = np.where(xxx<5)
#lll = len(a[0])
#b = np.where(xxx[a]>5)
#ddd = a[0]
#print(ddd)
#print(lll)

ddd = np.where((xxx == 3))
ct = ddd[0]  # 10
dt = ddd[1]  # 50
c_len = len(ct)
d_len = len(dt)
#print(ct[0],dt[0])
#print(ct[1],dt[1])
zz = np.where(np.logical_and(xxx[:,0] == c , xxx[:,1].real == d))

#for k in range(c_len):
#    # 有问题 Tar[:,0]， Tar[:,1]可能不是同一行，存index
#    for q in range(TarNum):
#        zz = np.where(np.logical_and(Tar[q,0].real == c[k] , Tar[q,1].real == d[k]))