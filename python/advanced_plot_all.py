# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:00:53 2018

@author: TongYu
"""

import numpy as np
import matplotlib.pyplot as plt
paras = np.array([[0.09778	,-5.1238],
                  [0.09688	,-3.13],
                  [0.096666,-1.12056],
                  [0.097038,1.138909],
                  [0.09684,3.25449529],
                  [0.09625,5.41605],
                  [0.098	,7.5131]])
my_matrix = np.loadtxt(open("scatter_data.csv","rb"),delimiter=",",skiprows=0)

fig1, ax = plt.subplots(1,1)
ax.tick_params(which='both',direction='in')
major_ticks_x = np.arange(-60,70,10)
minor_ticks_x = np.arange(-60,64,2)
major_ticks_y = np.arange(-15,16,5)
minor_ticks_y = np.arange(-15,16,1)

ax.set_xticks(major_ticks_x)
ax.set_xticks(minor_ticks_x,minor=True)
ax.set_yticks(major_ticks_y)
ax.set_yticks(minor_ticks_y,minor=True)
ax.grid(True,linestyle='--',which='both')
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)
x1 = np.arange(-60,60,0.1)
x = np.arange(-55,58,5)
seq = ['y','m','r','g','k','c','b']
plt.axis([-60,60,-15,15])
for i,color in enumerate(seq):
    
#    plt.figure(1)
    y0 = paras[i][0]*x1+paras[i][1]
    ax.plot(x1,y0,c=color,linestyle='--')
#    plt.plot(x1,y0,c=color,linestyle='--')
    ax.scatter(x,my_matrix[:,i],color=color)


plt.show()



#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)

#x1 = np.arange(-58,58,0.1)
#x = np.arange(-55,58,5)
#plt.rc('xtick', labelsize=10) # x轴 大小
#plt.rc('ytick', labelsize=10) # y轴 大小
#plt.rcParams.update({'font.size': 14})
plt.title('Relationship between phase_diff and velocity')

#seq = ['y','m','r','g','k','c','b']
#for i,color in enumerate(seq):
#    
#    plt.figure(1)
#    y0 = paras[i][0]*x1+paras[i][1]
#    plt.plot(x1,y0,c=color,linestyle='--')
#    plt.scatter(x,my_matrix[:,i],color=color)
#

#major_ticks = np.arange(-60,60,32)
#minor_ticks = np.arange(-60,60,5)
#major_ticks_y = np.arange(-10,10,10)
#minor_ticks_y = np.arange(-10,10,3.14)
#
#ax.set_xticks(major_ticks)
#ax.set_xticks(minor_ticks, minor=True)
#ax.set_yticks(major_ticks_y)
#ax.set_yticks(minor_ticks_y, minor=True)
#
plt.xlabel('Velocity m/s')
plt.ylabel('Phase_diff rad')
#ax.grid(which='both')
#
#ax.grid(which='minor', alpha=0.2)
#ax.grid(which='major', alpha=0.5)
#
#plt.show()



#

