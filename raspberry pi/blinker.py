import RPi.GPIO as GPIO
import time

# Use GPIO pin 
GPIO.setmode(GPIO.BCM) #BOARD -> BCM BOARD didn't work
# Set LED pin as output
GPIO.setup(10, GPIO.OUT)
# try this block of code
try:
    while 1:
        GPIO.output(10, GPIO.HIGH)
        time.sleep(0.25)
# Press ctrl + c to stop
except KeyboardInterrupt:
    GPIO.cleanup()
