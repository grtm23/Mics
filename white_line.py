import time
import gopigo3
import easygopigo3 as easy
easy_gpg = easy.EasyGoPiGo3()
GPG = gopigo3.GoPiGo3()
lineFollow = easy_gpg.init_line_follower("AD1")

import subprocess
import time

#get output of ps -e
psout = str(subprocess.check_output(["ps", "-e"]))

psout = psout[::-1]

index = psout.index("3nohtyp")

psout = psout[index+7:]

#May have to change if PID is 4 digits
endof=0
#LOOP for seeing line

try:
        #Find index of python in output
        index = psout.index("3nohtyp")
except:
        print("oopsie i had an ewwor")
while True:
        time.sleep(.15)
        if("w"in lineFollow.read("bivariate-str")):
                print("saw")
                print( psout[index+26:index+30][::-1])
                GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 0)
                try:
                        start = psout[index+26:index+30][::-1]
                        subprocess.check_output(["kill", "-TSTP", start])
                except:
                        start = psout[index+26:index+31][::-1]
                        subprocess.check_output(["kill", "-TSTP", start])
                GPG.set_motor_power(GPG.MOTOR_LEFT, 75)
                GPG.set_motor_power(GPG.MOTOR_RIGHT, -75)
                spin = True
                while spin:
                        time.sleep(.15)
                        if not "w"in lineFollow.read("bivariate-str"):
                                spin = False
                time.sleep(.3)
                for i in range(8):
                        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 100)
                        if "w"in lineFollow.read("bivariate-str"):
                                GPG.set_motor_power(GPG.MOTOR_LEFT, 100)
                                GPG.set_motor_power(GPG.MOTOR_RIGHT, -100)
                                time.sleep(.2)
                        time.sleep(.10)
                GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 0)
                print("continueing")
                subprocess.check_output(["kill", "-CONT", start])   
                    


#We found line, get away from line

#Drive away!!!
 