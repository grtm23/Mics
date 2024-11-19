import time
import gopigo3
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()

servo1 = easy_gpg.init_servo("SERVO1")
servo2 = easy_gpg.init_servo("SERVO2")
my_distance_sensor_left = easy_gpg.init_distance_sensor("AD2")
my_distance_sensor_right = easy_gpg.init_distance_sensor("I2C")

GPG = gopigo3.GoPiGo3()
spin = False
def find():
    try:
        GPG.set_motor_power(GPG.MOTOR_LEFT, 0)
        GPG.set_motor_power(GPG.MOTOR_RIGHT, 0)
        EFR = False
        servo1.rotate_servo(160) 
        servo2.rotate_servo(0)
        spin = False
        rot1 = 0
        rot2 = 160
        #rush( go foward to a line and move)
        while True:
            if not EFR:

                rot2-=10
                rot1+=10
                servo2.rotate_servo(rot1) 
                servo1.rotate_servo(rot2)
            if my_distance_sensor_left.read_mm() < 650:
                '''
                GPG.set_motor_power(GPG.MOTOR_LEFT, -100)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, 100)
                print(rot1/10)
                print((rot1/10)*0.05375)
                
                time.sleep((rot1%10)*0.05375)
                GPG.reset_all()
                '''
                easy_gpg.turn_degrees(-rot1-10)
                #spin towards eye that saw bot
                servo1.rotate_servo(160) 
                servo2.rotate_servo(0)
                break
            if not spin and my_distance_sensor_right.read_mm() < 650:
                #spin
                '''
                GPG.set_motor_power(GPG.MOTOR_LEFT, 100)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, -100)
                time.sleep(((160-rot2)/10)*0.05375)
                
                '''
                easy_gpg.turn_degrees((160-rot2)+10)
                servo1.rotate_servo(160) 
                servo2.rotate_servo(0)
                break
            if rot1 == 90:#where the rotation maxes out
                EFR = True
                servo2.rotate_servo(0)
                rot1=90.5
            if EFR:
                GPG.set_motor_power(GPG.MOTOR_LEFT, -40)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, 40)
                spin=True

    except KeyboardInterrupt:
        GPG.set_motor_power(GPG.MOTOR_LEFT, 0)
        GPG.set_motor_power(GPG.MOTOR_RIGHT, 0)
