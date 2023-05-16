import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)# to avoid errors


# Pin numbers
led_pin = 2 #17
buzzer_pin = 3 #18
echo_pin =4 #23
trig_pin = 17 #24
button_pin = 23 #25

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to measure distance using the ultrasonic sensor
def measure_distance():
    # Trigger the ultrasonic sensor
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    # Measure the duration of the echo pulse
    while GPIO.input(echo_pin) == 0:
        pulse_start = time.time()

    while GPIO.input(echo_pin) == 1:
        pulse_end = time.time()

    # Calculate distance in centimeters
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

# Function to control the LED and Buzzer based on distance
def control_led_buzzer(distance):
    if distance <= 10:
        GPIO.output(led_pin, GPIO.HIGH)
        GPIO.output(buzzer_pin, GPIO.HIGH)
        print("Object detected!")
    else:
        GPIO.output(led_pin, GPIO.LOW)
        GPIO.output(buzzer_pin, GPIO.LOW)

# Main loop
try:
    while True:
        # Measure distance
        distance = measure_distance()
        control_led_buzzer(distance)

        # Check if button is pressed
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            GPIO.output(led_pin, GPIO.LOW)
            GPIO.output(buzzer_pin, GPIO.LOW)
            print("LED and Buzzer stopped.")
            break

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()


