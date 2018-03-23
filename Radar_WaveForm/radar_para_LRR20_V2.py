# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:02:14 2018

@author: TongYu
"""
c = 3*1e8
range_interpolation = 0.2
velocity_interpolation = 0.5
#
#Tdwell = tchirp + tdwell MIMO2
#Tchirp = tchirp + tchirp
#Tdwell = tchirp + tchirp +tdwell


class Waveform(object):
#   fs 采样频率 ；L 发波个数；N 第一维FFT点数；Tdwell 保压时间；Tchirp_up 上升沿时间；Treset 下降沿时间；f 载频；Bw 带宽
    def __init__(self,fs,L,N,Tdwell,Tchirp_up,Treset,f,Bw):
#    def __init__(self,fs,L,N,NF,Tdwell,Tchirp_up,Treset,f,Bw,mimo):
        self.fs = fs
        self.L = L
        self.N = N
        self.Tdwell= Tdwell
        self.Tchirp_up = Tchirp_up
        self.Treset = Treset
        self.f = f
        self.Bw = Bw
#        self.NF = NF
#        self.mimo = mimo
    def init_spmParasThroughRFinfo(self):
        self.calcul_delta_r()
        self.calcul_rmax()
        self.calcul_rmin()
        self.calcul_racc()
        self.calcul_rsep()
        self.calcul_vmax()
        self.calcul_delta_v()
        self.calcul_vacc()
        self.calcul_vsep()
        
        
    def calcul_delta_r(self):
        Tchirp_eff = self.N/self.fs
        Bw_eff = self.Bw*Tchirp_eff/self.Tchirp_up
        self.delta_r = c/(2*Bw_eff)
    def get_delta_r(self):
        return self.delta_r
    
    
    def calcul_rmax(self):
        u = self.Bw/self.Tchirp_up
#        self.rmax = (self.fs/2)*(self.NF/(self.N/2))*(c/(2*u))
        self.rmax = (self.fs/2)*(c/(2*u))
    def get_rmax(self):
        return self.rmax
    
    def calcul_rmin(self):
        self.rmin = self.delta_r
    def get_rmin(self):
        return self.rmin
    
    def calcul_racc(self):
        self.racc = range_interpolation*self.delta_r
    def get_racc(self):
        return self.racc
    
    def calcul_rsep(self):
        self.rsep = 2*self.delta_r
    def get_rsep(self):  
        return self.rsep
    
    def calcul_vmax(self):
        lamda = c/self.f
#        if self.mimo == 1:
#            Tchirp = (self.Tdwell+self.Tchirp_up+self.Treset)*2  # for MIMO RADAR
#        else :
        Tchirp = self.Tdwell+self.Tchirp_up+self.Treset

        self.vmax = (lamda/(2*Tchirp))
    def get_vmax(self):
        return self.vmax
    
    def calcul_delta_v(self):
        self.delta_v = self.vmax/self.L
    def get_delta_v(self):
        return self.delta_v
    def calcul_vacc(self):
        self.vacc = velocity_interpolation*self.delta_v
    def get_vacc(self):   
        return self.vacc
    
    def calcul_vsep(self):
        self.vsep = 2*self.delta_v
    def get_vsep(self):
        return self.vsep
    def print_para(self):
        print('delta_r: %s\nrmax: %s\nrmin: %s\nracc: %s\nrsep: %s\nvmax: %s\ndelta_v: %s\nvacc: %s\nvsep: %s\n' \
                        % (self.delta_r,self.rmax,self.rmin,self.racc,self.rsep,self.vmax,self.delta_v,self.vacc,self.vsep))
    
lrr20 = Waveform(40*1e6, 256,512, 8*1e-6, 19*1e-6, 3*1e-6, 77*1e9, 247*1e6)
#print(lrr20.vsep())
#lrr20.print_para()
lrr20.init_spmParasThroughRFinfo()
#print(lrr20.rmax)
lrr20.print_para()

