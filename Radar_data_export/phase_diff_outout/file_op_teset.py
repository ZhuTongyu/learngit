# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 14:57:22 2018

@author: TongYu
"""

import os
#path = r'C:\ZTY\MRR20_data_export\learn_dir_op' # r raw string
path = r'C:\ZTY\MRR20_data_export\New_export_py\3\-10\MRR20\20180408\Rotary Test' # r raw string
#path = r'path = r'C:\ZTY\MRR20_data_export\New_export_py\3'  # r raw string
f_list = os.listdir(path)
print((f_list[0][5:8]=='000'))  # && ==.hyd  break