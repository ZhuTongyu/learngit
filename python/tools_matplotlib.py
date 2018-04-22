# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 12:47:10 2018

@author: ZTY
"""

import matplotlib.pyplot as plt
import numpy as np

# 1
#plt.plot([-3,-2,5,0],[1,6,4,3])  # plot(x,y)
#plt.axis([-4,6,0,7]) # 调整坐标轴范围[xmin,xmax,ymin,ymax]
#plt.show()

# 2
#x = np.linspace(-2,2,500)
#y = x**2

#plt.plot(x,y)
#plt.show()

# add a title, and x and y labels, and draw a grid
#plt.plot(x,y)
#plt.title("Square function")
#plt.xlabel("x")
#plt.ylabel("y = x**2")
#plt.grid(True)
#plt.show()

# 3 line style and color//By default, matplotlib draws a line between consecutive points.
# You can pass a 3rd argument to change the line's style and color. 
#For example "g--" means "green dashed line".
#plt.plot([0, 100, 100, 0, 0, 100, 50, 0, 100], [0, 0, 100, 100, 0, 100, 130, 100, 0],"g--")
#plt.axis([-10, 110, -10, 140])
#plt.show()

# You can plot multiple lines on one graph very simply:
# just pass x1, y1, [style1], x2, y2, [style2], ...
#plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], "r-", [0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
#plt.axis([-10, 110, -10, 140])
#plt.show()
# Or simply call plot multiple times before calling show.
#plt.plot([0, 100, 100, 0, 0], [0, 0, 100, 100, 0], 'r-')
#plt.plot([0, 100, 50, 0, 100], [0, 100, 130, 100, 0], "g--")
#plt.axis([-10, 110, -10, 140])
#plt.show()

# green dashes 'g--'; red dotted 'r:'; blue triangles 'b^'
#x = np.linspace(-1.4,1.4,30)


# 4 plot function returns Line2D objects. You can set extra attributes
# line width ,dash style, alpha level
#x = np.linspace(-1.4, 1.4, 30)
#line1, line2, line3 = plt.plot(x, x, 'g--', x, x**2, 'r:', x, x**3, 'b^')
#line1.linewideth(3.0)
#plt.setp(line1)
##line1 = plt.plot(x, x, 'g--')
#line1.set_linewidth(3.0)
#line1.set_dash_capstyle("round")
#line3.set_alpha(0.1)
#
#plt.show()

# 5 Pyplot's state machine: implicit vs explicit

x = np.linspace(-2,2,200)
# figure object, 坐标轴（个数取决于子图的个数）
fig1, (ax_top, ax_bottom) = plt.subplots(2,1) # sharex 共享x轴
ax_top.tick_params(direction='in')
ax_bottom.tick_params(direction='in')
major_ticks_x = np.arange(-2,2.3,0.5)
minor_ticks_x = np.arange(-2,2.3,0.1)
major_ticks_y = np.arange(-1,1.1,0.5)
minor_ticks_y = np.arange(-1,1.1,0.1)

ax_top.set_xticks(major_ticks_x)
ax_top.set_xticks(minor_ticks_x,minor=True)
ax_top.set_yticks(major_ticks_y)
ax_top.set_yticks(minor_ticks_y,minor=True)

ax_top.grid(which='minor', alpha=0.2)
ax_top.grid(which='major', alpha=0.5)

#fig1, (ax_top, ax_bottom) = plt.subplot(2,1, sharex=True)
fig1.set_size_inches(10,5) #设置图的大小
line1, line2 = ax_top.plot(x, np.sin(3*x**2),"r-",x,np.cos(5*x**2),"b-")
line3, = ax_bottom.plot(x,np.sin(3*x),"r-")
ax_top.grid(True,linestyle='--',which='both')
#ax.grid(color='r', linestyle='-', linewidth=2)
#Axes.grid(b=None, which='major', axis='both', **kwargs)
fig2,ax = plt.subplots(1,1)
ax.grid(True,linestyle='--',which='both')
ax.plot(x,x**2)
plt.show()
 




























