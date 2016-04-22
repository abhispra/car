from time import sleep
#from RPi.GPIO import GPIO
import RPi.GPIO as GPIO
from motor import Motor
from values import DebugTraceLevel
from values import Const
from pin_set import PinSet
from vehicle import Vehicle

Motor1A = 18
Motor1B = 16
Motor1E = 12
Motor2A = 15
Motor2B = 13
Motor2E = 11

GPIO.setmode(GPIO.BOARD)
rl_pin_set = PinSet(Motor1E, Motor1A, Motor1B)
rr_pin_set = PinSet(Motor2E, Motor2A, Motor2B)

vehicle = Vehicle(Const.TWO_WHEELED, rl_pin_set, rr_pin_set)

vehicle.forward()
sleep(2)
vehicle.turn_left()
sleep(0.75)
vehicle.forward()
sleep(2)
vehicle.turn_right()
sleep(0.75)
vehicle.forward()
sleep(1)
vehicle.reverse()
sleep(3)
vehicle.stop()
