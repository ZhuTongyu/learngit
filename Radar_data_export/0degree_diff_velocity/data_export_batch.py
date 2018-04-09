# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:54:52 2018

@author: TongYu
"""
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
    new_list2.append(os.path.join(path,filename)) # list末尾追加元素

for index_,fileIdx in enumerate(new_list2):
    path_sub = r'MRR20\20180408\Rotary Test' # r raw string
    path_dir = bytes(fileIdx+'/'+path_sub, encoding = "utf8")
    path_str = fileIdx+'/'+path_sub
#    print(path_str)
    speed_bin = abs(math.floor(new_list[index_]/0.13))
    f_list_sub = os.listdir(path_dir)
#   一个文件目录下的所有文件 
    for i in f_list_sub:

        if((i[5:8] == b'000') and (os.path.splitext(i)[1] == b'.hyd')): # split 分离文件名和扩展名
#            print('correct')
#            print(fileIdx)
            print(path_dir)
#            print(i)
            path_str_all = path_str+'/'+bytes.decode(i) # bytes是给计算机看的，str是给人看的
#            path_all = bytes(path_dir.decode()+'/'+i, encoding = "utf8")
#            path_all = os.path.join(fileIdx,i)
            path_bytes_all = bytes(path_str_all,encoding = "utf8")
#            print(path_str_all)
#            print(path_bytes_all)
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
#           帧数
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
                    if(abs(Tar[TarIdx,0]-14)<3 and abs(Tar[TarIdx,1]-speed_bin)<3):
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
                    continue
        #            final = Tar[ee,2:10]
        #            for w in range(8):
        #                output[index_,2*w+16*i] = 0.
        #                output[index_,2*w+1+16*i] = 0.
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
                                if(abs(Tar[q,1]-speed_bin)<3):
                                    final = Tar[q,2:10]
                                    final_new = np.reshape(final,(1,8))
                                    for w in range(8):
        #                                while(flag>0):
                                        output[index_,2*w+16*(i-flag)] = final_new[0,w].real
                                        output[index_,2*w+1+16*(i-flag)] = final_new[0,w].imag
                                    break

            break
            
        else:
#            print('error') 
            print(i) # else 后要接语句，防止什么都不执行
    Hdll.CloseRadarDataFile()
