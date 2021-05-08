import psutil
import serial
import numpy as np
import time

## AUX faunctions
def get_temp():
    temps = psutil.sensors_temperatures()['coretemp']
    tlist = [t.current for t in temps]
    return np.average(tlist)

def fanON(S):
    S.close()

def fanOFF(S):
    S.open()

## Main
def main():
    ## cts
    Thigh=70
    Tlow=45
    COMPort="/dev/ttyS0"
    ## setup
    ser=serial.Serial()
    ser.port=COMPort
    ser.setRTS(True)
    ser.open()
    ## main loop
    state=0
    print("Running fan control...")
    while(True):
        if state==0:
            if get_temp()>Thigh:
                fanON(ser)
                state=1
        elif state==1:
            if get_temp()<Tlow:
                fanOFF(ser)
                state=0
        else:
            state=0
        #print("state: {}\tT: {:.1f}".format(state, get_temp()))
        time.sleep(10)

main()

