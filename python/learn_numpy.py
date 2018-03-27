# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:52:13 2018

@author: TongYu
"""
#from _future_ import division, print_function, unicode_literals

import numpy as np
#print(np.zeros(5))
#print(np.zeros((3,4)))
# some vocabulary 
# dimension: axis
#m = np.array([20,-5,30,40])
#print(m < [15,16,35,36])
#a = np.array([[-2.5,3.1,7],[10,11,12]])
#for func in (a.min, a.max, a.sum, a.prod, a.std, a.var,a.mean):
#    print(func.__name__ , "=",func())
#    print(func.__name__, "=", func())
#a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
#print(a)
#print("mean =", a.mean())

#for func in (a.min, a.max, a.sum, a.prod, a.std, a.var, a.mean):
#    print(func.__name__, "=", func())
#numpy.prod()  连乘
#np.square()
#a = np.array([1,5,3,19,13,7,3])
#print(a[2:5])
#try:
#    a[2:5] = [1,2,3]  # too long
#except ValueError as e:
#    print(e)

#Numpy Differences with regular python arrays

b = np.arange(48).reshape(4,12)
print(b)
#print(b[1,:])
#print(b[1:2,:])
#print(b[(0,2),2:5]) # rows 0 and 2,
print(b[0:2,2:5]) # rows 0 to 2, !!!
print(b[:,(-1,2,-1)])
print(b[(-1, 2, -1, 2), (5, 9, 1, 9)] )










