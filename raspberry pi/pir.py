# I import these library
import RPi.GPIO as GPIO
import time


# I connect these pin
pir_pin = 38 # PIR motion sensor connects to 38 pin 
led_pin=21 # LED connects to 21 pin
buzzer_pin=31 # buzzer connects to 31 pin
# this is pir state
state=0

# I set mode to BOARD
GPIO.setmode(GPIO.BOARD)
# I set pir_pin to GPIO.IN
GPIO.setup(pir_pin,GPIO.IN)
# I set led_pin and buzzer pin to GPIO.OUT
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)


try:
    while True:
        time.sleep(0.1)
        state=0
        state=GPIO.input(pir_pin)
        state-0
        if(state == 1): #if the pir motion sensor detect movement print detect
            # snf LED and buzzer inform users
            print("detect！")
            GPIO.output(led_pin, GPIO.HIGH)
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep( 0.1 ) 
        
        else: # else print no detect and nothing
            print("no detect")
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep( 0.1 )

except KeyboardInterrupt:
    GPIO.cleanup()

