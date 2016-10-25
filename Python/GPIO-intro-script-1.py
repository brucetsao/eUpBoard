import RPi.GPIO as GPIO ## Import GPIO Library
GPIO.setmode(GPIO.BOARD) ## Use BOARD pin numbering
GPIO.setup(7, GPIO.OUT) ## Setup GPIO pin 7 to OUT
GPIO.output(7, True) ## Turn on GPIO pin 7
