import RPi.GPIO as GPIO
#from RPi.GPIO import GPIO
from values import Const


class Pin:
    _pin_number = -1
    _pin_type = GPIO.OUT
    _pin_value = GPIO.LOW

    def __init__(self, pin_number, pin_type, pin_value = GPIO.LOW):
        if pin_number < Const.PIN_MIN or pin_number > Const.PIN_MAX:
            raise ValueError
        if pin_type != GPIO.IN and pin_type != GPIO.OUT:
            raise ValueError
        if pin_value != GPIO.LOW and pin_value != GPIO.HIGH:
            raise ValueError
        self._pin_number = pin_number
        self._pin_type = pin_type
        self._pin_value = pin_value
        GPIO.setup(self._pin_number, self._pin_type)

    def get_pin_value(self):
        self._pin_value = GPIO.input(self._pin_number)
        return self._pin_value

    def get_pin_type(self):
        return self._pin_type

    def get_pin_number(self):
        return self._pin_number

    def set_pin_value(self, pin_value):
        self._pin_value = pin_value
        GPIO.output(self._pin_number, pin_value)

    def set_pin_type(self, pin_type):
        self._pin_type = pin_type
        GPIO.setup(self._pin_number, self._pin_type)
