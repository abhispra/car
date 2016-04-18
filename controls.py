# import RPi.GPIO as GPIO
from RPi.GPIO import GPIO
from pin_val_set import PinValueSet
from values import DebugTraceLevel


class Motor:
    """Class to control motor direction
    Motor can start/stop/reverse"""
    _initLibrary = False
    _debug_level = 0

    _refCount = 0

    def __init__(self, enable_pin, pin1, pin2,
                 debug_level=DebugTraceLevel.NONE):
        if not Motor._initLibrary:
            GPIO.setmode(GPIO.BOARD)

        Motor._initLibrary = True
        Motor._refCount += 1
        self.__enable = enable_pin
        self.__pin1 = pin1
        self.__pin2 = pin2
        self._debug_level = debug_level
        GPIO.setup(self.__pin1, GPIO.OUT)
        GPIO.setup(self.__pin2, GPIO.OUT)
        GPIO.setup(self.__enable, GPIO.OUT)

    def __del__(self):
        self.debug_message(DebugTraceLevel.DEBUG, "Cleanup called")
        Motor._refCount -= 1
        if not Motor._refCount:
            GPIO.cleanup()

    def debug_message(self, debug_level, string):
        if (self._debug_level.value <= debug_level.value and
                    self._debug_level.value != DebugTraceLevel.NONE):
            print(type(self).__name__ + ": " + string)

    def __write(self, pin_val):
        self.debug_message(DebugTraceLevel.DEBUG, "Entering write with val " +
                           str(pin_val.get_all()))
        GPIO.output(self.__enable, pin_val.get_enable())
        GPIO.output(self.__pin1, pin_val.get_pin1())
        GPIO.output(self.__pin2, pin_val.get_pin2())
        self.debug_message(DebugTraceLevel.DEBUG, "Exiting write")

    def __read(self):
        pin_val = PinValueSet(GPIO.input(self.__enable),
                              GPIO.input(self.__pin1), GPIO.input(self.__pin2))
        self.debug_message(DebugTraceLevel.DEBUG, "Read " + str(pin_val.get_all()))
        return pin_val

    @property
    def __is_running(self):
        pin_val = self.__read()
        enabled = (pin_val.get_enable() == GPIO.HIGH and
                   pin_val.get_pin1() != pin_val.get_pin2())
        self.debug_message(DebugTraceLevel.DEBUG, "__is_running: " + str(enabled))
        return enabled

    def start(self):
        """
        Starts the motor in forward(assumed) direction
        """
        if self.__is_running:
            self.debug_message(DebugTraceLevel.INFO, "Motor already running")
        else:
            pin_val = PinValueSet(GPIO.HIGH, GPIO.LOW, GPIO.HIGH)
            self.__write(pin_val)
            self.debug_message(DebugTraceLevel.DEBUG, "Motor started")

    def stop(self):
        """
        Stops the motor if its currently running
        """
        if not self.__is_running:
            self.debug_message(DebugTraceLevel.INFO, "Motor not running")
        else:
            pin_val = self.__read()
            pin_val.set_enable(GPIO.LOW)
            self.__write(pin_val)
            self.debug_message(DebugTraceLevel.DEBUG, "Motor stopped")

    def reverse(self):
        pin_val = PinValueSet()
        if not self.__is_running:
            self.debug_message(DebugTraceLevel.INFO, "Motor not running, starting in assumed reverse")
        else:
            pin_val = self.__read()
            pin_val.set_pin1(int(pin_val.get_pin1() != GPIO.HIGH))
            pin_val.set_pin2(int(pin_val.get_pin2() != GPIO.HIGH))

        self.debug_message(DebugTraceLevel.DEBUG, "Pin values :" + str(pin_val.get_all()))
        self.__write(pin_val)
