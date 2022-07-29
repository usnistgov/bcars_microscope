import serial
import time
import traceback
import numpy as np
from bcars_microscope.devices import AbstractDevice, AbstractStage

class ESP301(AbstractStage):

    device_name = 'ESP 301 Stage'
    prefix = 'Delay'

    def __init__(self, com_port, baudrate=921600, **kwargs):
        super().__init__(com_port=com_port, baudrate=baudrate, **kwargs)

    def get_position(self, axis=1):
        if self.serial:
            pos = float(self._read_write('{}TP'.format(axis)))
            self.settings['position'] = pos
            return pos

    def set_position(self, pos, axis=1, read_after=True):
        self._write('{}PA {}'.format(axis,pos))
        if read_after:
            self.get_position()

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
            self.motor_on()
            self.get_position()
            self.get_velocity()
        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')
        
    def motor_on(self):
        self._write('1MO_Set')
        self.settings['motor'] = 'on'

    def motor_off(self):
        self._write('1MF_Set')
        self.settings['motor'] = 'off'

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
        output = self.serial.readline().decode().rstrip('\r\n')
        return output

    def _write(self, write_command):
        self.serial.write('{}\r\n'.format(write_command).encode())

    def set_velocity(self, vel, axis=1):
        pass

    def get_velocity(self, axis=1):
        vel = self._read_write('{}VA?'.format(axis))
        self.settings['velocity'] = vel
        return vel


if __name__ == '__main__':
    esp = ESP301(com_port='COM9')
    print('Open?: {}'.format(esp.is_open))
    esp.open()
    try:
        print(esp._write('1MO'))
        print(esp._read_write('1MO?'))
    except Exception:
        print('Failed: {}'.format(traceback.format_exc()))
    # print('Open?: {}'.format(esp.is_open))

    curr_pos = esp.get_position()
    
    print('Current position: {:.3f}'.format(curr_pos))
    
    try:
        print('Velocity: {}'.format(esp.get_velocity()))
    except:
        print(traceback.format_exc())

    print('Current position: {:.3f}'.format(esp.get_position()))
    esp.close()
    print('Open?: {}'.format(esp.is_open))
    print(esp.__dict__)

