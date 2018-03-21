# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 15:30:54 2018
@author: TongYu
"""
# 最大探测距离
# 最小探测距离
# 距离精度
# 速度范围
# 速度精度
# 宽波  A波  B波
# 窄波  A波  B波
# 最大测速范围 Vmax = lamda/(2*Tchirp)   单个的Tchirp
c = 3*1e8
f = 77*1e9   #实际频率不是这个值，76.424GHz  76.576  76.7115
lamda = c/f
Tchirp_a = 60*1e-6
Tchirp_b = 70*1e-6
Tchirp_up = 56*1e-6
Tchirp_eff = 51.2*1e-6  #有效发波时间
#测速范围
#0~Vmax   +- Vmax_both    0~32m/s   +-16m/s
Vmax_a = lamda/(2*Tchirp_a)  # 速度有正负之分，所以实际最大测速为计算值的一半？？？
Vmax_a_both = Vmax_a/2
Vmax_b = lamda/(2*Tchirp_b)
Vmax_b_both = Vmax_b/2

# 128 A WAVE  128 B WAVE
L = 256  # 发波个数 
N = 512  # 第一次FFT点数 距离维
N_2 = 128 # 第二次FFT点数 速度维
# 速度分辨率
delta_v_a = Vmax_a/128
delta_v_b = Vmax_b/128
#速度精度
V_acc_a = 0.5*delta_v_a
V_acc_b = 0.5*delta_v_b
#速度分离度
V_sep_a = 2*delta_v_a
V_sep_b = 2*delta_v_b
#发波总时间
Tchirp_all_a = 128*Tchirp_a
Tchirp_all_b= 128*Tchirp_b
#采样频率
fs = 10*1e6
#带宽
Bw_wide = 423*1e6
Bw_narrow = 152*1e6

Bw_eff_wide = Bw_wide*Tchirp_eff/Tchirp_up      # 有效扫频带宽  
Bw_eff_narrow = Bw_narrow*Tchirp_eff/Tchirp_up
#距离分辨率
delta_R_wide = c/(2*Bw_eff_wide)
delta_R_narrow = c/(2*Bw_eff_narrow)

#调频斜率
u = Bw_narrow/Tchirp_up
#最大探测距离   指的是宽波的最大距离还是窄波的，应该是窄波的
Rmax = (fs/2)*(160/256)*(c/(2*u))
#最小探测距离
Rmin_wide = delta_R_wide
Rmin_narrow = delta_R_narrow
#距离精度
R_acc = 0.2*delta_R_narrow
R_aeb = 0.2*delta_R_wide

#距离分离度ACC,AEB
R_sep_acc = 2*delta_R_narrow
R_sep_aeb = 2*delta_R_wide














