import numpy as np
import matplotlib.pyplot as plt
import ctypes
import tkinter.filedialog
import GetRadarData as grd
RADAR_MAX_COUNT = 100
RADAR_DATA_MAX_SIZE = 1025*256
Hdll = ctypes.cdll.LoadLibrary('E://for xl//ExportRawData//SQLite3Hyc.dll')
#path = b'D://CapData//MRR20//20180326//Road Test//MRR20_20180326 17-31-40.625_data.hyd'
path = tkinter.filedialog.askopenfilename()
path = bytes(path, encoding = "utf8") 
pStr = ctypes.c_char_p(path)
ret = Hdll.OpenRadarDataFile(pStr)
arrayTableNumber = (ctypes.c_long*RADAR_MAX_COUNT)()
arrayTableDataCount = (ctypes.c_long*RADAR_MAX_COUNT)()
nArrayCount =(ctypes.c_long*1)()
nArrayCount[0] = RADAR_MAX_COUNT
ret = Hdll.GetRadarDataTabelInfo(arrayTableNumber, arrayTableDataCount, nArrayCount)
fCapTime =(ctypes.c_double*1)()
iLen = (ctypes.c_long*1)()
dataBuf = np.array(range(RADAR_DATA_MAX_SIZE), dtype = np.int32)

for i in range(arrayTableDataCount[0]):
    retHyc = Hdll.GetRadarData(0, i, fCapTime, dataBuf.ctypes.data, iLen)
    FrameData = dataBuf[256:256+(iLen[0]>>2)].byteswap()
    TarA,TarB,*_ = grd.MRR20_1M(FrameData)
Hdll.CloseRadarDataFile()