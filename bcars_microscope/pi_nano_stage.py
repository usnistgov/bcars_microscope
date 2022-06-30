import abc
import traceback

from pipython import GCSDevice
from time import sleep

from devices import AbstractStage

class NanoStage(AbstractStage):
    device_name = 'PI E-517 Display and Interface SN 0114071272'

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.sdk = GCSDevice('E-545')
            self.sdk.ConnectUSB(self.device_name)

        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')
        
    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.sdk.CloseConnection()
        except Exception:
            print('Closing failed')
            print(traceback.format_exc())
        else:
            print('Closing succeeded')
            self.sdk = None

    def get_position(self):
        if self.sdk:
            pos = self.sdk.qPOS()
            return pos

    def set_position(self, pos_dict):
        assert isinstance(pos_dict, dict)
        self.sdk.MOV(pos_dict)
        
    def wait_till_done(self, n_iter, pause, let_settle, settle_pause):
        raise NotImplementedError('Haven\'t found a good way to do this yet')

    def set_velocity(self, vel_dict):
        if self.sdk:
            self.sdk.VEL(vel_dict)

    def get_velocity(self):
        if self.sdk:
            vel = self.sdk.qVEL()
            return vel

    def get_wavegen_rate(self, num_wavegen=None):
        if self.sdk:
            if num_wavegen is None:
                return self.sdk.qWTR()
            else:
                return self.sdk.qWTR(num_wavegen)

    def set_wavegen_rate(self, num_wavegen, rate):
        if self.sdk:
            self.sdk.WTR(num_wavegen, rate, 0)

    def set_linescan(self, table_num, start, num_points, stop):
        self.sdk.WAV_LIN(table=table_num, firstpoint=0, numpoints=num_points, 
                         append='X', speedupdown=0, amplitude=stop - start, 
                         offset=start, seglength=num_points)

if __name__ == '__main__':
    ns = NanoStage()
    ns.open()
    print('Current Position: {}'.format(ns.get_position()))
    print('Current Velocity: {}'.format(ns.get_velocity()))
    print('Wavegen rates: {}'.format(ns.get_wavegen_rate()))
    print('Set Wavegen rates: {}'.format(ns.get_wavegen_rate()))
    ns.close()

