#import RPi.GPIO as GPIO
from RPi.GPIO import GPIO


class PinValueSet:
    _enable_val = GPIO.LOW
    _pin1_val = GPIO.LOW
    _pin2_val = GPIO.LOW

    def __init__(self, enable_val=GPIO.LOW, pin1_val=GPIO.LOW, pin2_val=GPIO.LOW):
        self._enable_val = enable_val
        self._pin1_val = pin1_val
        self._pin2_val = pin2_val

    def get_enable(self):
        return self._enable_val

    def get_pin1(self):
        return self._pin1_val

    def get_pin2(self):
        return self._pin2_val

    def get_all(self):
        return self.get_enable(), self.get_pin1(), self.get_pin2()

    def set_enable(self, enable_val):
        self._enable_val = enable_val

    def set_pin1(self, pin1_val):
        self._pin1_val = pin1_val

    def set_pin2(self, pin2_val):
        self._pin2_val = pin2_val

    def set_all(self, enable_val, pin1_val, pin2_val):
        self.set_enable(enable_val)
        self.set_pin1(pin1_val)
        self.set_pin2(pin2_val)
