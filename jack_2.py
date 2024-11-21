import time
import gopigo3
from search import find
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()
servo1 = easy_gpg.init_servo("SERVO1")
servo2 = easy_gpg.init_servo("SERVO2")
my_distance_sensor_left = easy_gpg.init_distance_sensor("I2C")
my_distance_sensor_right = easy_gpg.init_distance_sensor("AD2")
GPG = gopigo3.GoPiGo3()
lineFollow = easy_gpg.init_line_follower("AD1")

GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 50)
total=0

def infront(sensor):
    total=0
    for i in sensor:
        total+=i
    if total>0.8:
        return True
    return False

def whiteside(sensor):
    left=sensor[4]+sensor[5]+sensor[6]
    right=sensor[0]+sensor[1]+sensor[2]

    if left>right:
        return False
    return True

def turnRight():
    GPG.set_motor_power(GPG.MOTOR_LEFT, 100)
    GPG.set_motor_power(GPG.MOTOR_RIGHT, 30)

def turnLeft():
    GPG.set_motor_power(GPG.MOTOR_LEFT, 30)
    GPG.set_motor_power(GPG.MOTOR_RIGHT, 100)


while True:

    if infront(lineFollow.read("bivariate")):
        turnRight()

    if whiteside(lineFollow.read("bivariate")):
        turnRight()
        time.sleep(0.1)
    else:
        turnLeft()
        time.sleep(0.1)
        
        

GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 0)
