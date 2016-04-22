from values import Const
from motor import Motor
#from pin_set import PinSet


class Vehicle:

    _control_list = dict()

    def __init__(self, drive_type, rleft_pin_set, rright_pin_set,
                 fleft_pin_set=None, fright_pin_set=None):
        if drive_type != Const.FOUR_WHEELED and drive_type != Const.TWO_WHEELED:
            raise ValueError
        if (drive_type == Const.FOUR_WHEELED and
            (fleft_pin_set is None or fright_pin_set is None)):
            raise ValueError
        self._control_list[Const.REAR_LEFT] = Motor(rleft_pin_set)
        self._control_list[Const.REAR_RIGHT] = Motor(rright_pin_set)

    def forward(self):
        self._control_list[Const.REAR_LEFT].start()
        self._control_list[Const.REAR_RIGHT].start()

    def stop(self):
        self._control_list[Const.REAR_LEFT].stop()
        self._control_list[Const.REAR_RIGHT].stop()

    def reverse(self):
        self._control_list[Const.REAR_LEFT].reverse()
        self._control_list[Const.REAR_RIGHT].reverse()

    def turn_left(self):
        self._control_list[Const.REAR_LEFT].stop()
        #self._control_list[Const.REAR_RIGHT].reverse()

    def turn_right(self):
        #self._control_list[Const.REAR_LEFT].stop()
        self._control_list[Const.REAR_RIGHT].stop()