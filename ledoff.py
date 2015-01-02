#_____________________________________
#LED Off - ledoff.py
#By:Alexander Parsan, Under The Creative Commons Agreement
#This script is to be run before dualblink.py to turn off all lights


import RPi.GPIO as GPIO #Imports The RPi.GPIO module and gives it the short name "GPIO"
import time #Imports the Time Module 


#Sets Variables for LEDs
redled = 23
blueled = 11
yellowled = 37

#Main Setup

GPIO.setmode(GPIO.BOARD) #Pin Numbers are as printed, not BCM
GPIO.setup(redled, GPIO.OUT) #Sets RED LED as Output
GPIO.setup(blueled, GPIO.OUT) #Sets Blue LED as Output
GPIO.setup(yellowled, GPIO.OUT)

#Turns All LEDs Off
GPIO.output(redled, 0)
GPIO.output(blueled, 0)
GPIO.output(yellowled, 0)