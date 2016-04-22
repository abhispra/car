class GPIO:
    """Dummy class representing gpio library for rpi"""
    __pin_setup = dict()

    BOARD = 1
    IN = 1
    OUT = 2
    HIGH = 1
    LOW = 0

    @staticmethod
    def setmode(mode):
        if mode != GPIO.BOARD:
            raise ValueError("Invalid value for mode")

    @staticmethod
    def setup(pin, pintype):
        if pintype != GPIO.IN and pintype != GPIO.OUT:
            raise ValueError("Invalid mode")
        GPIO.__pin_setup[pin] = [pintype, GPIO.LOW]

    @staticmethod
    def input(pin):
        return list(GPIO.__pin_setup[pin])[1]

    @staticmethod
    def output(pin, val):
        if val != GPIO.LOW and val != GPIO.HIGH:
            raise ValueError("Invalid pin value")
        GPIO.__pin_setup[pin] = [list(GPIO.__pin_setup[pin])[0], val]

    @staticmethod
    def cleanup():
        print("cleanup called")
        GPIO.__pin_setup.clear()
