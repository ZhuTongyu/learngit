# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:09:41 2018

@author: TongYu
"""

import csv
import matplotlib.pyplot as plt
import numpy as np
#filename = 'C:/ZTY/vehicle_radius/data1.csv'
#with open(filename) as f:
#    reader = csv.DictReader(f)
#    column1 = [row['Speed'] for row in reader]
#    print(column1)
   
#with open(filename) as f:
#    reader = csv.reader(f)
#    column1 = [row[1] for row in reader]
#    print(column1)
#
#x = column1[1]

csvFile = open("data1.csv","r",encoding='UTF-8')
reader = csv.reader(csvFile)
data = []
for item in reader:
#    print(item)
    data.append(item)
   
#print(data)
speed = [row[0] for row in data]

yaw = [row[2] for row in data] # yaw是list 可是里面是字符串
radius = [row[3] for row in data]
#print(speed)
#np.around(yaw,decimals=4)
#y = np.array(yaw)
#z = np.around((float)y,decimals=4)
#data_np = np.array(yaw)
#yaw_new = float(yaw)
#yaw_new = map(float, yaw.split())
yaw_new = list(map(float,yaw))  # python list string convert to list float
yaw_np = np.array(yaw_new)
#print(yaw_new)
#w = float(yaw)
csvFile.close
#y = round(yaw,2)
x = np.arange(850)
plt.scatter(x,yaw_np,c= 'b')