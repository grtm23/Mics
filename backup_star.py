import time
import gopigo3
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()
GPG = gopigo3.GoPiGo3()
lineFollow = easy_gpg.init_line_follower("AD1")
GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 100)
while True:
        time.sleep(.15)
        if("w"in lineFollow.read("bivariate-str")):
                GPG.set_motor_power(GPG.MOTOR_LEFT, 75)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, -75)
                spin = True
                while spin:
                        time.sleep(.15)
                        if not "w"in lineFollow.read("bivariate-str"):
                                spin = False
                time.sleep(.19)
                GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 100)
