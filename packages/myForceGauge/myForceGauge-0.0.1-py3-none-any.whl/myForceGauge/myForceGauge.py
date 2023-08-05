# 0.0.1

import serial
import time

class ForceGauge_communication:
    def __init__(self):
        self._ser: serial.serialwin32.Serial = None

    def init(self, COM):
        try:
            self._ser = serial.Serial(COM, baudrate=460800, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE, timeout=0.0001)
            return 1
        except serial.serialutil.SerialException:
            return -1

    def read(self):
        self._ser.write(b'XAR\r')
        time.sleep(0.0001)
        line = self._ser.read_all().decode()
        if line == '':
            while line == '':
                line = self._ser.read_all().decode()
        value = float(line[1:7])
        return value

    def exit(self):
        self._ser.close()
