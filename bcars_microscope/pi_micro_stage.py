import abc
from pipython import GCSDevice
from time import sleep
import traceback
from devices import AbstractStage

class MicroStage(AbstractStage):
    device_name = 'PI C-867 Piezomotor Controller SN 0111036765'
    num_to_axis = {'2':'X', '1':'Y'}
    axis_to_num = {'X':'2','Y':'1'}

    def open(self):
        print('Opening device: {}'.format(self.device_name))
        try:
            self.sdk = GCSDevice('C-867')
            self.sdk.ConnectUSB(self.device_name)

        except Exception:
            print('Opening failed')
            print(traceback.format_exc())
        else:
            print('Opening succeeded')
            self.set_joystick_off()
        
    def close(self):
        print('Closing device: {}'.format(self.device_name))
        try:
            self.set_joystick_off()
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

    def set_x_position(self, pos):
        self.set_position({self.axis_to_num['X']: pos})

    def set_y_position(self, pos):
        self.set_position({self.axis_to_num['Y']: pos})
        
    def wait_till_done(self, pause=0.1, let_settle=False, settle_pause=0.1):
        while self.is_moving():
            sleep(pause)
        if let_settle:
            sleep(settle_pause)

    def is_moving(self):
        move_status = self.sdk.IsMoving()
        return (move_status['1'] | move_status['2'])

    def set_velocity(self, vel_dict):
        if self.sdk:
            self.sdk.VEL(vel_dict)

    def get_velocity(self):
        if self.sdk:
            vel = self.sdk.qVEL()
            return vel

    def get_joystick_status(self):
        if self.sdk:
            return self.sdk.qJON(1)[1]

    def set_joystick_on(self):
        if self.sdk:
            self.sdk.JON(1,1)

    def set_joystick_off(self):
        if self.sdk:
            self.sdk.JON(1,0)

if __name__ == '__main__':
    ms = MicroStage()
    ms.open()
    print('Current Position: {}'.format(ms.get_position()))
    print('Current Velocity: {}'.format(ms.get_velocity()))
    try:
        print('JoyStick State: {}'.format(ms.get_joystick_status()))
    except:
        print(traceback.format_exc())

    try:
        ms.set_joystick_on()
        print('JoyStick State: {}'.format(ms.get_joystick_status()))
    except:
        print(traceback.format_exc())

    try:
        ms.set_joystick_off()
        print('JoyStick State: {}'.format(ms.get_joystick_status()))
    except:
        print(traceback.format_exc())

    ms.close()