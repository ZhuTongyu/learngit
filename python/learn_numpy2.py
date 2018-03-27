# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:52:13 2018

@author: TongYu
"""
#from _future_ import division, print_function, unicode_literals

#import numpy as np
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

#b = np.arange(48).reshape(4,12)
#print(b)
#print(b[1,:])
#print(b[1:2,:])
#print(b[(0,2),2:5]) # rows 0 and 2,
#print(b[0:2,2:5]) # rows 0 to 2, !!!
#print(b[:,(-1,2,-1)])
#print(b[(-1, 2, -1, 2), (5, 9, 1, 9)] )
#rows_on = np.array([True,False,True,False])
#cols_on = np.array([False,True,False]*4)
##print(b[rows_on,cols_on])
#print(b[np.ix_(rows_on,cols_on)])
#r = np.arange(24).reshape(6,4)
#print(r)
#t = np.arange(24).reshape(4,2,3)
#print(t)
#n1.dot(n2)
#Caution: as mentionned previously, n1*n2 is not a dot product, it is an elementwise product.
import numpy as np
#m3 = np.array([[1,2,3],[5,7,11],[21,29,31]])
#m2 = np.array([[1,0,0],[0,2,0],[0,0,3]])
#print(m3)
#print(np.linalg.inv(m3))
#print(np.linalg.pinv(m3))
#print(m3.dot(np.linalg.pinv(m3))) # identity matrix 单位矩阵
#print(np.eye(3))
#q,r = np.linalg.qr(m2)
#print(q)
#print(r)
#print(q.dot(r))
#print(np.linalg.det(m2))
#eigenvalues, eigenvectors = np.linalg.eig(m3)
#print(eigenvalues)
#print(eigenvectors)

#print(m3.dot(eigenvectors)-eigenvalues*eigenvectors)

#m4 = np.array([[1,0,0,0,2],[0,0,3,0,0],[0,0,0,0,0],[0,2,0,0,0]])
#U, S_diag, V = np.linalg.svd(m4)
#print(U)
#print(S_diag)
#print(V)
#a =np.empty((3,1))
#print(a)
#
#x_coords = np.arange(0,1024)
#y_coords = np.arange(0,768)
#x, y = np.meshgrid(x_coords,y_coords)

a = np.random.rand(2,3)
#np.save("my_array",a)
#with open("my_array.npy","rb") as f:
#    content = f.read()
##print(content)
#a_load = np.load("my_array.npy")
#print(a_load)

#np.savetxt("my_array.csv",a)
#
#with open("my_array.csv","rt") as f:
#    print(f.read())

np.savetxt("my_array1.csv",a ,delimiter=",")
a_loaded = np.loadtxt("my_array.csv",delimiter=",")

