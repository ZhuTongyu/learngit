# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 17:00:55 2018

@author: TongYu
"""

# 最大探测距离
# 最小探测距离
# 距离精度
# 速度范围
# 速度精度
# 角度范围
# 角度精度
# 更新时间
# 宽波  A波  B波
# 窄波  A波  B波
# 最大测速范围 Vmax = lamda/(2*Tchirp)   单个的Tchirp
# A 256   b 256
c = 3*1e8
f = 77*1e9   #实际频率不是这个值，76.424GHz  76.576  76.7115
lamda = c/f

#采样频率
fs = 40*1e6

# 256 A WAVE  256 B WAVE
L = 256  # 发波个数 
N = 512  # 第一次FFT点数 距离维
#N_2 = 128 # 第二次FFT点数 速度维

Tchirp_a = 30*1e-6*2   # A  WAVE
Tchirp_b = 36*1e-6*2   # B  WAVE
Tchirp_up = 19*1e-6  # Tramp  19us
Tchirp_eff = N/fs  #有效发波时间  12.8us

#带宽
#Bw_wide = 423*1e6      #AEB
Bw_narrow = 247*1e6    #ACC 

#Bw_eff_wide = Bw_wide*Tchirp_eff/Tchirp_up      # 有效扫频带宽  
Bw_eff_narrow = Bw_narrow*Tchirp_eff/Tchirp_up

#距离分辨率
#delta_r_wide = c/(2*Bw_eff_wide)
delta_r_narrow = c/(2*Bw_eff_narrow)

#最大不模糊速度
Vmax_a = lamda/(2*Tchirp_a)  
Vmax_b = lamda/(2*Tchirp_b)

Vmax_a_both = Vmax_a/2  # 速度有正负之分
Vmax_b_both = Vmax_b/2

# 速度分辨率
delta_v_a = Vmax_a/L
delta_v_b = Vmax_b/L
#速度精度
V_acc_a = 0.5*delta_v_a
V_acc_b = 0.5*delta_v_b
#速度分离度
V_sep_a = 2*delta_v_a
V_sep_b = 2*delta_v_b
#发波总时间
Tchirp_all_a = L*Tchirp_a
Tchirp_all_b= L*Tchirp_b

#调频斜率
u = Bw_narrow/Tchirp_up
#最大探测距离   指的是宽波的最大距离还是窄波的，应该是窄波的
Rmax_acc = (fs/2)*(192/256)*(c/(2*u))
#最小探测距离
#Rmin_wide = delta_r_wide
Rmin_narrow = delta_r_narrow
#距离精度ACC,AEB
R_acc = 0.2*delta_r_narrow
#R_aeb = 0.2*delta_r_wide

#距离分离度ACC,AEB
R_sep_acc = 2*delta_r_narrow
#R_sep_aeb = 2*delta_r_wide














