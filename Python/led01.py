import RPi.GPIO as GPIO ## Import GPIO library
GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(21, GPIO.OUT) ## Setup GPIO Pin 21 to OUT
GPIO.output(21,True) ## Turn on GPIO pin 