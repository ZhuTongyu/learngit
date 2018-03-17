# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 10:08:16 2018

@author: TongYu
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
import math

csvFile = open("LRR10_20180305 14-16-40.299_VehicleInfo.csv","r",encoding='UTF-8')
reader = csv.reader(csvFile)
data = []
for item in reader:
#    print(item)
    data.append(item)
  
#print(data)
speed = [row[0] for row in data]
steerAngle = [row[1] for row in data]
yaw = [row[2] for row in data] # yaw是list 可是里面是字符串
radius = [row[3] for row in data]

speed_new = list(map(float,speed))
yaw_new = list(map(float,yaw))  # python list string convert to list float
steer_new = list(map(float,steerAngle))
radius_new = list(map(float,radius))
speed_np = np.array(speed_new)
yaw_np = np.array(yaw_new)

csvFile.close
#y = round(yaw,2)
x = np.arange(1999)
plt.figure(1)
plt.scatter(x,speed_new,c= 'b')
plt.title('VehicleSpeed',fontsize=14)
plt.xlabel('t',fontsize=16)
plt.ylabel('m/s',fontsize=16)

plt.figure(2)
plt.scatter(x,steer_new,c= 'b')
plt.title('SteerAngle',fontsize=14)
plt.xlabel('t',fontsize=16)
plt.ylabel('Degree°',fontsize=16)

plt.figure(3)
plt.scatter(x,yaw_new,c= 'b')
plt.title('YawRate',fontsize=14)
plt.xlabel('t',fontsize=16)
plt.ylabel('Degree°/s',fontsize=16)

plt.figure(4)
plt.scatter(x,radius_new,c= 'b')
plt.title('TurnRadius',fontsize=14)
plt.xlabel('t',fontsize=16)
plt.ylabel('m',fontsize=16)

turnradius = speed_np/yaw_np*(180/math.pi)

plt.figure(5)
plt.scatter(x,turnradius,c= 'b')
plt.title('TurnRadius',fontsize=14)
plt.xlabel('t',fontsize=16)
plt.ylabel('m',fontsize=16)
