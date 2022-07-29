import abc
import serial
import traceback
import time

import numpy as np

class AbstractDevice(abc.ABC):
    device_name = 'Abstract Device'
    prefix = None
    
    def __init__(self, *args, **kwargs):
        """Abstract base class for all devices """
        super().__init__()
        self.settings = {}
        self.sdk = None
        self.serial = None

        if kwargs:
            self.settings.update(kwargs)

    @property
    def is_open(self):
        return (self.sdk is not None) | (self.serial is not None)
        
    @abc.abstractmethod
    def open(self):
        """ Open the channel, SDK, and device """
        pass

    @abc.abstractmethod
    def close(self):
        """ Open the channel, SDK, and device """
        pass

    @property
    def meta(self):
        if self.prefix is None:
            return self.settings
        else:
            return {'{}.{}'.format(self.prefix, k):self.settings[k] for k in self.settings}


class AbstractStage(AbstractDevice):
    device_name = 'Abstract Stage'

    @abc.abstractmethod
    def get_position(self):
        pass

    @abc.abstractmethod
    def set_position(self, axis, pos):
        pass

    @abc.abstractmethod
    def set_velocity(self, axis, vel):
        pass

    @abc.abstractmethod
    def wait_till_done(self, n_iter, pause, let_settle, settle_pause):
        pass

