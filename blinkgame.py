#Star Trek Blink Game - blinkgame.py
#Program Based Of The Number Guessing Game Program Copyright Warren Sande, 2009
#Rest of The Program Copyright Alexander Parsan, 2014
#Released under MIT license   http://www.opensource.org/licenses/mit-license.php
#Version 0.0.1 of blinkgame
#Remember Gerbiter. Keep [Code] Bugs In Their Place. Since 2014



import RPi.GPIO as GPIO #Imports The RPi.GPIO module and gives it the short name "GPIO"
import time #Imports the Time Module 
import os #Imports OS Module for Bash Control 
import random #For Game Logic

#Sets Variables for LEDs and Game Logic
redled = 23
blueled = 11
yellowled = 37



secret = random.randint(1, 99) #pick a secret number
guess = 0 
tries = 0
wins = 0
sound = 0 #For Music Output
flag = 1  #A main flag
play = 1 #To end Game


#Sets GPIO Modes and Pins
GPIO.setwarnings(False) #Prevents Warnings from Showing Up in Console
GPIO.setmode(GPIO.BOARD) #Pin Numbers are as printed, not BCM
GPIO.setup(redled, GPIO.OUT) #Sets RED LED as Output
GPIO.setup(blueled, GPIO.OUT) #Sets Blue LED as Output
GPIO.setup(yellowled, GPIO.OUT) #Sets Yellow LED as output

#Main Program

#Uncomment the Following Code to get the answer printed out neatly at the top. Use this for testing any modifications. NO cheating :P
print "DEBUG MODE:"
print "\b"
print secret
print "\b"

#Main Game with Loops
os.popen("omxplayer tng_chirp_clean.mp3")
print "________________________"
print "Hello there.  I'm Captain Jean-Luc Picard of the USS Enterprise.!"
print "The Untited Federation of Planents has a problem. They must crack a hidden number. \bIt is a number from 1 to 99.  The computer wil give you 6 tries."
print "We wish you the best of luck, for all of our sakes. Thank You. Picard Out."
time.sleep(5)
os.popen("omxplayer tng_chirp_clean.mp3")
time.sleep(1)
print "You are now logged into the computer. LCARS Terminal 1 Ready."
while wins < 3 and play == 1:
    
        

    while guess != secret and tries < 6:
        guess = input("Please enter guess:") 
        if guess < secret:
            print "Number is Too low."
        elif guess > secret:
            print "Number is Too High"
        tries = tries + 1
    if guess == secret:
        os.popen("omxplayer tng_chirp_clean.mp3")
        wins = wins + 1
        sound = 1
        flag = 1

        if wins == 1:
            print "Picard Here. You Solved it! Your graceous help has been noticed at Starfleet. \bIf you'd like, we can appoint you Acing Ensign. \bTwo more codes are waiting to be solved if you wish."
            print "After all, you have only cracked Code"
            print wins
            print "of 3."
            GPIO.output(blueled,1) 
            os.popen("omxplayer tng_chime_clean.mp3")
            varcontinue = raw_input("Accept Assignment as Acting Ensign(Yes/No):")
            if varcontinue == "Yes":
                 tries = 0
                 secret = random.randint(1, 99)
                 #Uncomment Lines Below for Debug
                 print "DEBUG MODE:"
                 print "\b"
                 print secret
                 flag = 0
            elif varcontinue == "No":
                print "Thank you for your help. Starfleet will still remember your actions. "
                play = 0
                break




        
        if wins == 2:
            time.sleep(3)
            print "Picard Here. You Solved it again! You have one last code to crack."
            print "After all, you have cracked" 
            print wins
            print "codes of 3."
            GPIO.output(redled, 1)
            os.popen("omxplayer tng_chime_clean.mp3")
            varcontinue = raw_input("Continue?(Yes/No):")
            if varcontinue == "Yes":
                 tries = 0
                 secret = random.randint(1, 99)
                 #Uncomment Lines Below for Debug
                 print "DEBUG MODE:"
                 print "\b"
                 print secret
                 flag = 0
            elif varcontinue == "No":
                print "Thank you for your help. Starfleet will still remember your actions. "
                play = 0
                break




        if wins == 3:
            GPIO.output(yellowled, 1)
            print "Congratualions Actin Ensign! You have solved all three codes. You got the numbers!"
            time.sleep(2)
            os.popen("omxplayer tng_chime_clean.mp3")
            for loop in (0,3):
             GPIO.output(redled, 0)
             GPIO.output(blueled,0)
             GPIO.output(yellowled,0)
             os.popen("omxplayer tng_transporter1.mp3")
             time.sleep(2)
             GPIO.output(redled, 1)
             GPIO.output(blueled,1)
             GPIO.output(yellowled,1)
             os.popen("omxplayer tng_transporter1.mp3")
             time.sleep(2)
             

            

      
    else:
        print "LCARS TERMINAL:No more guesses!"
        print "The secret number was", secret


print "Game Finished."
GPIO.output(redled, 0)
GPIO.output(yellowled, 0)
GPIO.output(blueled, 0)
