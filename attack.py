import time
import gopigo3
from search import find
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()
servo1 = easy_gpg.init_servo("SERVO1")
servo2 = easy_gpg.init_servo("SERVO2")
my_distance_sensor_left = easy_gpg.init_distance_sensor("AD2")
my_distance_sensor_right = easy_gpg.init_distance_sensor("I2C")
#left
servo1.rotate_servo(160)
#right
servo2.rotate_servo(0)

GPG = gopigo3.GoPiGo3()

try:
    while True:
        leftdist = my_distance_sensor_left.read_mm()
        rightdist = my_distance_sensor_right.read_mm()
        while(leftdist  < 650 or rightdist < 650):
            if(leftdist  < 650 and rightdist < 650):
                #ram
                GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 100)

            
            if(leftdist  < 650 and not rightdist < 650):
                #turn right
                GPG.set_motor_power(GPG.MOTOR_LEFT, 50)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, 100)
               
            if(rightdist< 650 and not leftdist  < 650):
                #turn left
                GPG.set_motor_power(GPG.MOTOR_LEFT, 100)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, 50)
                
            if(not leftdist  < 650 and not rightdist< 650):
                find()
            leftdist = my_distance_sensor_left.read_mm()
            rightdist = my_distance_sensor_right.read_mm()
        
        find()
except KeyboardInterrupt:
    GPG.set_motor_power(GPG.MOTOR_LEFT, 0)
    GPG.set_motor_power(GPG.MOTOR_RIGHT, 0)