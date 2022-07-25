import serial
import time
import traceback

from devices import AbstractDevice

class TopticaPro(AbstractDevice):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    laser = TopticaPro()