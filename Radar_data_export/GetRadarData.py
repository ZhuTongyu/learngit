import numpy as np

def MRR20_1M(frm):
    if frm.size!=1024*256:
        return 0,0,0,0,0,0
    M = 192
    N = 256
    Peak_len = 6*256
    Mag_len = M*N
    PeakA_ptr = 0x5d000>>2
    ObjA_ptr = 0x40000>>2
    PeakB_ptr = 0x5e800>>2
    ObjB_ptr = 0x4e800>>2
    MagA_ptr = 0x60000>>2
    MagB_ptr = 0x90000>>2
    MagA = frm[MagA_ptr:MagA_ptr+Mag_len].reshape([192,256])
    MagB = frm[MagB_ptr:MagB_ptr+Mag_len].reshape([192,256])
    TarNuma = frm[ObjA_ptr]
    TarNumb = frm[ObjB_ptr]
    TargetA = np.zeros([TarNuma,10], dtype = np.complex)
    TargetB = np.zeros([TarNumb,10], dtype = np.complex)
    TargetA[:,0] = frm[ObjA_ptr+3:ObjA_ptr+3+27*TarNuma:27]>>16 # int32 高16位
    TargetA[:,1] = frm[ObjA_ptr+3:ObjA_ptr+3+27*TarNuma:27]&(0xff) # 0x00..0011111111 得到低16位
    temp = frm[ObjA_ptr+13:ObjA_ptr+13+27*TarNuma].reshape([TarNuma,27])
    TargetA[:,2:10] = 1j*temp[:,0:15:2]+temp[:,1:16:2] #[2:9]??
    TargetB[:,0] = frm[ObjB_ptr+3:ObjB_ptr+3+27*TarNumb:27]>>16
    TargetB[:,1] = frm[ObjB_ptr+3:ObjB_ptr+3+27*TarNumb:27]&(0xff)
    temp = frm[ObjB_ptr+13:ObjB_ptr+13+27*TarNumb].reshape([TarNumb,27])
    TargetB[:,2:10] = 1j*temp[:,0:15:2]+temp[:,1:16:2]
    PeakA = np.zeros([M,N],np.int)
    PeakB = np.zeros([M,N],np.int)
    peaka = frm[PeakA_ptr:PeakA_ptr+Peak_len].reshape([N,M>>5])
    peakb = frm[PeakB_ptr:PeakB_ptr+Peak_len].reshape([N,M>>5])
    for Bit in range(1<<5):
        for Idx in range(M>>5):
            PeakA[Idx*32+Bit,:]=(peaka[:,Idx]>>Bit)&1
            PeakB[Idx*32+Bit,:]=(peakb[:,Idx]>>Bit)&1
    return TargetA , TargetB , MagA , MagB , PeakA , PeakB



