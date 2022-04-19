from pipython import GCSDevice
import traceback
from time import sleep

pidevice = GCSDevice('E-545')
try:
    pidevice.ConnectUSB('PI E-517 Display and Interface SN 0114071272')
    print(pidevice.qIDN())
    # print(pidevice.qPOS())
    pidevice.MOV({'X':90})
    # print(pidevice.qPOS())
    pidevice.WAV_LIN(1,1,50,'X',0, 198, 1, 50)
    print(pidevice.qPOS())
    pidevice.gcscommands.WAV_LIN(table=1, firstpoint=0, numpoints=50, append='X', speedupdown=0, amplitude=198, offset=1, seglength=50)
    # WAV 1 X LIN 100 198 1 100 0 0
    pidevice.gcscommands.WGO(1,mode=11)
    # print('Is moving: {}'.format(pidevice.gcscommands.IsMoving()))
    temp = pidevice.gcscommands.IsMoving()
    print('Is moving: {}'.format(any([temp[t] for t in temp])))
    sleep(1)
    
    print(pidevice.qPOS())
except Exception as e:
    print(traceback.format_exc())
    pidevice.CloseConnection()
else:
    pidevice.CloseConnection()