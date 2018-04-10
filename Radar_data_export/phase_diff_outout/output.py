# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:54:52 2018
@author: TongYu
"""
# import sqlite3 也可以读.hyd文件，那为什么还用dll，我为什么还要装32位的python
# MAG没有进行fftshift
# line 85  44  69  127
import numpy as np
import math
#import matplotlib.pyplot as plt
import ctypes
#import tkinter.filedialog
import GetRadarData as grd
import os
output = np.zeros([17,160])

RADAR_MAX_COUNT = 100
RADAR_DATA_MAX_SIZE = 1025*256
Hdll = ctypes.cdll.LoadLibrary('C://ZTY//MRR20_data_export//export_py//SQLite3Hyc.dll')

#path = r'C:\ZTY\MRR20_data_export\learn_dir_op' # r raw string
path = r'C:\ZTY\MRR20_data_export\New_export_py\3' # r raw string
f_list = os.listdir(path)
new_list = list(map(int,f_list))  # list 中 str -> int

new_list.sort() # sorted() 函数范围一个对象，此函数不返回对象
new_list1 = list(map(str,new_list)) # list 中 int -> str
new_list2 = []  # 初始化list
for filename in new_list1:
#   new_list2 = C:\ZTY\MRR20_data_export\New_export_py\3\-16 .. 16
    new_list2.append(os.path.join(path,filename)) # list末尾追加元素 
#   0     C:\ZTY\MRR20_data_export\New_export_py\3\-16 
for index_,fileIdx in enumerate(new_list2):
    path_sub = r'MRR20\20180408\Rotary Test' # r raw string
#    C:\ZTY\MRR20_data_export\New_export_py\3\-16\MRR20\20180408\Rotary Test
    path_dir = bytes(fileIdx+'/'+path_sub, encoding = "utf8") # bytes形式，给计算机看
    path_str = fileIdx+'/'+path_sub  # str格式，给人看
#    print(path_str)
    if(new_list[index_]<0):
        speed_bin = abs(255-math.floor(abs(new_list[index_])/0.13))
    else:
        speed_bin = abs(math.floor(new_list[index_]/0.13))
    f_list_sub = os.listdir(path_dir)  # os.listdir只认byte????
#   一个文件目录下的所有文件  -40~40 degree
#   000_+000_MRR20_20180330 16-27-16.265.hyd
    for dirdata in f_list_sub:
#       两个bool与，可以用and吗？？？？ 之前为什么用np.logical_and??
        if((dirdata[5:8] == b'000') and (os.path.splitext(dirdata)[1] == b'.hyd')): # split 分离文件名和扩展名
#            print('correct')
#            print(fileIdx)
            print(path_dir)
            print(dirdata)
# C:\ZTY\MRR20_data_export\New_export_py\3\-16\MRR20\20180408\Rotary Test\000_+000_MRR20_20180408 16-27-16.265.hyd        
            path_str_all = path_str+'/'+bytes.decode(dirdata) # 转成str格式， bytes是给计算机看的，str是给人看的
#            path_all = bytes(path_dir.decode()+'/'+i, encoding = "utf8")
#            path_all = os.path.join(fileIdx,i)
            path_bytes_all = bytes(path_str_all,encoding = "utf8") # 转成bytes格式，输入给计算机
#            print(path_str_all)
#            print(path_bytes_all)
#            选中文件.hyd
            pStr = ctypes.c_char_p(path_bytes_all)
            ret = Hdll.OpenRadarDataFile(pStr)
            arrayTableNumber = (ctypes.c_long*RADAR_MAX_COUNT)()
            arrayTableDataCount = (ctypes.c_long*RADAR_MAX_COUNT)()
            nArrayCount =(ctypes.c_long*1)()
            nArrayCount[0] = RADAR_MAX_COUNT
            ret = Hdll.GetRadarDataTabelInfo(arrayTableNumber, arrayTableDataCount, nArrayCount)
            fCapTime =(ctypes.c_double*1)()
            iLen = (ctypes.c_long*1)()
            dataBuf = np.array(range(RADAR_DATA_MAX_SIZE), dtype = np.int32)
            flag = 0
#           帧数  10帧是怎么计算出来的？？arrayTableDataCount[0]？？
            for i in range(arrayTableDataCount[0]):
                retHyc = Hdll.GetRadarData(0, i, fCapTime, dataBuf.ctypes.data, iLen)
                FrameData = dataBuf[256:256+(iLen[0]>>2)].byteswap()
                _,Tar,maga,magb,*_ = grd.MRR20_1M(FrameData)
                [TarNum,_] = np.shape(Tar)
                b = np.zeros([1,50])  #用于存储该帧下的满足条件的targets
                j = 0
                
        #        某一帧筛选出的Targets
                for TarIdx in range(TarNum):
        #            print(TarIdx)
                    #1.筛选出来是TarB中的哪一行
                    #2.打印出该行的[2：9]列，8个复数，共16个数，实虚实虚实虚实虚。。。
                    #3.循环10次，打印出10帧的数据
                    # target range_bin = 10; speed_bin = 18
#                    Tar是复数，需要加real吧？？？调试看一下有没有影响
                    if(abs(Tar[TarIdx,0]-14)<3 and abs(Tar[TarIdx,1]-speed_bin)<5):
                        # 存储满足条件targets对应的mag能量图的能量，筛选最大峰值点
                        b[0, j] = magb[int(Tar[TarIdx,0].real),int(Tar[TarIdx,1].real)]
                        j = j + 1
                
        #        print(np.argmax(b))
                pow_max = np.argmax(b)  # 找到最大峰值点
        #        if(pow_max == 0): output这一帧的8个复数都给0？？
                if(b[0,pow_max] == 0):
                    flag = flag+1
        #            count = count+1
                    print(fileIdx)
                    print(i)
                    continue # 调到下一帧
        #            final = Tar[ee,2:10]
        #            for w in range(8):
        #                output[index_,2*w+16*i] = 0.
        #                output[index_,2*w+1+16*i] = 0.
#               找到匹配峰值点
                else:
                    x = np.where((magb == b[0,pow_max]))  # 如果有多个点匹配上了呢？？？果然有bug
            #        print(np.where(magb == b[0,pow_max]))
                    c = x[0]  # 10
                    d = x[1]  # 50
                    c_len = len(x[0])
        
            #       在test.py中验证两个for循环！！！！！****！！！！！！！
                    for k in range(c_len):
                        # 有问题 Tar[:,0]， Tar[:,1]可能不是同一行，存index
                        row_tar = c[k]
                        col_tar = d[k]
                        for q in range(TarNum):
        #                    print(q)
        
                            if(np.logical_and(Tar[q,0].real == row_tar , Tar[q,1].real == col_tar)):
                                if(abs(Tar[q,1]-speed_bin)<5):
                                    final = Tar[q,2:10]
                                    final_new = np.reshape(final,(1,8))
                                    for w in range(8):
        #                                while(flag>0):
                                        output[index_,2*w+16*(i-flag)] = final_new[0,w].real
                                        output[index_,2*w+1+16*(i-flag)] = final_new[0,w].imag
#                        break位置有讲究
                                    break

            break
            
        else:
            print('error') 
            print(dirdata) # else 后要接语句，防止什么都不执行
    # 是放在这里吗？output
    np.savetxt('output1.csv',output,fmt = '%.2f',delimiter=',')
    Hdll.CloseRadarDataFile()