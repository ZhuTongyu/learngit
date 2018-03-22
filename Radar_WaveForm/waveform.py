# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 13:02:14 2018

@author: TongYu
"""

class Waveform(object):
    
    def __init__(self,fs,L,N,NF,Tdwell,Tchirp_up,Treset,f,Bw,mimo):
        self.fs = fs
        self.L = L
        self.N = N
        self.Tdwell= Tdwell
        self.Tchirp_up = Tchirp_up
        self.Treset = Treset
        self.f = f
        self.Bw = Bw
        self.NF = NF
        self.mimo = mimo
        
    def delta_r(self):
        Tchirp_eff = self.N/self.fs
        Bw_eff = self.Bw*Tchirp_eff/self.Tchirp_up
        delta_r = 3*1e8/(2*Bw_eff)
        return delta_r
    
    def rmax(self):
        u = self.Bw/self.Tchirp_up
        rmax = (self.fs/2)*(self.NF/(self.N/2))*(3*1e8/(2*u))
        return rmax
    
    def rmin(self):
        rmin = self.delta_r()
        return rmin
    
    def racc(self):
        racc = 0.2*self.delta_r()
        return racc
    
    def rsep(self):
        rsep = 2*self.delta_r()
        return rsep
    
    def vmax(self):
        lamda = 3*1e8/self.f
        if self.mimo == 1:
            Tchirp = (self.Tdwell+self.Tchirp_up+self.Treset)*2  # for MIMO RADAR
        else :
            Tchirp = self.Tdwell+self.Tchirp_up+self.Treset

        vmax = (lamda/(2*Tchirp))
        return vmax
    
    def delta_v(self):
        delta_v = self.vmax()/self.L
        return delta_v
    def vacc(self):
        vacc = 0.5*self.delta_v()
        return vacc
    
    def vsep(self):
        vsep = 2*self.delta_v()
        return vsep
    def print_para(self):
        print('delta_r: %s\nrmax: %s\nrmin: %s\nracc: %s\nrsep: %s\nvmax: %s\ndelta_v: %s\nvacc: %s\nvsep: %s\n' \
                        % (self.delta_r(),self.rmax(),self.rmin(),self.racc(),self.rsep(),self.vmax(),self.delta_v(),self.vacc(),self.vsep()))
    
lrr20 = Waveform(40*1e6, 256,512,192, 8*1e-6, 19*1e-6, 3*1e-6, 77*1e9, 670*1e6,1)
#print(lrr20.vsep())
lrr20.print_para()