# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:18:40 2018

@author: TongYu
"""
#
#import pandas as pd
#data = pd.read_csv("output1.csv",header = False)
import numpy as np
import math
import matplotlib.pyplot as plt
my_matrix = np.loadtxt(open("output1.csv","rb"),delimiter=",",skiprows=0)
for i in range(17):
    for j in range(160):
        if(my_matrix[i][j]==0):
            my_matrix[i][j]=1e-10
            

phase = np.zeros((17,80))
phase_new = np.zeros((17,80))

phase_diff = np.zeros((17,40))
phase_diff_aver = np.zeros((17,4))  # 10帧平均
#power = np.zeros((17,80))
#print(phase[0][24])
#x = math.atan(1)
#print(x)
#print(math.pi/4)
#print(math.atan(5/5))
#print(math.atan2(5,5))
#print(math.atan(770048/(-180224)))
#print(math.atan(-770048/(180224)))
#
#
#
#
#print(math.atan2(770048,-180224))
#print(math.atan2(-770048,180224))
##-180224	770048

#print(math.atan2(my_matrix[15][1],my_matrix[15][0]))
#print(math.atan(my_matrix[15][1]/my_matrix[15][0]))

for i in range(17):
    for j in range(80):
        phase[i][j] = math.atan(my_matrix[i][2*j+1]/my_matrix[i][2*j])
        phase_new[i][j] = math.atan2(my_matrix[i][2*j+1],my_matrix[i][2*j])
#        power[i][j] = 
    
for i in range(17):
    for j in range(10):
        for k in range(4):
            phase_diff[i][4*j+k] = phase_new[i][8*j+k]-phase_new[i][8*j+k+4]


a1 = phase_diff[:,0:40:4]
a2 = phase_diff[:,1:40:4]
a3 = phase_diff[:,2:40:4]
a4 = phase_diff[:,3:40:4]  

b1 = np.mean(a1,axis = 1)
b2 = np.mean(a2,axis = 1)
b3 = np.mean(a3,axis = 1)
b4 = np.mean(a4,axis = 1)  
x = np.arange(-16,17,2)
plt.figure(1)
plt.plot(x,b1,color='g')
plt.figure(1)
plt.plot(x,b2,color='c')
plt.figure(1)
plt.plot(x,b3,color='r')
plt.figure(1)
plt.plot(x,b4,color='y')
plt.show()
#for i in range(17):
#    for j in range(4);:
#        phase_diff_aver[i][j] = phase_diff[][]
##            phase_diff[k][w] = phase[k][w]-phase[k][w+4]