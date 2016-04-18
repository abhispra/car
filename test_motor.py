from time import sleep
from RPi.GPIO import GPIO
from controls import Motor
from values import DebugTraceLevel

Motor1A = 16
Motor1B = 18
Motor1E = 12
Motor2A = 6
Motor2B = 8
Motor2E = 2

motor1 = Motor(Motor1E, Motor1A, Motor1B, DebugTraceLevel.DEBUG)
motor2 = Motor(Motor2E, Motor2A, Motor2B, DebugTraceLevel.DEBUG)

motor1.start()
motor1.start()
motor1.reverse()
motor1.stop()
motor1.start()
motor1.stop()
motor2.start()
motor1.reverse()
motor2.stop()
motor1.stop()

