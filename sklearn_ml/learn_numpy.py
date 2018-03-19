# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:37:30 2018

@author: ZTY
"""
#np.fromfunction
#Broadcasting有点复杂
#from _future_ import division, print_function, unicode_literals
import numpy as np
#print(np.zeros(5))
#print(np.zeros((3,4)))
#In NumPy, each dimension is called an axis
#The number of axes is called the rank
#a =np.zeros((3,4))
#print(a.shape)
#print(a.ndim)
#print(a.size)
#print(type(np.zeros((3,4))))
#NumPy arrays have the type ndarrays:
#print(np.ones((3,4)))

#print(np.full((3,4),np.pi))
#print(np.empty((2,3)))
#An uninitialized 2x3 array (its content is not predictable, as it is whatever is in memory at that point)
#a = np.array([[1,2,3,4],[10,20,30,40]])
#a = np.arange(1,5)
#a = np.arange(1.,5)
#it is generally preferable to use the linspace function instead of arange when working with floats. 
#a = np.arange(1,5,0.5)
#np.rand 0~1

#a = np.linspace(0,5/3,6)
#a = np.random.rand(3,4)
#np.randn() univariate normal distribution
#a = np.random.randn(3,4)
#print(a)

#c = np.arange(1.,5)
#print(c.dtype, c)

#d = np.arange(1,5,dtype=np.complex64)
#print(d.dtype,d)

#e = np.arange(1,5,dtype=np.complex64)
#print(e.itemsize)

#g = np.arange(24)
##print(g)
##print("Rank:", g.ndim)
##g.shape = (6,4)
#g.shape = (2,3,4)
##print(g)
##print("Rank:",g.ndim)
##
#g2 = g.reshape(4,6)
##print(g2)
##print("Rank:", g2.ndim)
#g2[1,2] = 999
##print(g2)
##print(g)
#g.ravel()
#print(g)

#All the usual arithmetic operators (+, -, *, /, //, **, etc.) can be used with ndarrays. They apply elementwise:

#// 表示整数除法
#**幂乘

#Broadcasting
#In general, when NumPy expects arrays of the same shape but finds that this is not the case, it applies the so-called broadcasting rules:
#h = np.arange(5).reshape(1,1,5)
#h = h+[10,20,30,40,50]
#print(h)
a = [[100,200,300]]
b = [100,200,300]
print(a)
print(b)
























