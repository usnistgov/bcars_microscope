import serial
import time
import traceback
import numpy as np

from devices import AbstractStage

class ESP301(AbstractStage):
    device_name = 'ESP 301 Stage'
    def __init__(self, com_port, baudrate=921600, **kwargs):
        super().__init__(com_port=com_port, baudrate=baudrate, **kwargs)

    def get_position(self, axis=1):
        if self.serial:
            pos = self._read_write('{}TP'.format(axis))
            return pos

    def set_position(self, pos, axis=1):
        self._write('{}PA {}'.format(axis,pos))

    def set_home(self, axis=1):
        self._write('{}DH'.format(axis))

    def wait_till_done(self, n_iter=10, pause=0.1, let_settle=True, settle_pause=0.25, axis=1):
        for _ in range(n_iter):
            time.sleep(pause)
            line = self._read_write('{}MD?'.format(axis))
            # print('Is motion done? (0: NOT done; 1: done): {}'.format(line))
            if int(line) == 1:
                break
        if let_settle:
            for _ in range(n_iter):
                pos1 = self.get_position()
                time.sleep(settle_pause)
                pos2 = self.get_position()
                if round(pos1,3) == round(pos2,3):
                    break
        return None

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.serial = serial.Serial(self.settings['com_port'], self.settings['baudrate'], timeout=1)
        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')
        
    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.serial.close()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.serial = None
    
    def _read_write(self, write_command):
        self.serial.write('{}\r\n'.format(write_command).encode())
        output = float(self.serial.readline().decode().rstrip('\r\n'))
        return output

    def _write(self, write_command):
        self.serial.write('{}\r\n'.format(write_command).encode())

    def set_velocity(self, vel, axis=1):
        pass

    def get_velocity(self, axis=1):
        vel = self._read_write('{}VA?'.format(axis))
        return vel

if __name__ == '__main__':
    esp = ESP301(com_port='COM9')
    print('Open?: {}'.format(esp.is_open))
    esp.open()
    print('Open?: {}'.format(esp.is_open))

    curr_pos = esp.get_position()
    new_pos = curr_pos + (-1 * np.sign(curr_pos) * 0.1)

    print('Current position: {:.3f}'.format(curr_pos))
    print('Set position: {:.3f}'.format(new_pos))
    esp.set_position(new_pos)
    esp.wait_till_done()
    
    try:
        print('Velocity: {}'.format(esp.get_velocity()))
    except:
        print(traceback.format_exc())

    print('Current position: {:.3f}'.format(esp.get_position()))
    esp.close()
    print('Open?: {}'.format(esp.is_open))
    print(esp.__dict__)


# class ESP301:
#     def __init__(self, com_port='COM9', baudrate=921600):
#         self.ser = serial.Serial(com_port, baudrate, timeout=1)
        
#     def wait_till_done(self, n_iter=10, pause=0.1, let_settle=True, settle_pause=0.25):
#         for _ in range(n_iter):
#             time.sleep(pause)
#             self.ser.write(b'1MD?\r\n')
#             line = self.ser.readline().decode().rstrip('\r\n')
#             # print('Is motion done? (0: NOT done; 1: done): {}'.format(line))
#             if int(line) == 1:
#                 break
#         if let_settle:
#             for _ in range(n_iter):
#                 self.ser.write(b'1TP\r\n')
#                 pos1 = float(self.ser.readline().decode().rstrip('\r\n'))
#                 time.sleep(settle_pause)
#                 self.ser.write(b'1TP\r\n')
#                 pos2 = float(self.ser.readline().decode().rstrip('\r\n'))
#                 if round(pos1,3) == round(pos2,3):
#                     break
#         return None
    
#     def close(self):
#         self.ser.close()

#     def get_pos(self):
#         self.ser.write(b'1TP\r\n')
#         line = float(self.ser.readline().decode().rstrip('\r\n'))
#         return line

#     def set_pos(self, pos):
#         self.ser.write('1PA {}\r\n'.format(pos).encode())
#         # self.wait_till_done(pause=0.1, n_iter=100, let_settle=True)
#         return None

#     def set_home(self):
#         self.ser.write(b'1DH\r\n')
#         return None


# if __name__ == '__main__':
#     try:
#         esp_device = ESP301()
#         print('ESP is open: {}'.format(esp_device.ser.is_open))
#         curr_pos = esp_device.get_pos()
#         print('Current position: {} mm'.format(curr_pos))
#         new_pos = np.abs(curr_pos) - 1.
#         print('Moving to: {}'.format(new_pos))
#         esp_device.set_pos(new_pos)
#         print('Waiting...')
#         esp_device.wait_till_done()
#         curr_pos = esp_device.get_pos()
#         print('Current position: {} mm'.format(curr_pos))

#         if curr_pos == 0.0:
#             print('Near origin, doing small second experiment')
#             print('Move to 0.01')       
#             esp_device.set_pos(0.01)
#             esp_device.wait_till_done()
#             print('Current position: {}'.format(esp_device.get_pos()))
#             print('Set Home')
#             esp_device.set_home()
#             print('New Current position (Should be 0): {}'.format(esp_device.get_pos()))
#             print('Move to -0.01')       
#             esp_device.set_pos(-0.01)
#             esp_device.wait_till_done()
#             print('Current position: {}'.format(esp_device.get_pos()))
#             print('Set Home')
#             esp_device.set_home()
#             print('New Current position (Should be 0): {}'.format(esp_device.get_pos()))
#     except Exception as e:
#         print(traceback.format_exc())
#     finally:
#         esp_device.ser.close()
#     # print(ser.is_open)
#     # ser.write(b'1TP\r\n')
#     # line = ser.readline().decode().rstrip('\r\n')
#     # print('Current position: {} mm'.format(line))
#     # print('Move to: {}'.format(move_to))
#     # ser.write('1PA {}\r\n'.format(move_to).encode())
#     # wait_till_done(pause=0.1, n_iter=100)
#     # ser.write(b'1TP\r\n')
#     # line = ser.readline().decode().rstrip('\r\n')
#     # print('Current position: {} mm'.format(line))

#     # # create an ESP301 instance 
#     # ESP301Device = CommandInterfaceESP301.ESP301() 
#     # # Open communication 
#     # ret = ESP301Device.OpenInstrument(instrument, BAUDRATE)
#     # print('Open Instrument return value (0=good): {}'.format(ret))

#     # result, response, errString = ESP301Device.TP(1)
#     # print(result)
#     # print(response)
#     # print(errString)

#     # # Close communication
#     # ret = ESP301Device.CloseInstrument()
#     # print('Close Instrument return value (0=good): {}'.format(ret))

