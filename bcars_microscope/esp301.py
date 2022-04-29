import serial
import time
import traceback
import numpy as np

class ESP301:
    def __init__(self, com_port='COM9', baudrate=921600):
        self.ser = serial.Serial(com_port, baudrate, timeout=1)
        
    def wait_till_done(self, n_iter=10, pause=0.1, let_settle=True, settle_pause=0.25):
        for _ in range(n_iter):
            time.sleep(pause)
            self.ser.write(b'1MD?\r\n')
            line = self.ser.readline().decode().rstrip('\r\n')
            # print('Is motion done? (0: NOT done; 1: done): {}'.format(line))
            if int(line) == 1:
                break
        if let_settle:
            for _ in range(n_iter):
                self.ser.write(b'1TP\r\n')
                pos1 = float(self.ser.readline().decode().rstrip('\r\n'))
                time.sleep(settle_pause)
                self.ser.write(b'1TP\r\n')
                pos2 = float(self.ser.readline().decode().rstrip('\r\n'))
                if round(pos1,3) == round(pos2,3):
                    break
        return None
    
    def close(self):
        self.ser.close()

    def get_pos(self):
        self.ser.write(b'1TP\r\n')
        line = float(self.ser.readline().decode().rstrip('\r\n'))
        return line

    def set_pos(self, pos):
        self.ser.write('1PA {}\r\n'.format(pos).encode())
        # self.wait_till_done(pause=0.1, n_iter=100, let_settle=True)
        return None

    def set_home(self):
        self.ser.write(b'1DH\r\n')
        return None


if __name__ == '__main__':
    try:
        esp_device = ESP301()
        print('ESP is open: {}'.format(esp_device.ser.is_open))
        curr_pos = esp_device.get_pos()
        print('Current position: {} mm'.format(curr_pos))
        new_pos = np.abs(curr_pos) - 1.
        print('Moving to: {}'.format(new_pos))
        esp_device.set_pos(new_pos)
        print('Waiting...')
        esp_device.wait_till_done()
        curr_pos = esp_device.get_pos()
        print('Current position: {} mm'.format(curr_pos))

        if curr_pos == 0.0:
            print('Near origin, doing small second experiment')
            print('Move to 0.01')       
            esp_device.set_pos(0.01)
            esp_device.wait_till_done()
            print('Current position: {}'.format(esp_device.get_pos()))
            print('Set Home')
            esp_device.set_home()
            print('New Current position (Should be 0): {}'.format(esp_device.get_pos()))
            print('Move to -0.01')       
            esp_device.set_pos(-0.01)
            esp_device.wait_till_done()
            print('Current position: {}'.format(esp_device.get_pos()))
            print('Set Home')
            esp_device.set_home()
            print('New Current position (Should be 0): {}'.format(esp_device.get_pos()))
    except Exception as e:
        print(traceback.format_exc())
    finally:
        esp_device.ser.close()
    # print(ser.is_open)
    # ser.write(b'1TP\r\n')
    # line = ser.readline().decode().rstrip('\r\n')
    # print('Current position: {} mm'.format(line))
    # print('Move to: {}'.format(move_to))
    # ser.write('1PA {}\r\n'.format(move_to).encode())
    # wait_till_done(pause=0.1, n_iter=100)
    # ser.write(b'1TP\r\n')
    # line = ser.readline().decode().rstrip('\r\n')
    # print('Current position: {} mm'.format(line))

    # # create an ESP301 instance 
    # ESP301Device = CommandInterfaceESP301.ESP301() 
    # # Open communication 
    # ret = ESP301Device.OpenInstrument(instrument, BAUDRATE)
    # print('Open Instrument return value (0=good): {}'.format(ret))

    # result, response, errString = ESP301Device.TP(1)
    # print(result)
    # print(response)
    # print(errString)

    # # Close communication
    # ret = ESP301Device.CloseInstrument()
    # print('Close Instrument return value (0=good): {}'.format(ret))

