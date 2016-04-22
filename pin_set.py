import RPi.GPIO as GPIO
#from RPi.GPIO import GPIO
from pin import Pin


class PinSet:

    def __init__(self, enable, pin1, pin2):
        self._enable = Pin(enable, GPIO.OUT)
        self._pin1 = Pin(pin1, GPIO.OUT)
        self._pin2 = Pin(pin2, GPIO.OUT)

    def get_enable_number(self):
        return self._enable.get_pin_number()

    def get_pin1_number(self):
        return self._pin1.get_pin_number()

    def get_pin2_number(self):
        return self._pin2.get_pin_number()

    def get_all_pin_numbers(self):
        return self._enable.get_pin_number(), self._pin1.get_pin_number(), \
               self._pin2.get_pin_number()

    def get_enable_val(self):
        return self._enable.get_pin_value()

    def get_pin1_val(self):
        return self._pin1.get_pin_value()

    def get_pin2_val(self):
        return self._pin2.get_pin_value()

    def get_all(self):
        return self._enable.get_pin_value(), self._pin1.get_pin_value(), \
               self._pin2.get_pin_value()

    def set_enable_val(self, val):
        self._enable.set_pin_value(val)

    def set_pin1_val(self, val):
        self._pin1.set_pin_value(val)

    def set_pin2(self, val):
        self._pin2.set_pin_value(val)

    def set_all(self, enable, pin1, pin2):
        self._enable.set_pin_value(enable)
        self._pin1.set_pin_value(pin1)
        self._pin2.set_pin_value(pin2)
