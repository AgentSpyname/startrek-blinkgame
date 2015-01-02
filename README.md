Star Trek Blink Game
==================

A Star Trek themed, text based game written in Python, which showcases the power of the Raspberry Pi. This python script uses the GPIO pins of the Raspberry Pi to create a hardware-software text game.

##Beginners Guide!STOP and Read This First.
If you have come here, you are most likely new to the Raspberry Pi. If you have a good understanding of Linux, the Raspberry Pi, Python and some knowledge about GPIO and circuts skip to System Requiremnts.  This is a Star Trek themed number-guessing text game. 
It shows off the power of your new(or old) Raspberry Pi by using both the GPIO Pins and the Python Programming Language. 

You will first have to hook up a basic circut to your GPIO pins(the pins on the top left of the board). You will need some basic electric components. If this is your first time the GPIO pins, you need to purchase a breadboard, led lights, resistors and breadboarding jumper wire. 
These are relativley cheap from [Adafruit](www.adafruit.com) so make sure to grab those before starting.
If you are using the model A+ or B+ follow [this diagram](link) to find a diagram and more instrcutions on how to hook it up to the breadboard. Plug in a speaker to the audio jack. 
Then  run `sudo apt-get upgrade` and `sudo apt-get update` in terminal on your Raspberry Pi. Then run `git clone link` and `cd startrek-blinkgame`. Then `sudo python blinkgame.py`. If everything works you should be able to play the game, and the lights will light and sounds will play.

Try looking up the commands used in the script and modifying it. 



System Requiremnts 
-------

Raspberry Pi
-----
You must be using the Raspberry Pi to run this script. You will have to hook up a basic circut comprising of 3 leds. For instructions on wiring the circut, [click here](linkhere).

This script has been written to be run  on the Raspberry Pi Model A+ and Model B+. If you are using the A+ or B+ and hooked your LEDs to the same pins on the board in the script, the script should have no trouble running.  
To run this script on the orginal Model A or B or with diffrent pins, change variables `redled`, `blueled` and `yellowled` to the pin numbers you chose.

Software
-----
Ensure that you have the following software installed and up to date. All of this software comes pre-installed on the Pi.
* Python 2.7.3 or higher
* Omxplayer Version:98982df
* RPi.GPIO Library Installed



Installation
-----------

    git clone link

Usage
-----

    sudo python blinkgame.py
    


A handy script to turn the LEDs off if they were in use is included. Run it the same way as any Python script.

    sudo python ledoff.py
    

Contributing
------------

Any contributions and changes to the script are appreciated. Thanks!
--------

