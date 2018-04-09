# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 13:35:59 2018

@author: TongYu
"""

import os
#path = r'C:\ZTY\MRR20_data_export\learn_dir_op' # r raw string
path = r'C:\ZTY\MRR20_data_export\New_export_py\3' # r raw string
f_list = os.listdir(path)
new_list = list(map(int,f_list))  # list 中 str -> int
#new_list1 = list(map(string,new_list))
#new_list_sort = f_list.sort(reverse = True)
new_list.sort() # sorted() 函数范围一个对象，此函数不返回对象
new_list1 = list(map(str,new_list)) # list 中 int -> str
new_list2 = []  # 初始化list
for filename in new_list1:
    new_list2.append(os.path.join(path,filename)) # list末尾追加元素
#    path_str = os.path.join(path,filename)
#    print(path_str)
for index_,fileIdx in enumerate(new_list2):
    path_sub = r'MRR20\20180408\Rotary Test' # r raw string
    path_dir = bytes(fileIdx+'/'+path_sub, encoding = "utf8")
    f_list_sub = os.listdir(path_dir)
    for i in f_list_sub:
#        print(i[5:8])
#        print(i)
#        print(i[5:8])
#        print(os.path.splitext(i)[1])
        if((i[5:8] == b'000') and (os.path.splitext(i)[1] == b'.hyd')): # split 分离文件名和扩展名
#            print('correct')
            print(fileIdx)
            print(i)
            break
            
        else:
#            print('error') 
            print(i) # else 后要接语句，防止什么都不执行
            
#        print(os.path.splitext(i)[1])
#        print(os.path.splitext(i[1])
#    print((f_list_sub[0][5:8])
#    print((f_list_sub[0][5:8]=='000'))  # && ==.hyd  break
    
#    print(os.path.join(path,filename)) # join must be str or bytes
